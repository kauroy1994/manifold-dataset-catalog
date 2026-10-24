#!/usr/bin/env python3
"""Render README and Markdown into a static site, not an enhancement pipeline."""
from __future__ import annotations
import html, json, re, shutil, sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urlunsplit
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
try:
    from markdown_it import MarkdownIt
except ImportError as exc:
    raise SystemExit('Run: python -m pip install -r requirements-site.txt') from exc

def slug(text: str) -> str:
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', text.strip().lower()))

def output_name(name: str) -> str:
    p=PurePosixPath(name)
    return str(p.with_name('index.html') if p.name=='README.md' else p.with_suffix('.html'))

def rewrite_link(href: str) -> str:
    p=urlsplit(href)
    if p.scheme or p.netloc or not p.path.endswith('.md'):return href
    return urlunsplit(('', '', output_name(p.path), p.query, p.fragment))

def markdown_pages() -> list[Path]:
    pages=list(ROOT.glob('*.md'))
    for folder in ['catalog','docs','examples']:pages.extend((ROOT/folder).glob('*.md'))
    return sorted(pages)

def render_page(source: Path, layout: str) -> tuple[str,str]:
    parser=MarkdownIt('commonmark',{'html':False}).enable(['table','strikethrough'])
    tokens=parser.parse(source.read_text(encoding='utf-8'))
    toc=[];used={};title=source.stem
    for i,token in enumerate(tokens):
        if token.type=='heading_open':
            text=''.join(c.content for c in (tokens[i+1].children or []) if c.type in ['text','code_inline'])
            anchor=slug(text);count=used.get(anchor,0);used[anchor]=count+1
            if count:anchor+=f'-{count}'
            token.attrSet('id',anchor)
            if token.tag=='h1':title=text
            elif token.tag=='h2':toc.append((text,anchor))
        for child in token.children or []:
            if child.type=='link_open':child.attrSet('href',rewrite_link(child.attrGet('href') or ''))
    content=parser.renderer.render(tokens,parser.options,{})
    content=content.replace('<table>','<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable data table"><table>').replace('</table>','</table></div>')
    relative=source.relative_to(ROOT).as_posix();target=output_name(relative)
    prefix='../'*(len(PurePosixPath(target).parts)-1) or './';home=relative=='README.md'
    nav=''.join(f'<a href="#{html.escape(a)}">{html.escape(t)}</a>' for t,a in toc)
    breadcrumb='' if home else f'<div class="breadcrumb"><a href="{prefix}index.html">MANIFOLD</a> / DOCUMENTATION</div>'
    values={'__TITLE__':html.escape('Dataset catalog & research roadmap' if home else title),'__ROOT__':prefix,'__BODY_CLASS__':'home' if home else 'document','__TOC__':nav,'__BREADCRUMB__':breadcrumb,'__CONTENT__':content}
    result=layout
    for key,value in values.items():result=result.replace(key,value)
    return target,result

def build() -> int:
    if OUT.is_symlink():raise ValueError('Refusing to replace symlink at _site.')
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir()
    layout=(ROOT/'site/layout.html').read_text(encoding='utf-8')
    for source in markdown_pages():
        target,text=render_page(source,layout);p=OUT/target;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
    files=[ROOT/'LICENSE',ROOT/'references.bib',ROOT/'CITATION.cff']
    for folder,patterns in {'assets':['*.css','*.js'],'catalog':['*.json','*.csv'],'examples':['*.jsonld']}.items():
        for pattern in patterns:files.extend((ROOT/folder).glob(pattern))
    for source in files:
        p=OUT/source.relative_to(ROOT);p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,p)
    example=json.loads((ROOT/'examples/illustrative_nose_cone.jsonld').read_text(encoding='utf-8'))
    encoded=json.dumps(example,indent=2,ensure_ascii=False).replace('<','\\u003c')
    viewer=(ROOT/'site/viewer.template.html').read_text(encoding='utf-8').replace('__EXAMPLE_JSON__',encoded)
    (OUT/'examples/interactive_peg_viewer.html').write_text(viewer,encoding='utf-8')
    (OUT/'.nojekyll').write_text('',encoding='utf-8')
    (OUT/'build-info.json').write_text(json.dumps({'version':'0.1.0-planning','homepage_source':'README.md','scope':'Documentation only; no manufacturing data validated.'},indent=2)+'\n',encoding='utf-8')
    pages=len(list(OUT.rglob('*.html')));print(f'Built {pages} HTML pages in {OUT}.');return pages

if __name__=='__main__':
    try:build()
    except (OSError,ValueError) as exc:sys.exit(f'Site build failed: {exc}')
