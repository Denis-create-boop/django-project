from PIL import Image, ImageDraw
import math

def render_product(category, index, angle):
    # Original schematic product illustrations, not manufacturer photographs.
    im = Image.new('RGB', (960, 660), '#171e1b')
    d = ImageDraw.Draw(im)
    for y in range(660):
        t = y / 660
        d.line((0,y,960,y), fill=(int(35-17*t),int(46-24*t),int(40-20*t)))
    d.ellipse((190,510,770,595), fill='#101512')
    palette = ['#aeb9b9','#65746f','#c6c8c4','#3c4643','#89988e']
    metal = palette[index % len(palette)]
    accent = ['#89d75d','#e8cd61','#64a6a2','#a6c2a0','#d8dbe0'][index%5]
    dx = 28 if angle else 0
    def rect(box, color, radius=18, outline=None, width=3):
        x,y,X,Y=box
        d.rounded_rectangle((x+dx,y,X+dx,Y), radius=radius, fill=color, outline=outline, width=width)
    def ellipse(box, color, outline=None, width=3):
        x,y,X,Y=box
        d.ellipse((x+dx,y,X+dx,Y), fill=color, outline=outline, width=width)
    def line(points, color, width=5):
        d.line([(x+dx,y) for x,y in points], fill=color, width=width)
    if category == 'tv':
        rect((150,100,810,475),'#0a0e0d',18,metal,5)
        rect((165,115,795,460),'#263e37',8)
        for k in range(7):
            d.polygon([(165+dx,460),(400+k*45+dx,115),(510+k*35+dx,115),(270+k*75+dx,460)],fill=['#31574a','#466e55','#6a9765'][k%3])
        line([(300,476),(255,535)],metal,12);line([(660,476),(705,535)],metal,12)
    elif category == 'phone':
        rect((335,65,625,570),metal,42,'#d3dbd5',3)
        rect((347,79,613,556),'#172b27',33)
        if angle:
            rect((360,95,465,220),'#26302c',20)
            for x,y in [(386,124),(436,124),(386,178)]:ellipse((x-18,y-18,x+18,y+18),'#090e0c',metal,4)
        else:
            for k in range(6):ellipse((365+k*16,190+k*20,590-k*9,470-k*12),['#395c4a','#537b5a','#83ab6e'][k%3])
            ellipse((473,92,487,106),'#0b100e')
    elif category == 'computer':
        rect((320,90,635,550),metal,20,'#aab6ac')
        rect((340,110,615,530),'#202a26',12)
        for y in (195,320,445):
            ellipse((401,y-50,501,y+50),'#111a16',accent,6)
            ellipse((429,y-22,473,y+22),'#42554a')
        rect((550,130,590,140),accent,4)
    elif category == 'fridge':
        rect((330,65,630,560),metal,19,'#d4d9d5')
        rect((345,80,615,365),metal,10,'#707b76')
        rect((345,375,615,545),metal,10,'#707b76')
        rect((365,195,378,320),'#e2e6e2',5);rect((365,405,378,495),'#e2e6e2',5)
    elif category == 'wash':
        rect((280,100,680,555),metal,22,'#d0d8d2')
        rect((300,120,660,195),'#28312d',10)
        ellipse((575,132,620,177),metal)
        rect((320,142,430,167),accent,5)
        ellipse((348,225,612,489),'#1c2521','#d2d9d5',12)
        ellipse((375,252,585,462),'#40594f','#667d70',5)
        ellipse((410,285,550,425),'#253b33')
    elif category == 'conditioner':
        rect((145,205,815,395),metal,35,'#d5ddd5')
        rect((175,320,785,377),'#1d2521',10)
        for y in (332,344,356):line([(195,y),(765,y)],'#85978a',4)
        rect((710,245,767,267),accent,4)
        for k in range(4):line([(400+k*32,402),(375+k*48,510)],'#608573',3)
    elif category == 'muse':
        for x in (250,510):
            rect((x,105,x+200,545),metal,25,'#9aa69e')
            rect((x+12,120,x+188,525),'#202923',16)
            for y,r in ((205,47),(370,76)):
                ellipse((x+100-r,y-r,x+100+r,y+r),'#101713',accent,4)
                ellipse((x+80,y-20,x+120,y+20),'#53665a')
    elif category == 'utug':
        d.polygon([(170+dx,485),(420+dx,240),(740+dx,470),(745+dx,500),(180+dx,500)],fill=metal)
        rect((320,330,705,472),'#41584b',35)
        rect((390,185,650,355),accent,65)
        rect((430,225,610,325),'#25382e',40)
        rect((170,480,745,515),'#c8d2cc',12)
    return im
