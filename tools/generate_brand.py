"""Render original DRAG portfolio motion graphics. Python 3.10+; pip install Pillow.

Run: python tools/generate_brand.py --root /path/to/parent-of-repositories
Fonts: set BRAND_FONT / BRAND_MONO to local TTF paths to override defaults.
No network, tracking pixels, external image services, or runtime dependencies.
"""
from pathlib import Path
import argparse, math, os
from PIL import Image, ImageDraw, ImageFont

W, H, FRAMES = 1200, 440, 40
BG = (11, 16, 20)
WHITE = (238, 242, 240)
MUTED = (150, 168, 171)
SPECS = {
    'ansh2807': ('ANSH KALRA', 'DRAG / INDEPENDENT BUILDER', 'Security in mind. Craft in every detail.', 'CYBERSECURITY  /  SOFTWARE  /  DESIGN', '#70e4b4', 'identity', '00'),
    'keyforge': ('KEYFORGE', 'AUTHENTICATION / LICENSING', 'Your software. Your keys.', 'ED25519  /  DEVICE CONTROL  /  SDKs', '#edc779', 'vault', '01'),
    'pdf-studio': ('PDF STUDIO', 'DOCUMENTS / SELF-HOSTED', 'A better home for your documents.', 'EDIT  /  OCR  /  CONVERT  /  REDACT', '#ee9a7f', 'paper', '02'),
    'scribe-studio': ('SCRIBE', 'TRANSCRIPTION / MEDIA STUDIO', 'Every voice. Every frame.', 'INDIC LANGUAGES  /  AUDIO  /  VIDEO', '#77d8ea', 'wave', '03'),
    'omniscope': ('OMNISCOPE', 'MARKETING / INTELLIGENCE', 'Follow the evidence.', 'CREATORS  /  WEBSITES  /  REPORTS', '#87dca7', 'radar', '04'),
    'creative-ui': ('CREATIVE UI', 'INTERFACES / MOTION / CRAFT', 'Make the interface worth remembering.', 'DESIGN SYSTEMS  /  MOTION  /  VERIFICATION', '#b2b0ff', 'mesh', '05'),
    'CMS-SYSTEM-': ('CMS SYSTEM', 'PROJECT PREVIEW / COMING SOON', 'A new workspace is taking shape.', 'SOURCE RELEASE PENDING', '#a4becf', 'blocks', '06'),
}

def font(size, mono=False):
    env = os.getenv('BRAND_MONO' if mono else 'BRAND_FONT')
    choices = [env] if env else []
    choices += (['C:/Windows/Fonts/consola.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'] if mono else ['C:/Windows/Fonts/bahnschrift.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
    for path in choices:
        if path and Path(path).is_file(): return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)

def mix(a,b,t): return tuple(round(x+(y-x)*t) for x,y in zip(a,b))
def rgb(s): return tuple(bytes.fromhex(s[1:]))
def line(d,points,c,w=1): d.line(points,fill=c,width=w,joint='curve')

def art(d, kind, c, phase):
    cx,cy=951,209
    dim=mix(BG,c,.22); medium=mix(BG,c,.53)
    # Instrument field. The typography stays completely still during the loop.
    for x in range(744,1160,26):
        for y in range(56,366,26): d.point((x,y), fill=dim)
    d.line((727,62,727,350),fill=mix(BG,c,.15))
    if kind in ('vault','identity'):
        for j,r in enumerate((161,133,104)):
            theta=phase*.25*(1 if j%2 else -1)+j*.25
            pts=[(cx+math.cos(theta+k*math.pi/2)*r,cy+math.sin(theta+k*math.pi/2)*r) for k in range(5)]
            line(d,pts,dim if j!=1 else medium,2)
        if kind=='vault':
            d.ellipse((cx-42,cy-62,cx+42,cy+22),outline=c,width=5)
            d.ellipse((cx-22,cy-42,cx+22,cy+2),outline=medium,width=2)
            line(d,[(cx,cy+21),(cx,cy+83),(cx+32,cy+83)],c,6)
            line(d,[(cx+20,cy+64),(cx+20,cy+83)],c,5)
        else:
            pts=[(cx-52,cy-66),(cx+17,cy-66),(cx+69,cy-16),(cx+44,cy+61),(cx-79,cy+61),(cx-51,cy-31),(cx-14,cy-31),(cx-33,cy+23),(cx+14,cy+23),(cx+28,cy-9),(cx+6,cy-30),(cx-19,cy-30)]
            d.polygon(pts,fill=c)
        for a in (phase,phase+math.pi):
            x,y=cx+161*math.cos(a),cy+161*math.sin(a)
            d.ellipse((x-4,y-4,x+4,y+4),fill=c)
    elif kind=='paper':
        for j in range(3):
            x=827+j*27; y=104-j*23+7*math.sin(phase+j*.5)
            d.rounded_rectangle((x,y,x+195,y+214),radius=5,fill=BG,outline=medium if j<2 else c,width=2)
            for k,l in enumerate((119,140,103,140,73)):
                d.line((x+26,y+44+k*24,x+26+l,y+44+k*24),fill=dim if j<2 else medium,width=3)
            if j==2:
                sy=y+45+(math.sin(phase)+1)*66
                d.line((x+15,sy,x+180,sy),fill=c,width=2)
                d.rectangle((x+25,y+167,x+99,y+187),fill=c)
    elif kind=='wave':
        for j in range(3):
            pts=[]
            for x in range(769,1140,2):
                u=(x-769)/370
                env=math.sin(math.pi*u)**1.5
                y=cy+env*(49*math.sin(u*math.pi*8-phase+j*.7)+22*math.sin(u*math.pi*17+phase))*(1-j*.23)
                pts.append((x,y))
            line(d,pts,(c,medium,dim)[j],2)
        for y in (106,308): d.line((783,y,1129,y),fill=dim)
        for x in range(783,1130,23): d.line((x,305,x,313),fill=medium)
        d.text((797,84),'VOICE  /  SIGNAL  /  TIMELINE',font=font(14,True),fill=medium)
    elif kind=='radar':
        for r in (53,101,151): d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=dim,width=1)
        for k in range(12):
            a=k*math.pi/6
            line(d,[(cx+139*math.cos(a),cy+139*math.sin(a)),(cx+151*math.cos(a),cy+151*math.sin(a))],medium)
        nodes=[(-84,-73),(54,-40),(-38,79),(107,46),(16,-119)]
        for i,(x,y) in enumerate(nodes):
            x+=cx;y+=cy
            line(d,[(cx,cy),(x,y)],medium)
            r=5+2*math.sin(phase+i)
            d.ellipse((x-r,y-r,x+r,y+r),fill=c)
            d.ellipse((x-12,y-12,x+12,y+12),outline=dim)
        d.arc((cx-151,cy-151,cx+151,cy+151),math.degrees(phase),math.degrees(phase)+63,fill=c,width=3)
        d.ellipse((cx-10,cy-10,cx+10,cy+10),fill=c)
    elif kind=='mesh':
        for j in range(19):
            pts=[]
            for i in range(81):
                u=i/80; v=j/18
                x=778+343*u
                y=94+220*v+43*math.sin(u*math.pi*2+phase)*math.sin(v*math.pi)
                pts.append((x,y))
            line(d,pts,mix(dim,c,.25+.65*j/18),1)
        for j in range(17):
            u=j/16; pts=[]
            for i in range(61):
                v=i/60; pts.append((778+343*u,94+220*v+43*math.sin(u*math.pi*2+phase)*math.sin(v*math.pi)))
            line(d,pts,medium,1)
    else:
        for j in range(3):
            x=821+j*32; y=105+j*47+5*math.sin(phase+j)
            pts=[(x,y),(x+179,y),(x+207,y+25),(x+28,y+25),(x,y)]
            d.polygon(pts,fill=BG); line(d,pts,c if j==0 else medium,2)
            line(d,[(x,y),(x,y+18),(x+28,y+43),(x+207,y+43),(x+207,y+25)],dim,2)
        d.text((830,308),'IN DEVELOPMENT',font=font(17,True),fill=c)

def render(spec,t):
    title,kicker,tagline,stack,color,kind,index=spec
    c=rgb(color)
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rectangle((0,0,7,H),fill=c)
    d.text((48,36),'D /',font=font(22),fill=c)
    d.text((104,40),'ANSH KALRA  /  DRAG',font=font(14,True),fill=MUTED)
    d.text((1065,40),'VOL. '+index,font=font(14,True),fill=MUTED)
    d.line((48,79,1152,79),fill=(35,45,49))
    d.text((48,111),kicker,font=font(15,True),fill=c)
    size=87
    while d.textlength(title,font=font(size))>651: size-=1
    d.text((44,154),title,font=font(size),fill=WHITE)
    d.text((48,269),tagline,font=font(25),fill=MUTED)
    d.text((48,320),stack,font=font(14,True),fill=c)
    art(d,kind,c,t*math.tau)
    d.line((48,386,1152,386),fill=(35,45,49))
    d.text((48,406),'BUILT WITH INTENT.',font=font(12,True),fill=MUTED)
    d.text((963,406),'GITHUB / ANSH2807',font=font(12,True),fill=MUTED)
    return im

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);parser.add_argument('--only',choices=SPECS)
    args=parser.parse_args()
    for repo,spec in SPECS.items():
        if args.only and repo!=args.only: continue
        dest=args.root/repo/'assets'/'brand';dest.mkdir(parents=True,exist_ok=True)
        ims=[render(spec,i/FRAMES) for i in range(FRAMES)]
        ims[0].save(dest/'cover.png',optimize=True)
        # One shared palette eliminates frame-to-frame color shimmer.
        palette=ims[0].quantize(colors=96)
        frames=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in ims]
        frames[0].save(dest/'cover.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=1)
        print(repo,(dest/'cover.gif').stat().st_size,flush=True)

if __name__=='__main__': main()
