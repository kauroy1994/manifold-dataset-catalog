#!/usr/bin/env python3
"""Embed the illustrative JSON-LD in the checked-in viewer; no validation."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
example=json.loads((root/'examples/illustrative_nose_cone.jsonld').read_text(encoding='utf-8'))
encoded=json.dumps(example,indent=2,ensure_ascii=False).replace('<','\\u003c')
viewer=(root/'site/viewer.template.html').read_text(encoding='utf-8').replace('__EXAMPLE_JSON__',encoded)
# Source-tree links target Markdown; the website builder uses HTML links.
viewer=viewer.replace('href="../index.html"', 'href="../README.md"').replace('href="../docs/conceptual-peg.html"', 'href="../docs/conceptual-peg.md"')
(root/'examples/interactive_peg_viewer.html').write_text(viewer,encoding='utf-8')
print('Updated illustrative viewer. No manufacturing claim was validated.')
