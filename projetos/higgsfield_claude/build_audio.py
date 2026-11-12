"""Monta voz com silencios nas insercoes, trilha, picos e SFX para uma lista de insercoes."""
import json, sys, subprocess, random
S='/tmp/claude-0/-home-user-Wakizashi/a18d254c-fe44-5423-a2e6-562d716691fb/scratchpad'; P='/home/user/Wakizashi/projetos/higgsfield_claude'
INSL=json.loads(sys.argv[1]); tag=sys.argv[2]; CD=8*60/152; N=len(INSL); DUR=25.5+N*CD; FIM=23.25+N*CD
def toReal(m): return m+sum(CD for a,_ in INSL if m>=a)
# voz
parts=[];last=0;fc='';
for i,(a,_) in enumerate(INSL):
    fc+=f'[0]atrim={last}:{a},asetpts=PTS-STARTPTS[v{i}];aevalsrc=0|0:d={CD}:s=48000[z{i}];'; parts+= [f'[v{i}]',f'[z{i}]']; last=a
fc+=f'[0]atrim={last},asetpts=PTS-STARTPTS[vl];'; parts.append('[vl]')
fc+=''.join(parts)+f'concat=n={len(parts)}:v=0:a=1'
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{S}/entrega_v02/stems/voz.wav','-filter_complex',fc,'-c:a','pcm_f32le',f'{S}/aud/voz_{tag}.wav'],check=True)
subprocess.run([f'{S}/venv/bin/python','-I',f'{S}/trilha_cinematica.py',f'{S}/aud/musica.mp3','29','0.88',str(FIM),f'{S}/aud/trilha_{tag}.wav',f'{S}/sfx'],check=True,capture_output=True)
# sfx
E=json.load(open(f'{P}/sfx_16x9.json'))
for e in E: e['t']=round(toReal(e['t']),3)
def ev(n,t,db,az=(0,0),el=(0,0),rev=.25,al='pico'): E.append({"nome":n,"t":round(t,3),"db":db,"az":list(az),"el":list(el),"rev":rev,"alinhar":al})
r=random.Random(5)
for i,(a,_) in enumerate(INSL):
    ra=toReal(a)-CD; side=-1 if i%2==0 else 1
    ev("kt_long",ra-.05,-7,(side*120,0),(.4,0)); ev("pv_impact",ra+.02,-4,rev=.45); ev("kt_boom2",ra+.02,-7)
    ev("kt_long2",ra+CD/2-.06,-7,(-side*90,side*90)); ev("kt_crack",ra+CD/2-.03,-6,rev=.4); ev("pv_impact",ra+CD/2,-4,rev=.5); ev("kt_flash",ra+CD/2,-8)
    t=ra+.25
    while t<ra+1.1: ev(f"kt_key{r.randint(1,5)}",t,-14+r.uniform(-2,1),(10,10),rev=.05,al='inicio'); t+=.05+r.random()*.05
    ev("kt_wh2",ra+CD-.12,-9,(0,-side*90))
json.dump(E,open(f'{P}/sfx_{tag}.json','w'),indent=0)
subprocess.run([f'{S}/venv/bin/python','-I',f'{P}/mix_3d.py',f'{S}/aud/voz_{tag}.wav',f'{S}/aud/trilha_{tag}.wav',f'{S}/sfx',f'{P}/sfx_{tag}.json',f'{S}/entrega_{tag}','--dur',str(DUR),'--fim',str(FIM)],check=True,capture_output=True)
# picos da musica para o fundo
import librosa, numpy as np
y,sr=librosa.load(f'{S}/aud/trilha_{tag}.wav',sr=48000,mono=True); n=int(DUR*30)
Sx=np.abs(librosa.stft(y,n_fft=4096,hop_length=1600)); f=librosa.fft_frequencies(sr=sr,n_fft=4096)
def nz(a):
    a=a[:n]; a=np.pad(a,(0,max(0,n-len(a)))); a=a/np.percentile(a,98); a=np.clip(a,0,1.2); o=np.zeros_like(a); v=0
    for i,x in enumerate(a): v = x if x>v else v*0.86+x*0.14; o[i]=v
    return o
L=nz(Sx[f<150].mean(0)); Hh=nz(Sx[f>2000].mean(0)); fl=np.cumsum(0.4+1.6*L)/30
open(f'{S}/k16/peaks.js','w').write('const PK_L=%s,PK_H=%s,PK_F=%s;'%tuple(json.dumps([round(float(x),3) for x in a]) for a in (L,Hh,fl)))
print('ok', tag, round(DUR,3), n, 'quadros')
