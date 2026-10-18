const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const Layout=require('./layout.js'),model=require('./layout-model.json'),bank=require('./clean-proof/complete-glyphs.json');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
fs.mkdirSync(path.join(__dirname,'spacing'),{recursive:true});
const options={optical:true,joins:true,capitalA:'signature'};
for(const word of ['ant','elementary','minimum','writing','Arthur','Watson','letter','little','running','morning','tata','thin','Café']){
 const run=Layout.shapeRun([...word],bank,options,model);assert(run.records.every(r=>Number.isFinite(r.x)&&r.x>=0));
 for(const b of run.bridges){assert(!'tfgjqz'.includes(b.left));assert(b.end[0]>b.start[0]);assert(Math.abs(b.end[1]-b.start[1])<=130)}
}
const long=Layout.shapeRuns([...'minimum'.repeat(15)],bank,options,model,3500);assert(long.length>1);assert(long.every(r=>r.width<=3500));assert(long.every(r=>r.records[0].x===0));assert.equal(long.flatMap(r=>r.records.map(g=>g.ch)).join(''),'minimum'.repeat(15));
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_EXECUTABLE||undefined});const page=await browser.newPage({viewport:{width:1350,height:1050}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+path.resolve(__dirname,'../outputs/handwriting-desk.html'));await page.locator('#mode').selectOption('note');await page.locator('#size').fill('52');
 const text='elementary\nminimum\nwriting Arthur Watson\nant letter little\nrunning morning\nWith kind regards,\n“Holmes?” £13 & £25.';await page.locator('#text').fill(text);
 for(const value of ['previous','optical']){await page.locator('#spacing').selectOption(value);let d=page.waitForEvent('download');await page.locator('#png').click();await(await d).saveAs(path.resolve(__dirname,'spacing',value+'.png'))}
 await page.locator('#mode').selectOption('font');await page.locator('#text').fill('elementary');
 const svgAdvance=+(await page.locator('#paper g[data-word]').getAttribute('data-advance'));const run=Layout.shapeRun([...'elementary'],bank,options,model);assert.equal(svgAdvance,run.width);
 // The desktop font's GPOS must agree with the SVG renderer, including accents and ss01.
 await page.evaluate(()=>document.fonts.load('100px Doyle'));
 for(const [word,capitalA] of [['elementary','signature'],['Arthur','signature'],['Arthur','body'],['Café','signature'],["Doyle's",'signature'],['“Holmes?”','signature'],['With kind regards,','signature']]){
  const actual=await page.evaluate(({word,capitalA})=>{const s=document.createElement('span');s.style.cssText='position:absolute;display:inline-block;white-space:pre;font:100px Doyle';s.style.fontFeatureSettings=capitalA==='body'?'"ss01" 1':'normal';s.textContent=word;document.body.append(s);const w=s.getBoundingClientRect().width;s.remove();return w},{word,capitalA});
  const expected=Layout.shapeRun([...word],bank,{...options,capitalA},model).width/10;assert(Math.abs(actual-expected)<.15,`${word}/${capitalA}: font ${actual}, SVG ${expected}`);
 }
 await page.locator('#text').fill('minimum'.repeat(120));const groups=await page.locator('#paper g[data-word]').evaluateAll(ns=>ns.map(n=>({transform:n.getAttribute('transform'),width:+n.dataset.advance})));assert(groups.length>5);assert(groups.every(g=>g.width*0.052<=870));
 await page.locator('#text').fill('ant ant');const one=+(await page.locator('#paper g[data-word]').nth(1).getAttribute('transform')).match(/translate\(([^ ]+)/)[1];await page.locator('#text').fill('ant  ant');const two=+(await page.locator('#paper g[data-word]').nth(1).getAttribute('transform')).match(/translate\(([^ ]+)/)[1];assert(Math.abs(two-one-15.6)<.01);await page.locator('#text').fill('ant\u00a0ant');assert.equal(await page.locator('#paper g[data-word]').count(),1);
 await page.locator('#text').fill('ant\nminimum');const ys=await page.locator('#paper g[data-word]').evaluateAll(ns=>ns.map(n=>n.getAttribute('transform').match(/translate\([^ ]+ ([^)]+)/)[1]));assert(+ys[1]>+ys[0]);
 await page.locator('#text').fill('<script>alert(1)</script>');assert.equal(await page.locator('#paper script').count(),0);
 await page.locator('#spacing').selectOption('previous');await page.reload();assert.equal(await page.locator('#spacing').inputValue(),'previous');await page.locator('#spacing').selectOption('optical');await page.locator('#words').click();assert((await page.locator('#text').inputValue()).includes('minimum'));assert.equal(errors.length,0,errors.join('; '));
 await browser.close();console.log('Spacing passed: shared font/SVG kerning, accents/ss01, bounded joins, wrapping/line breaks, escaping, comparison persistence and word proof.');
})().catch(e=>{console.error(e);process.exit(1)});
