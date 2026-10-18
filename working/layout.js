/* Shared, deterministic word layout. Glyph geometry stays unchanged. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.DoyleLayout=api})(globalThis,function(){
'use strict';
function keyFor(ch,bank,options){return ch==='A'&&options.capitalA==='body'&&bank['A.body']?'A.body':ch}
function adjustment(a,b,options,model){if(!a||!options.optical)return 0;return model.kern[model.groups[a.key]||a.key]?.[model.groups[b.key]||b.key]||0}
function bridges(records,options,model){
 if(!options.joins)return[];const out=[];
 for(let i=1;i<records.length;i++){
  const a=records[i-1],b=records[i],ga=model.groups[a.key]||a.ch,gb=model.groups[b.key]||b.ch;
  if(!/^[a-z]$/.test(ga)||!/^[a-z]$/.test(gb)||!a.g||!b.g)continue;
  const exit=model.joins[ga]?.exit,entry=model.joins[gb]?.entry;if(!exit||!entry)continue;
  const p=[a.x+exit[0],exit[1]],q=[b.x+entry[0],entry[1]],dx=q[0]-p[0],dy=q[1]-p[1];
  // Short, monotonic upstrokes only. A steep connector can read as an extra minim.
  if(dx<20||dx>model.bridge.max_gap||Math.abs(dy)>model.bridge.max_rise||Math.abs(dy)>Math.max(42,dx*1.6))continue;
  const d=`M${p} C${p[0]+dx*.35},${p[1]+dy*.15} ${q[0]-dx*.35},${q[1]-dy*.15} ${q}`;
  out.push({d,left:a.ch,right:b.ch,start:p,end:q,width:model.bridge.width});
 }
 return out;
}
function shapeRuns(units,bank,options,model,maxWidth=Infinity){
 const runs=[];let records=[],cursor=0,previous=null;
 function finish(){if(!records.length)return;runs.push({records,width:cursor,bridges:bridges(records,options,model)});records=[];cursor=0;previous=null}
 for(const unit of units){
  const ch=typeof unit==='string'?unit:unit.ch,key=typeof unit==='string'?keyFor(ch,bank,options):unit.key;
  const space=ch===' '||ch==='\u00a0',g=space?null:bank[key];const advance=space?model.word_space:g?.advance||500;
  const rec={ch,key,g,space,x:0,advance};let x=cursor+adjustment(previous,rec,options,model);
  if(records.length&&x+advance>maxWidth){finish();x=0}
  rec.x=x;records.push(rec);cursor=x+advance;previous=space||!g?null:rec;
 }
 finish();return runs;
}
function shapeRun(units,bank,options,model){return shapeRuns(units,bank,options,model)[0]||{records:[],width:0,bridges:[]}}
return {keyFor,adjustment,bridges,shapeRun,shapeRuns};
});
