"""Use one reviewed spacing model for the installable font and offline renderer."""
from pathlib import Path
import json

def feature_text(font,root=None):
 P=Path(root) if root else Path(__file__).resolve().parents[1]
 text='feature ss01 { sub uni0041 by A.body; } ss01;\n'
 path=P/'working/layout-model.json'
 model=json.loads(path.read_text());cmap=font.getBestCmap();groups={}
 for ch,group in model['groups'].items():
  name=cmap.get(ord(ch)) if len(ch)==1 else ch
  if name in font.getGlyphOrder():groups.setdefault(group,[]).append(name)
 ids={group:'@spacing'+str(i) for i,group in enumerate(groups)}
 for group,names in groups.items():text+=ids[group]+' = ['+' '.join(dict.fromkeys(names))+'];\n'
 text+='feature kern {\n'
 for left,pairs in model['kern'].items():
  for right,value in pairs.items():
   if left in ids and right in ids:text+=f' pos {ids[left]} {ids[right]} {value};\n'
 return text+'} kern;\n'

def apply_features(font,root=None):
 from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
 P=Path(root) if root else Path(__file__).resolve().parents[1]
 path=P/'working/layout-model.json'
 font['hmtx']['space']=(json.loads(path.read_text())['word_space'],0)
 addOpenTypeFeaturesFromString(font,feature_text(font,P))
