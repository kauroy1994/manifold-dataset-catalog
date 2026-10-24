/* Visualization of a fixed conceptual example; no data inference or verification. */
'use strict';
(() => {
 const doc = JSON.parse(document.getElementById('dataset').textContent);
 const byId = Object.fromEntries(doc['@graph'].map(x => [x['@id'], x]));
 const nodes = [
  {id:'peg:rocket-assembly-procedure',x:185,y:105,r:48,kind:'meta',label:['Expected','procedure']},
  {id:'peg:expected-body-ready',x:185,y:300,r:60,kind:'state',label:['Body ready','nose not installed']},
  {id:'peg:expected-complete',x:555,y:300,r:56,kind:'complete',label:['Expected','complete rocket']},
  {id:'peg:example-defective-execution',x:825,y:105,r:58,kind:'meta',label:['Illustrative','NoNoseCone cycle']},
  {id:'peg:observed-final-incomplete',x:825,y:470,r:64,kind:'defect',label:['Illustrative','incomplete rocket']},
  {id:'peg:missing-nose-cone-deviation',x:510,y:495,r:61,kind:'deviation',label:['Installation','not established']},
  {id:'peg:cycle-level-defect-annotation',x:185,y:525,r:58,kind:'evidence',label:['Category','reference only']},
  {id:'peg:nose-cone',x:555,y:105,r:44,kind:'component',label:['Nose cone']},
  {id:'peg:future-factories-v1',x:1005,y:300,r:49,kind:'meta',label:['Source family','FF23 / V1']}
 ];
 const initial = nodes.map(n=>({id:n.id,x:n.x,y:n.y}));
 const edges = [
  {id:'peg:expected-install-nose-cone',from:'peg:expected-body-ready',to:'peg:expected-complete',kind:'operation',label:'expected: install_nose_cone'},
  {id:'e1',from:'peg:rocket-assembly-procedure',to:'peg:expected-body-ready',kind:'membership',label:'hasState'},
  {id:'e2',from:'peg:rocket-assembly-procedure',to:'peg:expected-complete',kind:'membership',label:'hasState'},
  {id:'e3',from:'peg:example-defective-execution',to:'peg:observed-final-incomplete',kind:'membership',label:'hasState'},
  {id:'e4',from:'peg:example-defective-execution',to:'peg:missing-nose-cone-deviation',kind:'membership',label:'hasDeviation'},
  {id:'e5',from:'peg:missing-nose-cone-deviation',to:'peg:expected-install-nose-cone',kind:'association',label:'requiredOperation',targetEdge:true},
  {id:'e6',from:'peg:cycle-level-defect-annotation',to:'peg:observed-final-incomplete',kind:'evidence',label:'category reference'},
  {id:'e7',from:'peg:cycle-level-defect-annotation',to:'peg:missing-nose-cone-deviation',kind:'evidence',label:'category reference'},
  {id:'e8',from:'peg:expected-install-nose-cone',to:'peg:nose-cone',kind:'association',label:'component',sourceEdge:true},
  {id:'e9',from:'peg:example-defective-execution',to:'peg:future-factories-v1',kind:'association',label:'sourceDataset'},
  {id:'e10',from:'peg:rocket-assembly-procedure',to:'peg:future-factories-v1',kind:'association',label:'sourceDataset'}
 ];
 const colors={state:['#dbeaf7','#4f7799'],complete:['#dceee1','#3f7964'],defect:['#f3ddd5','#aa705d'],deviation:['#f5e8c4','#a57c38'],evidence:['#fcf3dc','#a18851'],meta:['#e9e6f3','#807498'],component:['#e3eef1','#6e91a0']};
 const ns='http://www.w3.org/2000/svg', svg=document.getElementById('graph');
 function el(tag,attrs={},parent=svg){const e=document.createElementNS(ns,tag);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,v);parent.appendChild(e);return e;}
 const defs=el('defs');
 for(const [id,color]of [['normal','#617d89'],['evidence','#a58b4e']]){const m=el('marker',{id:'arrow-'+id,viewBox:'0 0 10 10',refX:9,refY:5,markerWidth:6,markerHeight:6,orient:'auto-start-reverse'},defs);el('path',{d:'M0 0 L10 5 L0 10 Z',fill:color},m);}
 const scene=el('g'); let mode='all',selected=null,scale=1,tx=0,ty=0,drag=null,pan=null;
 const nodeMap=Object.fromEntries(nodes.map(n=>[n.id,n]));
 function endpoint(id){if(nodeMap[id])return nodeMap[id];const op=edges.find(e=>e.id===id);if(!op)return null;const a=nodeMap[op.from],b=nodeMap[op.to];return {x:(a.x+b.x)/2,y:(a.y+b.y)/2,r:0};}
 function visible(e){if(mode==='all')return true;if(mode==='procedure')return ['peg:expected-install-nose-cone','e1','e2','e8','e10'].includes(e.id);return ['e3','e4','e5','e6','e7','e9'].includes(e.id);}
 function draw(){
  scene.replaceChildren();const shown=edges.filter(visible);const ids=new Set(shown.flatMap(e=>[e.from,e.to]));
  if(mode==='deviation'){ids.add('peg:expected-body-ready');ids.add('peg:expected-complete');}
  for(const e of shown){const a=endpoint(e.from),b=endpoint(e.to);if(!a||!b)continue;const dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1,ux=dx/d,uy=dy/d;
   const x1=a.x+ux*a.r,y1=a.y+uy*a.r,x2=b.x-ux*(b.r+8),y2=b.y-uy*(b.r+8);
   const g=el('g',{class:'edge'+(selected===e.id?' selected':''),'data-id':e.id},scene);
   el('path',{d:`M${x1},${y1} L${x2},${y2}`,stroke:e.kind==='evidence'?'#a58b4e':'#617d89','stroke-dasharray':e.kind==='operation'?'none':'5 5','marker-end':'url(#arrow-'+(e.kind==='evidence'?'evidence':'normal')+')'},g);
   el('text',{x:(x1+x2)/2,y:(y1+y2)/2-10,'text-anchor':'middle',class:'edge-label'},g).textContent=e.label;
   g.addEventListener('click',ev=>{ev.stopPropagation();inspect(e.id);});
  }
  for(const n of nodes){if(mode!=='all'&&!ids.has(n.id))continue;const [fill,stroke]=colors[n.kind];const g=el('g',{class:'node'+(selected===n.id?' selected':''),'data-id':n.id},scene);el('circle',{cx:n.x,cy:n.y,r:n.r,fill,stroke},g);
   n.label.forEach((s,i)=>el('text',{x:n.x,y:n.y+(i-(n.label.length-1)/2)*18+4,class:'node-label'},g).textContent=s);
   g.addEventListener('click',ev=>{ev.stopPropagation();inspect(n.id);});
   g.addEventListener('pointerdown',ev=>{ev.stopPropagation();const p=point(ev);drag={node:n,x:p.x,y:p.y,ox:n.x,oy:n.y};svg.setPointerCapture(ev.pointerId);});
  }
 }
 function inspect(id){selected=id;const item=byId[id],edge=edges.find(e=>e.id===id);const data=item||{displayRelation:edge.label,from:edge.from,to:edge.to,representation:'Display projection of a JSON-LD reference; not an additional source observation'};
  document.getElementById('ptitle').textContent=item?.name||edge.label;document.getElementById('ptype').textContent=item?.['@type']||'Display relationship';
  const details=document.getElementById('details');details.replaceChildren();
  for(const [k,v]of Object.entries(data)){const row=document.createElement('div');row.className='kv';const key=document.createElement('span');key.className='k';key.textContent=k;const val=document.createElement('span');val.className='v';val.textContent=v===null?'not specified — no source value asserted':typeof v==='object'?JSON.stringify(v):String(v);row.append(key,val);details.append(row);}
  document.getElementById('item-select').value=id;draw();
 }
 const select=document.getElementById('item-select');
 for(const item of doc['@graph']){const o=document.createElement('option');o.value=item['@id'];o.textContent=item.name||item['@id'];select.appendChild(o);}
 select.addEventListener('change',()=>{if(select.value)inspect(select.value);});
 function transform(){scene.setAttribute('transform',`translate(${tx} ${ty}) scale(${scale})`);}
 function point(ev){const p=svg.createSVGPoint();p.x=ev.clientX;p.y=ev.clientY;return p.matrixTransform(svg.getScreenCTM().inverse());}
 svg.addEventListener('pointerdown',ev=>{if(drag)return;const p=point(ev);pan={x:p.x,y:p.y,tx,ty};svg.setPointerCapture(ev.pointerId);svg.classList.add('panning');});
 svg.addEventListener('pointermove',ev=>{const p=point(ev);if(drag){drag.node.x=drag.ox+(p.x-drag.x)/scale;drag.node.y=drag.oy+(p.y-drag.y)/scale;draw();}else if(pan){tx=pan.tx+p.x-pan.x;ty=pan.ty+p.y-pan.y;transform();}});
 const end=()=>{drag=null;pan=null;svg.classList.remove('panning');};svg.addEventListener('pointerup',end);svg.addEventListener('pointercancel',end);
 function zoom(k){scale=Math.max(.5,Math.min(2.6,scale*k));transform();}
 svg.addEventListener('wheel',ev=>{ev.preventDefault();zoom(ev.deltaY<0?1.1:.9);},{passive:false});
 document.getElementById('zin').onclick=()=>zoom(1.2);document.getElementById('zout').onclick=()=>zoom(.8);
 document.getElementById('reset').onclick=()=>{scale=1;tx=0;ty=0;initial.forEach(p=>Object.assign(nodeMap[p.id],{x:p.x,y:p.y}));transform();draw();};
 for(const m of ['all','procedure','deviation'])document.getElementById(m).onclick=()=>{mode=m;for(const b of ['all','procedure','deviation']){document.getElementById(b).classList.toggle('active',b===m);document.getElementById(b).setAttribute('aria-pressed',String(b===m));}draw();};
 document.getElementById('download').onclick=()=>{const blob=new Blob([JSON.stringify(doc,null,2)],{type:'application/ld+json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='manifold_illustrative_not_verified.jsonld';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
 draw();
})();
