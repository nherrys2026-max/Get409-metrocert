import sys, subprocess, os
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
S=os.path.dirname(os.path.abspath(__file__)); V=S+'/v'; IMG='docs/s7/images/'
os.makedirs(V, exist_ok=True)
exec(open(S+'/compose.py').read().split('# 1a')[0])  # bg, brand, fonts
FPS=30; DUR=65.0; T=0.3
AX,AY,AW,AH=40,250,1000,1230   # zone de contenu
def frame_bg(label):
    im=bg(); brand(im,label); return im
def content(src,box,h=None,w=None):
    c=Image.open(src).convert('RGB').crop(box)
    sc=(h/c.height) if h else (w/c.width)
    return c.resize((round(c.width*sc),round(c.height*sc)),Image.LANCZOS)
scenes=[ # (start, end, kind, data)
 (0,7,'card',V+'/s1.png'),(7,15,'card',V+'/s2.png'),
 (15,19.3,'pan',('Le site',content(IMG+'s01_accueil.jpg',(300,40,1600,560),h=760))),
 (19.3,23.5,'pan',('Vérifier un résultat',content(IMG+'s02_tableau_simple.jpg',(390,120,1520,800),h=AH))),
 (23.5,30,'pan',('Zone de garde w = U',content(IMG+'s03_tableau_garde.jpg',(390,120,1520,800),h=AH))),
 (30,35.5,'vpan',("L'agent relit",content(IMG+'s05_certificat_rapport.jpg',(410,150,1150,1080),w=AW))),
 (35.5,40.5,'vpan',('Verdict de l\'agent',content(IMG+'s04b_rapport_surligne.jpg',(420,330,1160,1000),w=AW))),
 (40.5,45.5,'pan',('Étalon échu repéré',content(IMG+'s04b_rapport_surligne.jpg',(420,560,1480,960),h=900))),
 (45.5,53.6,'pan',('Architecture',content('docs/s5/architecture-v2-1.png',(0,0,1800,1130),h=AH))),
 (53.6,65,'card',V+'/s11.png'),
]
cache={}
def render(i,t):
    a,b,kind,data=scenes[i]; u=min(max((t-a)/(b-a),0),1)
    if kind=='card':
        if i not in cache: cache[i]=Image.open(data).convert('RGB')
        return cache[i]
    label,c=data
    if i not in cache: cache[i]=frame_bg(label)
    im=cache[i].copy()
    e=u*u*(3-2*u)  # ease
    if kind=='pan':
        if c.width>AW: x0=round((c.width-AW)*e); crop=c.crop((x0,0,x0+AW,c.height))
        else: crop=c
    elif kind=='vpan':
        hh=min(c.height,AH); y0=round((c.height-hh)*e); crop=c.crop((0,y0,c.width,y0+hh))
    else: crop=c if c.height<=AH else c.crop((0,0,c.width,AH))
    x=(1080-crop.width)//2; y=AY+(AH-crop.height)//2
    ImageDraw.Draw(im).rectangle([x-3,y-3,x+crop.width+2,y+crop.height+2],fill=(255,255,255))
    im.paste(crop,(x,y)); return im
ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r',str(FPS),'-i','-',
   '-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p',S+'/video_muet.mp4'],stdin=subprocess.PIPE)
N=int(DUR*FPS)
for n in range(N):
    t=n/FPS
    i=max(k for k,s in enumerate(scenes) if s[0]<=t)
    im=render(i,t)
    if i>0 and t-scenes[i][0]<T:   # fondu enchaîné
        al=(t-scenes[i][0])/T; im=Image.blend(render(i-1,t),im,al)
    if t>DUR-0.8: im=Image.blend(im,Image.new('RGB',im.size),(t-(DUR-0.8))/0.8)
    ff.stdin.write(im.tobytes())
ff.stdin.close(); ff.wait(); print('frames',N)
