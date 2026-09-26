from pathlib import Path
import zipfile,tempfile,shutil
from ppt_deck import prs,OUT
import slides_a, slides_b

prs.save(OUT)
# Morph by object, with fade fallback
td=Path(tempfile.mkdtemp()); u=td/'u'; u.mkdir();
with zipfile.ZipFile(OUT,'r') as z:z.extractall(u)
block='<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"><mc:Choice Requires="p159"><p:transition spd="slow" xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" p14:dur="1650"><p159:morph option="byObject"/></p:transition></mc:Choice><mc:Fallback><p:transition spd="med"><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>'
ss=sorted((u/'ppt'/'slides').glob('slide*.xml'),key=lambda p:int(p.stem[5:]));
for f in ss[1:]:
    x=f.read_text(); p=x.rfind('</p:sld>'); f.write_text(x[:p]+block+x[p:])
tmp=OUT.with_suffix('.tmp.pptx')
with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
    for f in u.rglob('*'):
        if f.is_file():z.write(f,f.relative_to(u))
shutil.move(tmp,OUT); shutil.rmtree(td)
print('Generado:',OUT,'slides=',len(prs.slides),'morph=',len(ss)-1)
