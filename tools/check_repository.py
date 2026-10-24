#!/usr/bin/env python3
"""Offline catalog/documentation checks; NOT scientific data verification."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]

def check() -> list[str]:
    errors=[];data=json.loads((ROOT/'catalog/datasets.json').read_text(encoding='utf-8'))
    assets=data['assets'];campaigns={c['id'] for c in data['campaigns']}
    if len(assets)!=4 or len(campaigns)!=2:errors.append('Expected four assets / two campaigns.')
    if len({a['id'] for a in assets})!=len(assets):errors.append('Duplicate asset ID.')
    urls=[]
    for a in assets:
        if a['campaign_id'] not in campaigns:errors.append('Unrecognized campaign.')
        if a['catalog_status']!='publication_reported':errors.append('Preserve publication-reported status.')
        for f in ['raw_data_included','file_inventory_audited','source_version_pinned']:
            if a[f] is not False:errors.append(f'{a["id"]}: unsupported {f}.')
        parts=a['upstream_parts']
        if sorted(p['part'] for p in parts)!=list(range(1,len(parts)+1)):errors.append('Missing part in '+a['id'])
        for p in parts:
            if p['parts_total']!=len(parts):errors.append('Inconsistent part count.')
            u=urlsplit(p['url'])
            if u.scheme!='https' or u.netloc!='www.kaggle.com':errors.append('Unexpected upstream host.')
            if u.path!='/datasets/'+p['kaggle_identifier']:errors.append('Kaggle identifier mismatch.')
            if p['download_verified'] or p['raw_file_license_verified']:errors.append('Unsupported download audit claim.')
            urls.append(p['url'])
    if len(urls)!=11 or len(set(urls))!=11:errors.append('Expected 11 distinct upstream URLs.')
    ledger=json.loads((ROOT/'catalog/link-checks.json').read_text(encoding='utf-8'))
    if {p['url'] for p in ledger['links']}!=set(urls):errors.append('Link ledger mismatch.')
    example=json.loads((ROOT/'examples/illustrative_nose_cone.jsonld').read_text(encoding='utf-8'))
    ids={x['@id'] for x in example['@graph']}
    refs=['sourceDataset','expectedProcedure','execution','fromState','toState','requiredOperation','evidence','component','hasState','hasOperation','hasDeviation']
    for item in example['@graph']:
        for f in ['sourceCycleId','startTime','endTime','confidence']:
            if item.get(f) is not None:errors.append('Illustration asserts a measurement in '+item['@id'])
        for k in refs:
            if k not in item:continue
            for v in item[k] if isinstance(item[k],list) else [item[k]]:
                if v not in ids:errors.append('Unresolved example reference: '+v)
    text=(ROOT/'examples/interactive_peg_viewer.html').read_text(encoding='utf-8')
    m=re.search(r'<script id="dataset" type="application/json">(.*?)</script>',text,re.S)
    if not m or json.loads(m.group(1))!=example:errors.append('Viewer embedded JSON-LD out of sync.')
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    for term in ['PRE-AWARD','not','illustrative','University of South Carolina','11','NoNoseCone']:
        if term not in readme:errors.append('Missing scope note: '+term)
    for a in assets:
        card=ROOT/f'catalog/{a["slug"]}.md'
        if not card.exists():errors.append('Missing card: '+a['id']);continue
        text=card.read_text(encoding='utf-8')
        for p in a['upstream_parts']:
            if p['url'] not in text:errors.append('Card omits part: '+p['url'])
    return errors

if __name__=='__main__':
    try:errors=check()
    except (OSError,ValueError,KeyError) as exc:sys.exit('Repository check failed: '+str(exc))
    if errors:
        print('\n'.join('ERROR: '+e for e in errors));sys.exit(1)
    print('PASS: catalog bookkeeping, 11 published links, illustrative-example consistency.')
    print('NOT TESTED: downloads, manufacturing correctness, privacy clearance, research performance.')
