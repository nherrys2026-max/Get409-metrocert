from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
OUT=os.path.dirname(os.path.abspath(__file__))+'/v'; os.makedirs(OUT, exist_ok=True)  # lancer depuis la racine du dépôt
IMG='docs/s7/images/'; W,H=1080,1920
F='/usr/share/fonts/opentype/inter/'
def font(w,s): return ImageFont.truetype(F+{'b':'Inter-Bold.otf','sb':'Inter-SemiBold.otf','r':'Inter-Regular.otf','xb':'Inter-ExtraBold.otf'}[w],s)
ORANGE=(245,166,35); WHITE=(255,255,255); PALE=(200,212,240)
def bg():
    im=Image.new('RGB',(W,H)); d=ImageDraw.Draw(im)
    a,b=(11,31,92),(36,70,158)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3)))
    return im
def ruler(d,x,y,s=1.0,col=ORANGE):
    d.rounded_rectangle([x,y,x+int(64*s),y+int(26*s)],radius=4,outline=col,width=max(2,int(4*s)))
    for i in range(1,6):
        xx=x+int(i*64*s/6); d.line([(xx,y),(xx,y+int((14 if i%2 else 9)*s))],fill=col,width=max(2,int(3*s)))
def brand(im,label=None):
    d=ImageDraw.Draw(im); ruler(d,80,128); d.text((162,112),'MetroCert',font=font('b',50),fill=WHITE)
    if label:
        f=font('sb',30); w=d.textlength(label,font=f)
        d.rounded_rectangle([W-80-w-40,112,W-80,170],radius=29,outline=ORANGE,width=3); d.text((W-80-w-20,121),label,font=f,fill=ORANGE)
    f=font('r',26); t='GET 409 · Prototype pédagogique — données fictives'
    d.text(((W-d.textlength(t,font=f))/2,1850),t,font=f,fill=PALE)
def wrap(d,text,f,maxw):
    out=[];line=''
    for w in text.split():
        t=(line+' '+w).strip()
        if d.textlength(t,font=f)<=maxw: line=t
        else: out.append(line); line=w
    out.append(line); return out
def shot(src,box,name,label,y0=300,maxh=1180,hl=None):
    im=bg(); brand(im,label)
    s=Image.open(src).convert('RGB').crop(box)
    sc=min((W-80)/s.width, maxh/s.height); s=s.resize((int(s.width*sc),int(s.height*sc)),Image.LANCZOS)
    x=(W-s.width)//2; y=y0+(maxh-s.height)//2
    sh=Image.new('RGBA',(s.width+40,s.height+40),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([20,20,s.width+20,s.height+20],fill=(0,0,0,120))
    im.paste(sh.filter(ImageFilter.GaussianBlur(14)),(x-20,y-6),sh.filter(ImageFilter.GaussianBlur(14)))
    im.paste(s,(x,y)); d=ImageDraw.Draw(im); d.rectangle([x-1,y-1,x+s.width,y+s.height],outline=(255,255,255),width=2)
    im.save(f'{OUT}/{name}.png')
# 1a
im=bg(); brand(im); d=ImageDraw.Draw(im)
f=font('sb',34); t='ISO/IEC 17025:2017 §7.8'; w=d.textlength(t,font=f)
d.rounded_rectangle([80,430,80+w+48,494],radius=32,outline=ORANGE,width=3); d.text((104,440),t,font=f,fill=ORANGE)
d.text((70,520),'22',font=font('xb',380),fill=ORANGE)
y=960
for l in ['mentions obligatoires','sur un certificat',"d'étalonnage"]: d.text((80,y),l,font=font('b',84),fill=WHITE); y+=104
d.text((80,1300),'Exigences MC-01 à MC-22',font=font('r',34),fill=PALE)
im.save(OUT+'/s1.png')
# 1b
im=bg(); brand(im); d=ImageDraw.Draw(im); y=520
for l in ['Relus à la main,','souvent le soir.']: d.text((80,y),l,font=font('xb',104),fill=WHITE); y+=130
y=900
for t in ['Mention oubliée','Étalon échu',"Écart d'audit"]:
    f=font('sb',46); w=d.textlength(t,font=f)
    d.rounded_rectangle([80,y,80+w+110,y+92],radius=46,outline=WHITE,width=3)
    d.ellipse([112,y+36,132,y+56],fill=(239,83,80)); d.text((152,y+18),t,font=f,fill=WHITE); y+=126
im.save(OUT+'/s2.png')
# final
im=bg(); brand(im); d=ImageDraw.Draw(im)
ruler(d,80,400,2.2); d.text((80,480),'MetroCert',font=font('xb',150),fill=WHITE); y=690
for l in ['La relecture de vos certificats',"d'étalonnage, en un clic."]: d.text((80,y),l,font=font('sb',56),fill=WHITE); y+=72
qr=Image.open(IMG+'carte_finale.png').convert('RGB').crop((1300,310,1766,772)).resize((560,554),Image.LANCZOS)
im.paste(qr,((W-560)//2,930)); d=ImageDraw.Draw(im)
f=font('b',44); t='pixel-perfect-capture-0446.lovable.app'; d.text(((W-d.textlength(t,font=f))/2,1530),t,font=f,fill=ORANGE)
f=font('r',34)
for i,t in enumerate(['Livrer dans la journée','Passer l\'audit sans écart lié aux certificats']): d.text(((W-d.textlength(t,font=f))/2,1610+i*48),t,font=f,fill=PALE)
im.save(OUT+'/s11.png')
print('ok')
