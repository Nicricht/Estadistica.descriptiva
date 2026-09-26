from PIL import Image, ImageDraw
from pathlib import Path

P = Path('presentacion')
A = P / '.generated_assets'
A.mkdir(parents=True, exist_ok=True)
OUT = P / 'Estadistica_Descriptiva_Biobio_FINAL.pptx'

def assets():
    for k in range(6):
        q = A / f'bg{k}.jpg'
        if q.exists():
            continue
        im = Image.new('RGB', (1600, 900), (4, 12, 24))
        d = ImageDraw.Draw(im, 'RGBA')
        for y in range(900):
            col = (4 + int(14*y/900), 12 + int(9*(1-y/900)), 24 + int(18*(1-y/900)))
            d.line((0, y, 1600, y), fill=col)
        for i in range(10):
            y = 85 + i*75
            x = 60 + (k*97 + i*143) % 520
            d.line((x, y, x+270, y, x+340, y+45, x+640, y+45), fill=(40, 215, 255, 45), width=3)
        im.save(q, quality=86, optimize=True)

assets()
