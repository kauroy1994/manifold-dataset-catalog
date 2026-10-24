"""Documentation tests only; these are not manufacturing evaluation results."""
from __future__ import annotations
import json,re,sys,unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build_site import build,rewrite_link
from check_repository import check

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.has_lang=False;self.has_title=False
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.add(d['id'])
        if tag=='html' and d.get('lang')=='en':self.has_lang=True
        if tag=='title':self.has_title=True
        for attr in ['href','src']:
            if attr in d:self.links.append(d[attr])

class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages=build();cls.data=json.loads((ROOT/'catalog/datasets.json').read_text(encoding='utf-8'))
    def test_catalog_consistency(self):self.assertEqual(check(),[])
    def test_scope(self):
        self.assertEqual(len(self.data['assets']),4);self.assertEqual(len(self.data['campaigns']),2)
    def test_part_count(self):self.assertEqual(sum(len(a['upstream_parts']) for a in self.data['assets']),11)
    def test_no_false_audits(self):
        for a in self.data['assets']:
            self.assertFalse(a['file_inventory_audited']);self.assertFalse(a['raw_data_included'])
            for p in a['upstream_parts']:self.assertFalse(p['download_verified'])
    def test_ff24_sampling_not_invented(self):
        for a in self.data['assets']:
            if a['campaign_id']=='FF24':self.assertIsNone(a['reported_sampling_hz'])
    def test_readme_is_homepage(self):
        text=(ROOT/'_site/index.html').read_text(encoding='utf-8')
        for title in ['Dataset catalog','What exists now','Proposed team','Responsible reuse','README.md']:self.assertIn(title,text)
    def test_link_rewriting(self):
        self.assertEqual(rewrite_link('../README.md#dataset-catalog'),'../index.html#dataset-catalog')
        self.assertEqual(rewrite_link('docs/roadmap.md'),'docs/roadmap.html')
        self.assertEqual(rewrite_link('https://example.org/a.md'),'https://example.org/a.md')
    def test_all_local_site_links(self):
        site=ROOT/'_site';parsers={}
        for path in site.rglob('*.html'):
            p=Links();p.feed(path.read_text(encoding='utf-8'));parsers[path.resolve()]=p
        errors=[]
        for path,p in parsers.items():
            for link in p.links:
                u=urlsplit(link)
                if u.scheme or u.netloc:continue
                target=(path.parent/unquote(u.path)).resolve() if u.path else path
                if target.is_dir():target=target/'index.html'
                if not target.exists():errors.append(f'{path.relative_to(site)} -> {link}')
                elif u.fragment and target.suffix=='.html' and target in parsers and unquote(u.fragment) not in parsers[target].ids:errors.append(f'Missing anchor {link}')
        self.assertEqual(errors,[])
    def test_page_metadata(self):
        for path in (ROOT/'_site').rglob('*.html'):
            p=Links();p.feed(path.read_text(encoding='utf-8'));self.assertTrue(p.has_lang,path.name);self.assertTrue(p.has_title,path.name)
    def test_no_raw_data_or_private_documents_published(self):
        self.assertFalse(any(p.suffix.lower() in ['.pdf','.jpg','.jpeg','.png','.pt','.pth','.safetensors'] for p in (ROOT/'_site').rglob('*')))
    def test_example_not_measured(self):
        d=json.loads((ROOT/'examples/illustrative_nose_cone.jsonld').read_text(encoding='utf-8'))
        for obj in d['@graph']:
            for key in ['confidence','startTime','endTime','sourceCycleId']:self.assertIsNone(obj.get(key))
    def test_no_broken_template_tokens(self):
        for path in (ROOT/'_site').rglob('*.html'):self.assertIsNone(re.search(r'__(?:TITLE|ROOT|CONTENT|TOC|EXAMPLE_JSON|BODY_CLASS|BREADCRUMB)__',path.read_text(encoding='utf-8')))
    def test_no_owner_placeholder_on_homepage(self):
        text=(ROOT/'_site/index.html').read_text(encoding='utf-8')
        for x in ['YOUR_USERNAME','<username>','TODO','[confirmed']:self.assertNotIn(x,text)
    def test_source_viewer_local_links(self):
        source=ROOT/'examples/interactive_peg_viewer.html'
        p=Links();p.feed(source.read_text(encoding='utf-8'))
        for link in p.links:
            u=urlsplit(link)
            if u.scheme or u.netloc or not u.path:continue
            self.assertTrue((source.parent/unquote(u.path)).resolve().exists(),link)
    def test_references_complete(self):
        text=(ROOT/'references.bib').read_text(encoding='utf-8');self.assertEqual(text.count('@misc{'),2)
        for key in ['harik2024future','harik2025future']:self.assertIn(key,text)
        self.assertNotIn('and others',text)

if __name__=='__main__':unittest.main()
