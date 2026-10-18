"""Build the current font from reviewed vectors without downloading reference scans."""
import argparse,json
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from font_features import apply_features
P=Path(__file__).resolve().parents[1]
def build(destination):
 vectors=json.loads((P/'working/clean-proof/complete-glyphs.json').read_text())
 info=json.loads((P/'working/font-metrics.json').read_text())
 glyphs={};metrics={};cmap={32:'space',160:'space'}
 pen=TTGlyphPen(None);pen.moveTo((70,0));pen.lineTo((430,0));pen.lineTo((430,550));pen.lineTo((70,550));pen.closePath()
 glyphs['.notdef']=pen.glyph();metrics['.notdef']=(500,70)
 glyphs['space']=TTGlyphPen(None).glyph();metrics['space']=(250,0)
 for ch,rec in vectors.items():
  name='uni%04X'%ord(ch) if len(ch)==1 else ch;pen=TTGlyphPen(None)
  for path in rec['paths']:
   if len(path)<3:continue
   pts=[tuple(round(v) for v in pt) for pt in path]
   mids=[tuple(round((pts[i][d]+pts[(i+1)%len(pts)][d])/2) for d in (0,1)) for i in range(len(pts))]
   pen.moveTo(mids[-1])
   for pt,end in zip(pts,mids):pen.qCurveTo(pt,end)
   pen.closePath()
  glyphs[name]=pen.glyph();metrics[name]=(rec['advance'],info['left_bearings'][ch])
  if len(ch)==1:cmap[ord(ch)]=name
 fb=FontBuilder(1000,isTTF=True);fb.setupGlyphOrder(list(glyphs));fb.setupCharacterMap(cmap);fb.setupGlyf(glyphs);fb.setupHorizontalMetrics(metrics)
 fb.setupHorizontalHeader(**info['horizontal_header']);fb.setupNameTable(info['names']);fb.setupOS2(**info['os2']);fb.setupPost();fb.setupMaxp()
 apply_features(fb.font,P)
 destination.parent.mkdir(parents=True,exist_ok=True);fb.save(destination);print('Built',destination)
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=P/'outputs/conan-doyle-letters-study.ttf');args=ap.parse_args();build(args.output)
