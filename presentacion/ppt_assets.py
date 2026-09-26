from PIL import Image,ImageDraw
from pathlib import Path
import math
P=Path('presentacion'); A=P/'.generated_assets'; A.mkdir(parents=True,exist_ok=True)
OUT=P/'Del_Acero_al_Algoritmo_FINAL_MORPH.pptx'

def assets():
    # 6 changing raster backgrounds
    for k in range(6):
        q=A/f'bg{k}.jpg'
        if q.exists(): continue
        im=Image.new('RGB',(1600,900),(4,12,24)); d=ImageDraw.Draw(im,'RGBA')
        for y in range(900):
            col=(4+int(14*y/900),12+int(9*(1-y/900)),24+int(18*(1-y/900)))
            d.line((0,y,1600,y),fill=col)
        for i in range(10):
            y=85+i*75; x=60+(k*97+i*143)%520
            d.line((x,y,x+270,y,x+340,y+45,x+640,y+45),fill=(40,215,255,45),width=3)
        for i in range(6): d.arc((910+i*90,80+i*85,1510+i*30,500+i*70),190,340,fill=(255,132,32,50),width=4)
        for yy in range(550,900,55): d.line((0,yy,1600,yy),fill=(100,145,175,20),width=1)
        im.save(q,quality=86,optimize=True)
    # independent transparent image elements
    for kind in ['steel','industry','chip','data','price','curve','campus','people']:
        q=A/f'{kind}.png'
        if q.exists(): continue
        im=Image.new('RGBA',(1000,650),(0,0,0,0)); d=ImageDraw.Draw(im,'RGBA')
        if kind=='steel':
            d.rounded_rectangle((45,250,420,310),14,fill=(145,155,165,255),outline=(235,240,245,255),width=4); d.rounded_rectangle((165,110,290,530),14,fill=(105,115,125,255),outline=(225,232,238,255),width=4); d.rounded_rectangle((45,470,420,530),14,fill=(145,155,165,255),outline=(235,240,245,255),width=4); d.line((400,360,550,325,680,385,780,330),fill=(255,132,32,255),width=15); d.line((410,380,550,350,690,405,800,350),fill=(38,218,255,255),width=14); d.rounded_rectangle((770,235,950,420),25,fill=(20,45,68,255),outline=(38,218,255,255),width=8)
        elif kind=='industry':
            d.rectangle((70,230,480,535),fill=(88,100,113,255),outline=(220,230,238,255),width=4); d.polygon([(70,230),(230,130),(390,230)],fill=(120,130,140,255));
            for x in (125,205,285): d.rectangle((x,65,x+48,230),fill=(140,148,155,255),outline=(240,240,240,255),width=3)
            d.line((590,125,590,535),fill=(255,132,32,255),width=22); d.line((570,145,900,145),fill=(255,132,32,255),width=20); d.line((760,145,760,300),fill=(220,230,238,255),width=6); d.rectangle((690,300,840,385),fill=(170,70,38,255),outline=(255,175,70,255),width=4); d.rectangle((460,520,940,610),fill=(25,105,155,235)); d.polygon([(650,530),(860,530),(820,590),(690,590)],fill=(235,242,246,255),outline=(40,190,235,255))
        elif kind=='chip':
            d.rounded_rectangle((320,180,680,500),45,fill=(18,42,64,255),outline=(38,218,255,255),width=10); d.rounded_rectangle((405,260,595,420),25,fill=(42,76,100,255),outline=(120,245,255,255),width=6)
            for i in range(14):
                a=2*math.pi*i/14; x=500+390*math.cos(a); y=340+240*math.sin(a); d.line((500,340,x,y),fill=(38,218,255,150),width=7); d.ellipse((x-13,y-13,x+13,y+13),fill=(80,235,255,255))
        elif kind=='data':
            d.rounded_rectangle((130,60,800,400),32,fill=(35,96,164,245),outline=(95,235,255,255),width=7); d.rectangle((170,125,760,360),fill=(238,247,255,245),outline=(100,220,255,255),width=3)
            for i in range(1,5): d.line((170,125+i*47,760,125+i*47),fill=(90,160,215,180),width=2)
            for i in range(1,6): d.line((170+i*98,125,170+i*98,360),fill=(90,160,215,160),width=2)
            for yy in (470,520,570): d.ellipse((330,yy-25,650,yy+25),fill=(120,150,175,255),outline=(45,220,255,255),width=5); d.rectangle((330,yy,650,yy+35),fill=(105,130,153,255))
        elif kind=='price':
            for i in range(4):
                x=100+i*205; d.rounded_rectangle((x,250-i*45,x+90,550),12,fill=(45,50,58,255),outline=(120,135,150,255),width=3)
                for j in range(3+i*2): d.ellipse((x-20,570-j*30,x+110,600-j*30),fill=(225,160,45,255),outline=(255,220,120,255),width=2)
            d.line((100,520,300,460,500,370,700,265,900,110),fill=(255,190,70,255),width=16); d.polygon([(875,95),(960,90),(940,180)],fill=(255,190,70,255))
        elif kind=='curve':
            vals=[15,25,45,75,120,180,250,320,370,395,360,305,230,160,105,65,36,20]
            for i,v in enumerate(vals):
                x=35+i*51; bh=v; col=(int(35+220*i/17),int(220-90*i/17),int(255-220*i/17),235); d.rounded_rectangle((x,570-bh,x+34,570),7,fill=col,outline=(180,245,255,170),width=2)
            d.line((35+14*51,110,35+14*51,600),fill=(255,145,35,255),width=8)
        elif kind=='campus':
            d.polygon([(125,220),(500,70),(875,220)],fill=(225,230,235,255),outline=(80,210,255,255)); d.rectangle((150,220,850,570),fill=(205,214,222,255),outline=(100,220,255,255),width=5)
            for x in (245,360,565,680): d.rectangle((x,220,x+60,540),fill=(238,241,244,255),outline=(130,140,150,255),width=3)
            d.rectangle((430,340,570,570),fill=(40,75,100,255),outline=(70,220,255,255),width=5)
        else:
            skin=[(238,210,185,255),(188,140,100,255),(100,68,48,255),(225,185,150,255),(135,90,60,255),(205,165,125,255)]; shirts=[(190,190,210,255),(150,110,190,255),(70,110,85,255),(220,215,195,255),(75,110,145,255),(50,55,65,255)]
            for i in range(6):
                x=65+i*150; y=115+(i%2)*25; d.ellipse((x,y,x+65,y+65),fill=skin[i]); d.rounded_rectangle((x-15,y+62,x+80,410),30,fill=shirts[i],outline=(210,225,235,180),width=2); d.rectangle((x,y+400,x+30,595),fill=(70,85,100,255)); d.rectangle((x+42,y+400,x+72,595),fill=(70,85,100,255))
        im.save(q,optimize=True)
assets()
