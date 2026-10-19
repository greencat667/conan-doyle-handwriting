from pathlib import Path
import base64,json
P=Path(__file__).resolve().parents[1];O=P/'outputs'
html=r'''<!doctype html><!-- Code: MIT. Embedded font and glyph artwork: CC-BY-SA-2.0. See LICENSE, LICENSE-FONT and outputs/notice.md. --><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Doyle Desk — write in Conan Doyle’s hand</title>
<style>@font-face{font-family:Doyle;src:url(data:font/ttf;base64,FONTDATA)}*{box-sizing:border-box}body{margin:0;background:#e6e1d5;color:#25383c;font:16px system-ui}main{max-width:1220px;margin:auto;padding:38px 24px}header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #b9b5a7;padding-bottom:20px}h1{font:38px Georgia;margin:5px 0}small,.sub{color:#66695e}.layout{display:grid;grid-template-columns:320px 1fr;gap:30px;margin-top:30px}label{display:block;font-size:13px;margin:20px 0 8px}textarea{width:100%;height:210px;resize:vertical;padding:14px;background:#faf8f0;border:1px solid #bab7a8;font:16px/1.5 Georgia}select,input[type=range]{width:100%}button{background:#29474b;color:#fff;border:0;padding:12px 16px;cursor:pointer;border-radius:3px;margin:5px 5px 5px 0}button.secondary{background:transparent;color:#29474b;border:1px solid #8c9894}#paper{background:#faf7ed;box-shadow:0 5px 22px #28382b20;overflow:auto;min-height:440px}svg{display:block;width:100%;height:auto}.notice{font-size:12px;line-height:1.6;margin:20px 0;color:#716345}#status{font-size:12px;line-height:1.6}.downloads{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:18px;font-size:14px}.downloads a{color:#29474b;text-underline-offset:3px}.foot{font-size:12px;line-height:1.7;margin-top:25px}a{color:inherit}@media(max-width:760px){.layout{grid-template-columns:1fr}h1{font-size:29px}}</style>
<main><header><div><small>ARTHUR CONAN DOYLE’S HANDWRITING</small><h1>The Doyle Desk</h1><div class="sub">A little Victorian correspondence, in your browser.</div></div><small>v0.8.1 · an experimental recreation</small></header><nav class="downloads" aria-label="Downloads and source"><a href="conan-doyle-letters-study.ttf" download>Download font</a><a href="https://github.com/greencat667/the-doyle-desk/releases/latest">Download project</a><a href="https://github.com/greencat667/the-doyle-desk">Source &amp; licences</a></nav><div class="layout"><aside>
<label for="text">YOUR NOTE</label><textarea id="text">elementary my dear Watson

I have a curious case to consider.

With kind regards,
Arthur Conan Doyle</textarea>
<label for="source">LETTERFORMS</label><select id="source"><option value="clean">Complete study · v0.8</option><option value="legacy">v0.2 · previous mixed draft</option></select><label for="capitalA">CAPITAL A</label><select id="capitalA"><option value="signature">Signature form</option><option value="body">Rounded letter-body form</option></select><label for="mode">TREATMENT</label><select id="mode"><option value="note">Handwritten note — experimental joins</option><option value="font">Font proof — fixed letterforms</option></select>
<label for="spacing">SPACING &amp; JOINS</label><select id="spacing"><option value="optical">Revised · optical spacing</option><option value="previous">Previous · v0.6 layout</option></select><label for="size">LETTER SIZE <span id="sizeLabel"></span></label><input id="size" type="range" min="24" max="70" value="52">
<label><input id="transparent" type="checkbox"> Transparent export background</label>
<button id="png">Save PNG</button><button id="svg" class="secondary">Save SVG</button><button id="vary" class="secondary">Another variation</button><button id="alphabet" class="secondary">Character sheet</button><button id="words" class="secondary">Word proof</button>
<p id="status"></p><p class="notice">Capital A defaults to the pointed signature form; the rounded A from “America” is available above. Full A–Z, a–z, digits, standard punctuation and selected accented letters. X, Z, 6, 7, £, &amp;, double quotation marks, + and = use inferred designs matched to the reviewed handwriting. !, ?, apostrophe, dash, period and comma use source traces. Accents and smart punctuation are composed. The amber list identifies these forms in your text. Unsupported symbols still appear as boxes.</p>
</aside><section><div id="paper"></div><div class="foot">Main letterforms combine reviewed Ransom Center manuscripts, the 1901 Smith letter and the 1886 draft. Per-character provenance accompanies the font. Manuscript images: Harry Ransom Center, The University of Texas at Austin; Smith letter: Special Collections Toronto Public Library, CC BY-SA 2.0. Font and glyph artwork: <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA 2.0</a>. Code: MIT. Full credits and modifications are recorded in notice.md. Contemporary image-assisted forms are labelled as inferred and are not historical attestations. Optical spacing is shared with the font; note joins remain experimental. The previous v0.6 layout and v0.2 draft remain selectable for comparison. The installable font is included separately. No text leaves this page.</div></section></div></main>
<script>LAYOUTCODE
const layoutModel=LAYOUTDATA;const allGlyphs=GLYPHDATA;let glyphs=allGlyphs.clean;let seed=23;const $=s=>document.getElementById(s);let currentSvg='';
function rng(s){return()=>{s|=0;s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function esc(s){return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;')}
function shape(g){if(g.d)return g.d;return g.paths.map(p=>'M'+p.map(q=>q.join(',')).join('L')+'Z').join('')}
function endpoint(g,right){let pts=g.paths.flat().filter(p=>p[1]>-100&&p[1]<230);if(!pts.length)return null;return pts.reduce((a,b)=>right?(b[0]>a[0]?b:a):(b[0]<a[0]?b:a))}
function glyphKey(ch){return ch==='A'&&$('capitalA').value==='body'&&glyphs['A.body']?'A.body':ch}
function renderPrevious(){glyphs=allGlyphs[$('source').value];const text=$('text').value;const size=+$('size').value;const scale=size/1000;const random=rng(seed);const organic=$('mode').value==='note';const W=1000,pad=65;let x=pad,y=105,prev=null,body='',unsupported=new Set(),provisional=new Set();$('sizeLabel').textContent=size;
const parts=text.split(/(\n|[^\S\n]+)/);for(const word of parts){if(word==='\n'){x=pad;y+=size*1.9;prev=null;continue}if(/^\s+$/.test(word)){x+=size*.38;prev=null;continue}
const match=word.match(/^([A-Za-z]+)([^A-Za-z]*)$/);const units=organic&&match&&glyphs['word.'+match[1]]?['word.'+match[1],...match[2]]:[...word];
const wordWidth=units.reduce((s,c)=>s+Math.max(glyphs[glyphKey(c)]?.advance||500,glyphs[c+'.alt']?.advance||0)*scale*1.01,0);if(x+wordWidth>W-pad&&x>pad){x=pad;y+=size*1.9;prev=null}
for(const ch of units){if(x>W-pad-size*.5){x=pad;y+=size*1.9;prev=null}const kern={'To':-55,'Ta':-40,'Th':-25,'Wa':-40,'Wo':-40,'Yo':-45,'Av':-35,'Ar':-20,'ro':-22,'re':-22,'ve':-18,'ov':-18};if(prev)x+=(kern[prev.ch+ch]||0)*scale;let key=organic&&glyphs[ch+'.alt']&&random()>.52?ch+'.alt':ch;if(key===ch)key=glyphKey(ch);let g=glyphs[key];if(!g){unsupported.add(ch);body+=`<rect x="${x}" y="${y-size*.6}" width="${size*.45}" height="${size*.6}" fill="none" stroke="#b27643"/>`;x+=size*.6;prev=null;continue}if(g.kind!=='traced')provisional.add(ch);
let dy=organic?(random()-.5)*size*.035:0;let rotation=organic?(random()-.5)*1.4:0;const entry=endpoint(g,false),exit=endpoint(g,true);
if(organic&&prev&&/^[a-z]$/.test(ch)&&/^[a-z]$/.test(prev.ch)&&entry&&prev.exit&&($('source').value==='legacy'||'abcdehiklmnouvw'.includes(prev.ch))){let a=[prev.x+prev.exit[0]*scale,prev.y-prev.exit[1]*scale],b=[x+entry[0]*scale,y+dy-entry[1]*scale];let gap=b[0]-a[0];if(gap>0&&gap<size*.24&&Math.abs(b[1]-a[1])<size*.26)body+=`<path d="M${a} C${a[0]+gap*.4},${a[1]} ${b[0]-gap*.4},${b[1]} ${b}" fill="none" stroke="#25383e" stroke-width="${size*.035}" stroke-linecap="round"/>`}
body+=`<path d="${shape(g)}" transform="translate(${x} ${y+dy}) rotate(${rotation}) scale(${scale} ${-scale})" fill="#25383e" opacity="${organic?.91+random()*.09:1}"/>`;
prev={ch,x,y:y+dy,exit};x+=g.advance*scale*(organic?.98+random()*.025:1)}}
const H=Math.max(530,y+90);currentSvg=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${$('transparent').checked?'':`<rect width="100%" height="100%" fill="#faf7ed"/>`}${body}</svg>`;$('paper').innerHTML=currentSvg;
$('status').innerHTML=(unsupported.size?'<b>Unsupported:</b> '+esc([...unsupported].join(' '))+'<br>':'')+(provisional.size?'<span style="color:#9a651e">Reconstructed or composed: '+esc([...provisional].sort().join(' '))+'</span>':'All visible characters in this note use traced forms.')}
function render(){
 $('spacing').disabled=$('source').value==='legacy';
 if($('spacing').value==='previous'||$('source').value==='legacy'){renderPrevious();return}
 glyphs=allGlyphs.clean;const size=+$('size').value,scale=size/1000,organic=$('mode').value==='note',random=rng(seed),options={optical:true,joins:organic,capitalA:$('capitalA').value};
 const W=1000,pad=65,limit=(W-pad*2)/scale;let x=pad,y=105,body='',unsupported=new Set(),provisional=new Set();$('sizeLabel').textContent=size;
 const text=$('text').value.normalize('NFC').replace(/\r\n?/g,'\n');
 for(const word of text.split(/(\n|[ \t]+)/)){
  if(!word)continue;if(word==='\n'){x=pad;y+=size*1.9;continue}
  if(/^[ \t]+$/.test(word)){x+=[...word].reduce((n,c)=>n+(c==='\t'?4:1),0)*layoutModel.word_space*scale;continue}
  const units=[...word],whole=DoyleLayout.shapeRun(units,glyphs,options,layoutModel);
  if(x+whole.width*scale>W-pad&&x>pad){x=pad;y+=size*1.9}
  const runs=whole.width<=limit?[whole]:DoyleLayout.shapeRuns(units,glyphs,options,layoutModel,limit);
  for(let ri=0;ri<runs.length;ri++){
   if(ri){x=pad;y+=size*1.9}const run=runs[ri],dy=organic?(random()-.5)*size*.025:0,opacity=organic?.96+random()*.04:1;
   let ink='';for(const bridge of run.bridges)ink+=`<path data-join="${esc(bridge.left+bridge.right)}" d="${bridge.d}" fill="none" stroke="#25383e" stroke-width="${bridge.width}" stroke-linecap="round"/>`;
   for(const rec of run.records){
    if(rec.space)continue;if(!rec.g){unsupported.add(rec.ch);ink+=`<rect x="${rec.x}" y="0" width="450" height="600" fill="none" stroke="#b27643" stroke-width="18"/>`;continue}
    if(rec.g.kind!=='traced')provisional.add(rec.ch);
    ink+=`<path data-character="${esc(rec.ch)}" d="${shape(rec.g)}" transform="translate(${rec.x} 0)" fill="#25383e"/>`;
   }
   body+=`<g data-word="${esc(run.records.map(r=>r.ch).join(''))}" data-advance="${run.width}" transform="translate(${x} ${y+dy}) scale(${scale} ${-scale})" opacity="${opacity}">${ink}</g>`;x+=run.width*scale;
  }
 }
 const H=Math.max(530,y+90);currentSvg=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${$('transparent').checked?'':`<rect width="100%" height="100%" fill="#faf7ed"/>`}${body}</svg>`;$('paper').innerHTML=currentSvg;
 $('status').innerHTML=(unsupported.size?'<b>Unsupported:</b> '+esc([...unsupported].join(' '))+'<br>':'')+(provisional.size?'<span style="color:#9a651e">Reconstructed or composed: '+esc([...provisional].sort().join(' '))+'</span>':'All visible characters in this note use traced forms.');
}
function save(blob,name){const u=URL.createObjectURL(blob),a=document.createElement('a');a.href=u;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(u),2000)}
$('svg').onclick=()=>save(new Blob([currentSvg],{type:'image/svg+xml'}),'conan-doyle-note.svg');
$('png').onclick=()=>{const b=new Blob([currentSvg],{type:'image/svg+xml'}),u=URL.createObjectURL(b),im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width*2;c.height=im.height*2;const ctx=c.getContext('2d');ctx.drawImage(im,0,0,c.width,c.height);c.toBlob(v=>save(v,'conan-doyle-note.png'));URL.revokeObjectURL(u)};im.onerror=()=>{$('status').textContent='PNG export failed. Please save SVG instead.';URL.revokeObjectURL(u)};im.src=u};
$('alphabet').onclick=()=>{$('text').value='ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789\n.,;:!? \' \" - / ( ) [ ] & @ # £ €\nŴ ŵ Ŷ ŷ â ê î ô û';$('text').dispatchEvent(new Event('input'))};$('vary').onclick=()=>{seed++;render()};
$('words').onclick=()=>{$('text').value='ant  elementary  minimum\nwriting  Arthur  Watson\nletter  little  running  morning\nWith kind regards,\n“Holmes?” £13 & £25.';$('text').dispatchEvent(new Event('input'))};
const fields=['text','source','capitalA','mode','spacing','size','transparent'];
try{let saved=JSON.parse(localStorage.getItem('doyle-desk-v3')||'null');if(saved)for(let id of fields){if(saved[id]!==undefined){if(id==='transparent')$(id).checked=saved[id];else if($(id).tagName!=='SELECT'||[...$(id).options].some(o=>o.value===saved[id]))$(id).value=saved[id]}}}catch(e){}
for(let id of fields)$(id).addEventListener('input',()=>{render();try{let values={};for(let name of fields)values[name]=name==='transparent'?$(name).checked:$(name).value;localStorage.setItem('doyle-desk-v3',JSON.stringify(values))}catch(e){}});render();
</script></html>'''
banks={'clean':json.loads((P/'working/clean-proof/complete-glyphs.json').read_text())}
legacy=P/'archive/v0.2/glyphs.json'
if legacy.exists():banks['legacy']=json.loads(legacy.read_text())
else:
 html=html.replace('<option value="legacy">v0.2 · previous mixed draft</option>','')
 html=html.replace('The previous v0.6 layout and v0.2 draft remain selectable for comparison.','The previous spacing layout remains selectable for comparison.')
html=html.replace('LAYOUTCODE',(P/'working/layout.js').read_text()).replace('LAYOUTDATA',(P/'working/layout-model.json').read_text()).replace('FONTDATA',base64.b64encode((O/'conan-doyle-letters-study.ttf').read_bytes()).decode()).replace('GLYPHDATA',json.dumps(banks,separators=(',',':')))
(O/'handwriting-desk.html').write_text(html)
print('Saved self-contained renderer')
