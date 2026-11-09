#!/usr/bin/env python3
"""Build gate variants by swapping the gate CSS / HTML / JS blocks of index.html."""
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ROOT, '..', 'index.html')
s = open(BASE).read()

# ---- guards so base JS works without the old gate markup ----
s = s.replace("$('.d-light').insertAdjacentHTML('beforeend',m);", "const dl=$('.d-light'); if(dl) dl.insertAdjacentHTML('beforeend',m);")
s = s.replace("  $('#gateCap').innerHTML=`<defs>", "  if(!$('#gateCap')) return; $('#gateCap').innerHTML=`<defs>")

def blocks(src):
    c0 = src.index('/* ===================== GATE ===================== */')
    c1 = src.index('/* ===================== SECTIONS ===================== */')
    h0 = src.index('<!-- =================== GATE =================== -->')
    h1 = src.index('<canvas id="petals"')
    j0 = src.index('/* ---------- open gate ---------- */')
    j1 = src.index('(document.fonts?document.fonts.ready')
    return c0, c1, h0, h1, j0, j1

COMMON_CSS = r'''
.seal-hit{position:absolute;left:50%;top:50%;width:150px;height:150px;transform:translate(-50%,-50%);border-radius:50%;z-index:9;background:none}
#gate.go .seal-hit{display:none}
.tap{margin-top:18px;background:#fffaf0f0;border:1px solid var(--gold);color:var(--maroon);border-radius:999px;padding:8px 18px;font-family:var(--caps);font-size:12px;letter-spacing:2px;white-space:nowrap;box-shadow:0 6px 14px #0003;animation:bob 1.8s ease-in-out infinite;transition:opacity .3s}
.tap b{font-family:var(--hi);font-weight:600;letter-spacing:0;font-size:13px}
#gate.go .tap{opacity:0}
.bloom{position:absolute;left:50%;top:50%;width:80vmax;height:80vmax;margin:-40vmax 0 0 -40vmax;border-radius:50%;z-index:20;pointer-events:none;
  background:radial-gradient(circle,#fffaf0 0,#fff3d6 28%,#ffe7b866 48%,#fff0 68%);opacity:0;transform:scale(.25);will-change:transform,opacity;transition:transform 1.5s cubic-bezier(.5,0,.3,1),opacity .9s ease}
#gate.zoom .bloom{opacity:1;transform:scale(1.6)}
#gate.fade{opacity:0;pointer-events:none}
.pulse-ring{position:absolute;left:50%;top:50%;width:110px;height:110px;margin:-55px 0 0 -55px;border-radius:50%;border:2px solid #fff9;animation:pulse 2.2s ease-out infinite;pointer-events:none;will-change:transform,opacity}
#gate.go .pulse-ring{display:none}
@keyframes pulse{0%{transform:scale(.8);opacity:1}100%{transform:scale(1.5);opacity:0}}
'''

COMMON_JS = r'''/* ---------- open gate ---------- */
const gate=$('#gate'); let opened=false, musicTried=false;
function tryMusic(){ if(musicTried) return; musicTried=true; playMusic(); }
$$('[data-wdate]').forEach(el=>el.textContent=`${W.day} · ${String(W.mo+1).padStart(2,'0')} · ${W.y}`);
$$('[data-wdatehi]').forEach(el=>el.textContent=`${W.day} ${MON_HI[W.mo]} ${W.y}`);
__INIT__
const STAGES=__STAGES__;
function openGate(){ if(opened) return; opened=true; gate.classList.add('go');
  STAGES.forEach(([c,t])=>setTimeout(()=>{
    if(c==='unlock'){ document.documentElement.classList.remove('locked'); startObservers(); }
    else if(c==='remove'){ gate.remove(); startPetals(); }
    else gate.classList.add(c); },t)); }
gate.addEventListener('pointerdown',openGate);
gate.addEventListener('click',()=>{ openGate(); tryMusic(); });
gate.addEventListener('touchend',()=>{ tryMusic(); },{passive:true});
gate.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ openGate(); tryMusic(); } });
'''

V = {}

# =====================================================================
# A — SHAHI LIFAFA (royal envelope)
# =====================================================================
V['a'] = dict(css=r'''/* ===================== GATE ===================== */
#gate{position:fixed;inset:0;z-index:60;overflow:hidden;display:flex;align-items:center;justify-content:center;will-change:opacity;transition:opacity .9s ease;
  background:radial-gradient(120% 85% at 50% 42%,#97283a 0%,#641624 50%,#36090f 100%)}
#gate::before{content:"";position:absolute;inset:0;opacity:.13;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='70' height='70' viewBox='0 0 70 70'%3E%3Cg fill='none' stroke='%23f3d991' stroke-width='1'%3E%3Cpath d='M35 8c9 9 9 18 0 27-9-9-9-18 0-27zM35 62c9-9 9-18 0-27-9 9-9 18 0 27zM8 35c9-9 18-9 27 0-9 9-18 9-27 0zM62 35c-9-9-18-9-27 0 9 9 18 9 27 0z'/%3E%3Ccircle cx='35' cy='35' r='3'/%3E%3C/g%3E%3C/svg%3E")}
#gate::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(60% 45% at 50% 45%,#ffd9a033,#0000 70%)}
.ga-dust{position:absolute;inset:0;pointer-events:none}
.ga-dust i{position:absolute;bottom:-10px;width:3px;height:3px;border-radius:50%;background:#f6dc8f;box-shadow:0 0 6px #f6dc8f;opacity:0;animation:rise2 linear infinite;will-change:transform,opacity}
@keyframes rise2{0%{transform:translateY(0);opacity:0}15%{opacity:.9}100%{transform:translateY(-100vh);opacity:0}}
.ga-wrap{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center}
.ga-top{font-family:var(--caps);letter-spacing:4px;color:#f3d991;font-size:11.5px;opacity:.9;margin-bottom:2px;transition:opacity .5s}
.ga-top span{font-family:var(--hi);letter-spacing:0;font-size:13px}
.ga-names{font-family:var(--script);font-size:clamp(38px,11vw,50px);line-height:1.2;margin-bottom:16px;padding:0 .2em;transition:opacity .5s}
#gate.slide .ga-top,#gate.slide .ga-names{opacity:0}
.env{position:relative;width:min(78vw,330px);aspect-ratio:1/1.3;perspective:1100px}
.env-back{position:absolute;inset:0;border-radius:8px;background:linear-gradient(#e9d8b4,#dcc597);box-shadow:0 30px 50px #0009,0 0 0 1px #c9a14a}
.card{position:absolute;left:7%;right:7%;top:5%;height:90%;z-index:2;border-radius:6px;background:radial-gradient(circle at 50% 28%,#fffdf6,#f7e9cf);box-shadow:0 4px 14px #0003;transition:transform 1.1s cubic-bezier(.3,.7,.2,1);will-change:transform}
.card-in{position:absolute;inset:7px;border:1.5px solid #c9a14a;border-radius:4px;display:flex;flex-direction:column;align-items:center;padding-top:9%;text-align:center}
.card-in::after{content:"";position:absolute;inset:4px;border:1px solid #c9a14a77;border-radius:3px}
.c-shri{font-family:var(--hi-d);color:var(--maroon);font-size:12.5px}
.c-hi{font-family:var(--hi-d);color:var(--rani);font-size:20px;margin-top:2px}
.c-name{font-family:var(--script);color:var(--maroon);font-size:clamp(34px,10vw,42px);line-height:1.1}
.c-amp{font-family:var(--script);color:var(--gold-d);font-size:24px;line-height:.9}
.c-date{font-family:var(--caps);font-weight:700;color:var(--gold-d);letter-spacing:3px;font-size:12px;margin-top:8px}
.env-front{position:absolute;inset:0;width:100%;height:100%;z-index:3;pointer-events:none;filter:none}
.flap{position:absolute;left:0;right:0;top:0;height:57%;z-index:4;transform-origin:50% 0;transform-style:preserve-3d;will-change:transform;
  transition:transform .95s cubic-bezier(.45,0,.2,1),z-index 0s .45s}
.flap .f,.flap .b{position:absolute;inset:0;-webkit-backface-visibility:hidden;backface-visibility:hidden;clip-path:polygon(0 0,100% 0,50% 100%)}
.flap .f{background:linear-gradient(175deg,#f6ead0,#e3cda2)}
.flap .f svg{width:100%;height:100%}
.flap .b{transform:rotateX(180deg);background:#7a1f2b url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'%3E%3Cpath d='M14 3c4 5 4 9 0 12-4-3-4-7 0-12zM14 25c4-5 4-9 0-12-4 3-4 7 0 12z' fill='none' stroke='%23e8c06a' stroke-width='.8' opacity='.7'/%3E%3C/svg%3E")}
#gate.open .flap{transform:rotateX(180deg);z-index:1}
.ga-seal{position:absolute;left:50%;top:57%;width:92px;height:92px;margin:-50px 0 0 -46px;z-index:6;will-change:transform,opacity;transition:transform .45s cubic-bezier(.5,-.5,.6,1),opacity .35s ease .1s}
.ga-seal svg{width:100%;height:100%}
#gate.go .ga-seal{transform:scale(1.25) rotate(-10deg);opacity:0}
.env .pulse-ring{top:57%;margin-top:-59px}
.env .seal-hit{top:57%;margin-top:-4px}
#gate.slide .card{transform:translateY(-60%)}
.env-back,.env-front,.ga-tapwrap{transition:transform .9s cubic-bezier(.5,0,.8,.4),opacity .7s ease}
#gate.zoom .env-back,#gate.zoom .env-front{transform:translateY(55vh);opacity:0}
#gate.zoom .flap{transform:translateY(55vh) rotateX(180deg);opacity:0;transition:transform .9s cubic-bezier(.5,0,.8,.4),opacity .7s}
#gate.zoom .card{transform:translateY(-34%) scale(1.45);transition:transform 1.2s cubic-bezier(.4,0,.2,1)}
''' + COMMON_CSS,
html=r'''<!-- =================== GATE =================== -->
<div id="gate" role="dialog" aria-label="Wedding invitation — tap to open">
  <div class="ga-dust" id="gaDust"></div>
  <div class="ga-wrap">
    <div class="ga-top">YOU ARE INVITED · <span>सादर आमंत्रण</span></div>
    <div class="ga-names foil"><span data-k="bride.name"></span> &amp; <span data-k="groom.name"></span></div>
    <div class="env">
      <div class="env-back"></div>
      <div class="card"><div class="card-in">
        <div class="c-shri">॥ श्री गणेशाय नमः ॥</div><div class="c-hi">शुभ विवाह</div>
        <div class="c-name" data-k="bride.name"></div><div class="c-amp">&amp;</div><div class="c-name" data-k="groom.name"></div>
        <div class="c-date" data-wdate></div>
      </div></div>
      <svg class="env-front" viewBox="0 0 100 130" preserveAspectRatio="none" aria-hidden="true"><defs>
        <linearGradient id="efL" x1="0" x2="1"><stop offset="0" stop-color="#e2cda2"/><stop offset="1" stop-color="#f3e6c9"/></linearGradient>
        <linearGradient id="efR" x1="1" x2="0"><stop offset="0" stop-color="#e2cda2"/><stop offset="1" stop-color="#f3e6c9"/></linearGradient>
        <linearGradient id="efB" x1="0" x2="0" y1="1" y2="0"><stop offset="0" stop-color="#e6d2a8"/><stop offset="1" stop-color="#f8eedb"/></linearGradient></defs>
        <polygon points="0,0 53,71 0,130" fill="url(#efL)"/><polygon points="100,0 47,71 100,130" fill="url(#efR)"/><polygon points="0,130 50,64 100,130" fill="url(#efB)"/>
        <g fill="none" stroke="#c9a14a" vector-effect="non-scaling-stroke"><path d="M0 130 50 64 100 130" stroke-width="1.6" vector-effect="non-scaling-stroke"/><path d="M8 126 50 71 92 126" stroke-width="1" stroke-dasharray="2 2" vector-effect="non-scaling-stroke"/><rect x="2.5" y="2.5" width="95" height="125" rx="1.5" stroke-width="1" vector-effect="non-scaling-stroke"/></g>
        <text x="50" y="114" text-anchor="middle" font-family="Rozha One,serif" font-size="7" fill="#9a6b1c" opacity=".85">शुभ विवाह</text>
      </svg>
      <div class="flap"><div class="f"><svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><g fill="none" stroke="#c9a14a"><path d="M0 0 50 100 100 0" stroke-width="1.8" vector-effect="non-scaling-stroke"/><path d="M9 3 50 88 91 3" stroke-width="1" stroke-dasharray="2 2" vector-effect="non-scaling-stroke"/></g></svg></div><div class="b"></div></div>
      <div class="pulse-ring"></div>
      <div class="ga-seal" data-art="seal"></div>
      <button class="seal-hit" aria-label="Tap the seal to open"></button>
    </div>
    <div class="tap">TAP THE SEAL · <b>मोहर को छुएं</b></div>
  </div>
  <div class="bloom"></div>
</div>

''',
init=r'''(()=>{ let d=''; for(let i=0;i<22;i++) d+=`<i style="left:${(Math.random()*100).toFixed(1)}%;animation-duration:${(7+Math.random()*7).toFixed(1)}s;animation-delay:${(-Math.random()*12).toFixed(1)}s"></i>`; $('#gaDust').innerHTML=d; })();''',
stages="[['open',60],['slide',950],['zoom',2000],['fade',2550],['unlock',2700],['remove',3500]]")

# =====================================================================
# B — RAJWADA CURTAINS (velvet stage)
# =====================================================================
V['b'] = dict(css=r'''/* ===================== GATE ===================== */
#gate{position:fixed;inset:0;z-index:60;overflow:hidden;will-change:opacity;transition:opacity .9s ease}
.cur{position:absolute;top:0;bottom:0;width:50.6%;z-index:1;will-change:transform;transition:transform 2.2s cubic-bezier(.55,.02,.22,1);
  background:
   linear-gradient(180deg,#ffffff12 0%,#0000 25%,#0000 72%,#00000066 100%),
   repeating-linear-gradient(90deg,#4a0913 0px,#6e1323 8px,#9d2536 14px,#c13c4d 17px,#9d2536 20px,#6e1323 26px,#4a0913 34px)}
.cur::before{content:"";position:absolute;inset:0;opacity:.12;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='80' viewBox='0 0 60 80'%3E%3Cg fill='none' stroke='%23f3d991' stroke-width='1'%3E%3Cpath d='M30 10c8 9 8 18 0 26-8-8-8-17 0-26zM30 70c8-9 8-18 0-26-8 8-8 17 0 26z'/%3E%3Ccircle cx='30' cy='40' r='2.5'/%3E%3C/g%3E%3C/svg%3E")}
.cur::after{content:"";position:absolute;left:0;right:0;bottom:0;height:30px;
  background:linear-gradient(#d9ad52,#f3d991 40%,#b8862b) top/100% 6px no-repeat,repeating-linear-gradient(90deg,#f3d991 0 2px,#c9a14a 2px 3px,#0000 3px 5px);
  -webkit-mask:linear-gradient(#000,#000) top/100% 6px no-repeat,repeating-linear-gradient(90deg,#000 0 3px,#0000 3px 5px);mask:linear-gradient(#000,#000) top/100% 6px no-repeat,repeating-linear-gradient(90deg,#000 0 3px,#0000 3px 5px)}
.cur.l{left:0;transform-origin:0 0;box-shadow:inset -7px 0 0 -2px #d9ad52,inset -9px 0 0 -2px #7a5013,10px 0 22px #0008}
.cur.r{right:0;transform-origin:100% 0;box-shadow:inset 7px 0 0 -2px #d9ad52,inset 9px 0 0 -2px #7a5013,-10px 0 22px #0008}
#gate.open .cur.l{transform:scaleX(.13)}
#gate.open .cur.r{transform:scaleX(.13)}
.tie{position:absolute;top:56%;width:15%;z-index:3;opacity:0;transition:opacity .7s ease 1.6s}
.tie.l{left:0}.tie.r{right:0;transform:scaleX(-1)}
#gate.open .tie{opacity:1}
.pel{position:absolute;top:0;left:0;right:0;z-index:4;will-change:transform;transition:transform 1s cubic-bezier(.6,0,.4,1)}
.pel svg{width:100%;height:auto;filter:none}
.pel-names{position:absolute;left:0;right:0;top:4.2%;text-align:center;font-family:var(--script);font-size:clamp(26px,7.4vw,34px);color:#f6dc8f;text-shadow:0 2px 6px #0009}
#gate.fade .pel{transform:translateY(-105%)}
.gb-center{position:absolute;left:50%;top:56%;transform:translate(-50%,-50%);z-index:5;display:flex;flex-direction:column;align-items:center;transition:opacity .35s ease,transform .45s ease}
.gb-sub{font-family:var(--hi-d);color:#f6dc8f;font-size:17px;margin-bottom:10px;text-shadow:0 2px 6px #0009}
.gb-medal{width:104px;height:104px;position:relative}
.gb-medal svg{width:100%;height:100%}
.gb-center .pulse-ring{margin:-55px 0 0 -55px}
.gb-center .tap{margin-top:16px}
#gate.go .gb-center{opacity:0;transform:translate(-50%,-50%) scale(.8)}
.gb-light{position:absolute;inset:0;z-index:0;background:radial-gradient(60% 50% at 50% 55%,#fff1c8,#ffd27a55 45%,#0000 75%);opacity:0;transition:opacity 1.6s ease .3s;pointer-events:none}
#gate.open .gb-light{opacity:.55}
#gate .seal-hit{top:56%;width:170px;height:170px}
''' + COMMON_CSS,
html=r'''<!-- =================== GATE =================== -->
<div id="gate" role="dialog" aria-label="Wedding invitation — tap to open">
  <div class="gb-light"></div>
  <div class="cur l"></div><div class="cur r"></div>
  <svg class="tie l" viewBox="0 0 60 90" aria-hidden="true"><path d="M0 18q30 6 46 0" stroke="#d9ad52" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M0 18q30 6 46 0" stroke="#7a5013" stroke-width="1" stroke-dasharray="3 3" fill="none"/><circle cx="46" cy="18" r="7" fill="#e8c06a" stroke="#7a5013"/><path d="M40 24h12l4 46H36z" fill="#d9ad52"/><path d="M38 30h16M37 40h18M37 50h18M36 60h20" stroke="#9a6b1c" stroke-width="1"/><path d="M36 70h20l-2 8H38z" fill="#b8862b"/></svg>
  <svg class="tie r" viewBox="0 0 60 90" aria-hidden="true"><path d="M0 18q30 6 46 0" stroke="#d9ad52" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M0 18q30 6 46 0" stroke="#7a5013" stroke-width="1" stroke-dasharray="3 3" fill="none"/><circle cx="46" cy="18" r="7" fill="#e8c06a" stroke="#7a5013"/><path d="M40 24h12l4 46H36z" fill="#d9ad52"/><path d="M38 30h16M37 40h18M37 50h18M36 60h20" stroke="#9a6b1c" stroke-width="1"/><path d="M36 70h20l-2 8H38z" fill="#b8862b"/></svg>
  <div class="pel"><svg id="pelmet" viewBox="0 0 400 150" preserveAspectRatio="xMidYMin slice" aria-hidden="true"></svg><div class="pel-names"><span data-k="bride.name"></span> &amp; <span data-k="groom.name"></span></div></div>
  <div class="gb-center">
    <div class="gb-sub">॥ शुभ विवाह ॥</div>
    <div class="gb-medal"><div class="pulse-ring"></div><div data-art="seal" style="width:100%;height:100%"></div></div>
    <div class="tap">TAP TO OPEN · <b>पर्दा उठाएं</b></div>
  </div>
  <button class="seal-hit" aria-label="Tap to open the invitation"></button>
</div>

''',
init=r'''(()=>{ let s=`<defs><linearGradient id="pv" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5a0d18"/><stop offset=".6" stop-color="#9d2536"/><stop offset="1" stop-color="#6e1323"/></linearGradient>
  <linearGradient id="pg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f6dc8f"/><stop offset="1" stop-color="#b8862b"/></linearGradient></defs>
  <rect width="400" height="40" fill="url(#pv)"/><rect y="0" width="400" height="5" fill="url(#pg)"/><rect y="36" width="400" height="4" fill="url(#pg)"/>`;
  for(let i=0;i<4;i++){ const x=i*100; s+=`<path d="M${x} 38Q${x+50} 132 ${x+100} 38Z" fill="url(#pv)"/><path d="M${x} 38Q${x+50} 132 ${x+100} 38" fill="none" stroke="url(#pg)" stroke-width="5"/><path d="M${x+8} 42Q${x+50} 120 ${x+92} 42" fill="none" stroke="#f3d991" stroke-width="1" stroke-dasharray="3 3" opacity=".8"/><circle cx="${x+50}" cy="72" r="5" fill="url(#pg)"/>`; }
  for(let i=0;i<=4;i++){ const x=i*100; s+=`<path d="M${x} 38v26" stroke="#d9ad52" stroke-width="2"/><circle cx="${x}" cy="66" r="5" fill="url(#pg)"/><path d="M${x-6} 70h12l3 30h-18z" fill="url(#pg)"/><path d="M${x-5} 78h10M${x-6} 86h12M${x-7} 94h14" stroke="#9a6b1c"/>`; }
  $('#pelmet').innerHTML=s; })();''',
stages="[['open',40],['unlock',1500],['zoom',1700],['fade',2200],['remove',3100]]")

# =====================================================================
# C — KAMAL BLOOM (golden mandala + opening lotus)
# =====================================================================
V['c'] = dict(css=r'''/* ===================== GATE ===================== */
#gate{position:fixed;inset:0;z-index:60;overflow:hidden;display:flex;align-items:center;justify-content:center;will-change:opacity;transition:opacity .9s ease;
  background:radial-gradient(circle at 50% 48%,#64287a 0%,#3a1250 42%,#1b0727 100%)}
.gc-stars{position:absolute;inset:0;pointer-events:none}
.gc-stars i{position:absolute;width:2px;height:2px;border-radius:50%;background:#fff;box-shadow:0 0 4px #fff;animation:twinkle 2.6s ease-in-out infinite}
.gc-wrap{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;will-change:transform;transition:transform 1.6s cubic-bezier(.5,0,.2,1)}
.gc-sub{font-family:var(--hi-d);color:#f3d991;font-size:16px;opacity:.9;transition:opacity .5s}
.gc-names{font-family:var(--script);font-size:clamp(38px,11vw,50px);line-height:1.2;padding:0 .2em;transition:opacity .5s}
#gate.open .gc-sub,#gate.open .gc-names{opacity:0}
.mandala{position:relative;width:min(88vw,370px);aspect-ratio:1;margin:6px 0 0}
.ring{position:absolute;inset:0;will-change:transform,opacity;transition:transform 1.6s cubic-bezier(.4,0,.2,1),opacity 1.2s ease}
.ring .spin{position:absolute;inset:0;will-change:transform}
.ring svg{width:100%;height:100%}
.ring.r3 .spin{animation:spin2 90s linear infinite}
.ring.r2{inset:11%}.ring.r2 .spin{animation:spin2 60s linear infinite reverse}
.ring.r1{inset:22%}.ring.r1 .spin{animation:spin2 40s linear infinite}
#gate.open .ring.r3{transform:scale(1.35);opacity:.0}
#gate.open .ring.r2{transform:scale(1.5);opacity:.0;transition-delay:.15s}
#gate.open .ring.r1{transform:scale(1.7);opacity:.0;transition-delay:.3s}
.halo2{position:absolute;inset:25%;border-radius:50%;background:radial-gradient(circle,#ffe7a8aa 0,#ffb84d33 45%,#0000 70%);animation:glow 3s ease-in-out infinite;will-change:opacity}
.lotus{position:absolute;inset:0}
.lp{position:absolute;left:50%;top:50%;width:17%;height:33%;margin:-33% 0 0 -8.5%;transform-origin:50% 100%;will-change:transform;
  transform:rotate(var(--c)) scale(var(--cs,1));transition:transform 1.5s cubic-bezier(.3,1.25,.45,1);transition-delay:calc(var(--i)*45ms)}
.lp svg{width:100%;height:100%;display:block}
.lp.back{--cs:.9}
#gate.open .lp{transform:rotate(var(--o)) scale(var(--os,1.05))}
.core{position:absolute;left:50%;top:50%;width:21%;height:21%;margin:-10.5% 0 0 -10.5%;border-radius:50%;z-index:3;display:grid;place-items:center;
  background:radial-gradient(circle at 40% 35%,#fff3c4,#e2b24f 55%,#8a5a14);box-shadow:0 0 0 3px #f6dc8f,0 0 24px #ffd98088;transition:transform 1.2s cubic-bezier(.3,1.4,.5,1) .3s;will-change:transform}
.core span{font-family:var(--script);font-size:clamp(28px,8vw,36px);color:var(--maroon);line-height:1;margin-top:4px}
#gate.open .core{transform:scale(1.25)}
.mandala .pulse-ring{width:60%;height:60%;margin:-30% 0 0 -30%}
.mandala .seal-hit{width:70%;height:70%}
#gate.zoom .gc-wrap{transform:scale(2.3)}
#gate.go .gc-wrap .tap{opacity:0}
''' + COMMON_CSS,
html=r'''<!-- =================== GATE =================== -->
<div id="gate" role="dialog" aria-label="Wedding invitation — tap to open">
  <div class="gc-stars" id="gcStars"></div>
  <div class="gc-wrap">
    <div class="gc-sub">॥ शुभ विवाह ॥</div>
    <div class="gc-names foil"><span data-k="bride.name"></span> &amp; <span data-k="groom.name"></span></div>
    <div class="mandala">
      <div class="ring r3"><div class="spin" id="ring3"></div></div>
      <div class="ring r2"><div class="spin" id="ring2"></div></div>
      <div class="ring r1"><div class="spin" id="ring1"></div></div>
      <div class="halo2"></div>
      <div class="lotus" id="lotus"></div>
      <div class="core"><span>S</span></div>
      <div class="pulse-ring"></div>
      <button class="seal-hit" aria-label="Tap the lotus to open"></button>
    </div>
    <div class="tap">TAP THE LOTUS · <b>कमल को छुएं</b></div>
  </div>
  <div class="bloom"></div>
</div>

''',
init=r'''(()=>{ let st=''; for(let i=0;i<46;i++) st+=`<i style="left:${(Math.random()*100).toFixed(1)}%;top:${(Math.random()*100).toFixed(1)}%;animation-delay:${(-Math.random()*3).toFixed(2)}s;opacity:${(.3+Math.random()*.7).toFixed(2)}"></i>`; $('#gcStars').innerHTML=st;
  const G=`<defs><linearGradient id="mg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#fff0b8"/><stop offset=".5" stop-color="#e2b24f"/><stop offset="1" stop-color="#9a6b1c"/></linearGradient></defs>`;
  let r3=G+`<circle r="48.5" fill="none" stroke="#e2b24f" stroke-width=".5" opacity=".7"/><circle r="38" fill="none" stroke="#e2b24f" stroke-width=".4" stroke-dasharray="1 1.5" opacity=".7"/>`;
  for(let i=0;i<36;i++){ const a=i*10; r3+=`<g transform="rotate(${a})"><path d="M0-47C2.6-44 2.6-41 0-39C-2.6-41-2.6-44 0-47Z" fill="url(#mg)" opacity=".85"/><circle cy="-36" r=".9" fill="#f6dc8f"/></g>`; }
  let r2=G+`<circle r="30" fill="none" stroke="#e2b24f" stroke-width=".6"/>`;
  for(let i=0;i<16;i++){ r2+=`<g transform="rotate(${i*22.5})"><path d="M0-49C8-42 7-34 0-30C-7-34-8-42 0-49Z" fill="url(#mg)" stroke="#8a5a14" stroke-width=".4"/><path d="M0-46C3.5-41 3-36 0-33C-3-36-3.5-41 0-46Z" fill="#7a1f2b" opacity=".55"/></g>`; }
  let r1=G;
  for(let i=0;i<24;i++){ r1+=`<g transform="rotate(${i*15})"><path d="M0-49C5-40 4-30 0-24C-4-30-5-40 0-49Z" fill="none" stroke="#f3d991" stroke-width=".7"/></g>`; }
  r1+=`<circle r="23" fill="none" stroke="#f3d991" stroke-width=".6"/>`;
  [['ring3',r3],['ring2',r2],['ring1',r1]].forEach(([id,c])=>$('#'+id).innerHTML=`<svg viewBox="-50 -50 100 100" aria-hidden="true">${c}</svg>`);
  const pet=(id,a,b)=>`<svg viewBox="0 0 40 80" aria-hidden="true"><defs><linearGradient id="${id}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${a}"/><stop offset=".65" stop-color="${b}"/><stop offset="1" stop-color="#fff4f6"/></linearGradient></defs><path d="M20 1C34 18 40 44 31 65C27 73 23 78 20 80C17 78 13 73 9 65C0 44 6 18 20 1Z" fill="url(#${id})" stroke="#f3c24f" stroke-width=".9"/><path d="M20 8V74" stroke="#fff" stroke-width=".8" opacity=".55"/><path d="M20 30C14 42 13 56 15 70M20 30C26 42 27 56 25 70" stroke="#fff" stroke-width=".5" opacity=".35" fill="none"/></svg>`;
  let L=''; const N=8;
  for(let i=0;i<N;i++){ const o=-157.5+i*45+22.5; L+=`<div class="lp back" style="--i:${i};--c:${((i-3.5)*3).toFixed(1)}deg;--o:${o}deg;--os:.95">${pet('pb'+i,'#c2185b','#f48fb1')}</div>`; }
  for(let i=0;i<N;i++){ const o=-157.5+i*45; L+=`<div class="lp" style="--i:${i+2};--c:${((i-3.5)*6).toFixed(1)}deg;--o:${o}deg">${pet('pf'+i,'#e0457b','#ffc1d6')}</div>`; }
  $('#lotus').innerHTML=L; })();''',
stages="[['open',40],['zoom',1550],['fade',2150],['unlock',2300],['remove',3150]]")

# =====================================================================
# D — MARBLE JAALI (sliding carved screens)
# =====================================================================
JAALI_MASK = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='36' height='36' viewBox='0 0 36 36'%3E%3Cpath fill-rule='evenodd' d='M0 0H36V36H0Z M18 5L21 13L29 10L25 18L29 26L21 23L18 31L15 23L7 26L11 18L7 10L15 13Z M0 0H5A5 5 0 0 1 0 5Z M36 0V5A5 5 0 0 1 31 0Z M0 36V31A5 5 0 0 1 5 36Z M36 36H31A5 5 0 0 1 36 31Z'/%3E%3C/svg%3E\")"
V['d'] = dict(css=r'''/* ===================== GATE ===================== */
#gate{position:fixed;inset:0;z-index:60;overflow:hidden;display:flex;align-items:center;justify-content:center;will-change:opacity;transition:opacity .9s ease;
  background:radial-gradient(120% 90% at 50% 38%,#f6dcc0 0%,#e2ad84 50%,#b86f47 100%)}
#gate::before{content:"";position:absolute;inset:0;opacity:.25;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48' viewBox='0 0 48 48'%3E%3Cg fill='none' stroke='%23fff' stroke-width='1'%3E%3Cpath d='M24 6c6 7 6 13 0 18-6-5-6-11 0-18zM24 42c6-7 6-13 0-18-6 5-6 11 0 18zM6 24c7-6 13-6 18 0-5 6-11 6-18 0zM42 24c-7-6-13-6-18 0 5 6 11 6 18 0z'/%3E%3C/g%3E%3C/svg%3E")}
.g-toran{position:absolute;top:0;left:0;width:100%;height:auto;z-index:3}
.gd-scene{position:relative;z-index:2;width:min(82vw,400px);display:flex;flex-direction:column;align-items:center;transform-origin:50% 58%;will-change:transform;transition:transform 1.7s cubic-bezier(.5,0,.2,1)}
#gate.zoom .gd-scene{transform:scale(1.9)}
.gd-head{display:flex;flex-direction:column;align-items:center;transition:opacity .5s}
#gate.open .gd-head{opacity:0}
.gd-names{font-family:var(--script);font-size:clamp(32px,9.4vw,42px);color:var(--maroon);line-height:1.1;text-shadow:0 1px 0 #fff8}
.gd-sub{font-family:var(--hi-d);color:var(--maroon-d);font-size:15px;margin-bottom:10px;opacity:.85}
.gd-arch{position:relative;width:100%;height:min(58svh,560px);display:flex;flex-direction:column}
.gd-arch::after{content:"";position:absolute;left:-8%;right:-8%;bottom:-26px;height:40px;background:radial-gradient(ellipse at 50% 40%,#5a1e1455,#0000 70%)}
.gd-cap{width:100%;height:auto;margin-bottom:-1px;position:relative;z-index:2}
.gd-body{flex:1;position:relative;z-index:1;padding:0 13px;background:linear-gradient(90deg,#e9e0d2,#fffdf8 20%,#fffdf8 80%,#e9e0d2);border:solid #c9a14a;border-width:0 2px}
.gd-body::before,.gd-body::after{content:"";position:absolute;top:8px;bottom:8px;width:3px;background:repeating-linear-gradient(#b71c3a 0 4px,#2e7d32 4px 8px,#c9a14a 8px 12px);opacity:.75}
.gd-body::before{left:4px}.gd-body::after{right:4px}
.gd-open{position:absolute;inset:0 13px;overflow:hidden;background:#3a1d0e;box-shadow:inset 0 0 0 2px #c9a14a}
.gd-glow{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 60%,#fffdf2 0%,#ffe6a0 30%,#f4ad5e 64%,#b4542e 100%)}
.gd-glow .rays{position:absolute;left:50%;top:60%;width:220%;aspect-ratio:1;transform:translate(-50%,-50%);will-change:transform;background:repeating-conic-gradient(from 0deg,#fff5 0 3deg,#fff0 3deg 12deg);-webkit-mask:radial-gradient(circle,#000 0,#0000 60%);mask:radial-gradient(circle,#000 0,#0000 60%);animation:spin 26s linear infinite;animation-play-state:paused}
#gate.open .gd-glow .rays{animation-play-state:running}
.jl{position:absolute;top:0;bottom:0;width:50%;will-change:transform;transition:transform 1.8s cubic-bezier(.6,.05,.22,1)}
.jl.l{left:0}.jl.r{right:0}
#gate.open .jl.l{transform:translateX(-102%)}
#gate.open .jl.r{transform:translateX(102%)}
.jl-m{position:absolute;inset:0;background:linear-gradient(90deg,#e8dfd1,#fffdf8 45%,#f4eee4 70%,#e3d9c8);
  -webkit-mask:linear-gradient(#000,#000) top/100% 12px no-repeat,linear-gradient(#000,#000) bottom/100% 12px no-repeat,linear-gradient(#000,#000) left/12px 100% no-repeat,linear-gradient(#000,#000) right/12px 100% no-repeat,__MASK__ 12px 12px/30px 30px;
  mask:linear-gradient(#000,#000) top/100% 12px no-repeat,linear-gradient(#000,#000) bottom/100% 12px no-repeat,linear-gradient(#000,#000) left/12px 100% no-repeat,linear-gradient(#000,#000) right/12px 100% no-repeat,__MASK__ 12px 12px/30px 30px}
.jl-in{position:absolute;inset:5px;border:1.5px solid #c9a14a;pointer-events:none}
.jl-in::after{content:"";position:absolute;inset:4px;border:1px solid #c9a14a88}
.jl.l .jl-in{border-right-width:1px}.jl.r .jl-in{border-left-width:1px}
.medh{position:absolute;top:50%;width:84px;height:84px;margin-top:-42px;z-index:3}
.jl.l .medh{right:-42px;clip-path:inset(0 50% 0 0)}
.jl.r .medh{left:-42px;clip-path:inset(0 0 0 50%)}
.medh svg{width:100%;height:100%}
.gd-open .pulse-ring{width:96px;height:96px;margin:-48px 0 0 -48px}
.d-steps{width:112%;margin-left:-6%;height:11px;background:linear-gradient(#fffdf8,#ded3c2);border-radius:2px;position:relative;z-index:2}
.d-steps+.d-steps{width:124%;margin-left:-12%;height:13px;margin-top:1px}
.g-diya{position:absolute;bottom:-14px;width:46px;z-index:3}
.g-diya.l{left:-14%}.g-diya.r{right:-14%}
'''.replace('__MASK__', JAALI_MASK) + COMMON_CSS,
html=r'''<!-- =================== GATE =================== -->
<div id="gate" role="dialog" aria-label="Wedding invitation — tap to open">
  <svg class="g-toran" data-toran viewBox="0 0 400 70" preserveAspectRatio="xMidYMin slice" aria-hidden="true"></svg>
  <div class="gd-scene">
    <div class="gd-head"><div class="gd-names"><span data-k="bride.name"></span> &amp; <span data-k="groom.name"></span></div><div class="gd-sub">॥ शुभ विवाह ॥</div></div>
    <div class="gd-arch">
      <svg class="gd-cap" id="gdCap" viewBox="0 0 400 200" aria-hidden="true"></svg>
      <div class="gd-body"><div class="gd-open">
        <div class="gd-glow"><div class="rays"></div></div>
        <div class="jl l"><div class="jl-m"></div><div class="jl-in"></div><div class="medh" data-art="medal"></div></div>
        <div class="jl r"><div class="jl-m"></div><div class="jl-in"></div><div class="medh" data-art="medal"></div></div>
        <div class="pulse-ring"></div>
        <button class="seal-hit" aria-label="Tap to open the invitation"></button>
      </div></div>
      <div class="d-steps"></div><div class="d-steps"></div>
      <div class="g-diya l" data-art="diya"></div><div class="g-diya r" data-art="diya"></div>
    </div>
    <div class="tap">TAP TO OPEN · <b>द्वार खोलें</b></div>
  </div>
  <div class="bloom"></div>
</div>

''',
init=r'''(()=>{ const outer=archPath(400,200,150,8,6), inner=archPath(344,200,158,40,6,28);
  const fl=(x,y,s)=>`<g transform="translate(${x} ${y}) scale(${s})">${[0,72,144,216,288].map(a=>`<ellipse cx="0" cy="-5" rx="3" ry="5" fill="#b71c3a" transform="rotate(${a})"/>`).join('')}<circle r="2.2" fill="#f3c24f"/><path d="M-12 6q6-4 9 0M12 6q-6-4-9 0" stroke="#2e7d32" stroke-width="2" fill="none"/></g>`;
  $('#gdCap').innerHTML=`<defs><linearGradient id="gmb" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fffdf8"/><stop offset="1" stop-color="#e9e0d2"/></linearGradient>
   <radialGradient id="gglw" cx="50%" cy="100%" r="90%"><stop offset="0" stop-color="#fff6d6"/><stop offset=".6" stop-color="#f8c77a"/><stop offset="1" stop-color="#d07a44"/></radialGradient>
   <pattern id="gjp" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="url(#gglw)"/><path d="M10 2L12 8L18 6L14 10L18 14L12 12L10 18L8 12L2 14L6 10L2 6L8 8Z" fill="none" stroke="#fffdf8" stroke-width="2.6"/><circle cx="0" cy="0" r="3" fill="#fffdf8"/><circle cx="20" cy="0" r="3" fill="#fffdf8"/><circle cx="0" cy="20" r="3" fill="#fffdf8"/><circle cx="20" cy="20" r="3" fill="#fffdf8"/></pattern>
   <radialGradient id="gmd" cx="45%" cy="35%"><stop offset="0" stop-color="#fff1bf"/><stop offset=".6" stop-color="#d9a94a"/><stop offset="1" stop-color="#8a5a14"/></radialGradient></defs>
   <path d="${outer} Z" fill="url(#gmb)" stroke="#c9a14a" stroke-width="2.5"/>
   <path d="${archPath(380,200,154,22,6,10)}" fill="none" stroke="#c9a14a" stroke-width="1.2" stroke-dasharray="3 3"/>
   <path d="${inner} Z" fill="url(#gjp)"/>
   <path d="${inner}" fill="none" stroke="#c9a14a" stroke-width="2.5"/>
   ${fl(40,150,1)}${fl(360,150,1)}${fl(200,22,.9)}${fl(110,70,.7)}${fl(290,70,.7)}
   <rect x="22" y="192" width="356" height="8" fill="url(#gmd)"/>`; })();''',
stages="[['open',60],['zoom',1400],['fade',2050],['unlock',2200],['remove',3050]]")

MEDAL = r'''  medal(){ const g=uid('md'),m=uid('mm'); return `<svg viewBox="0 0 100 100"><defs><radialGradient id="${m}" cx="40%" cy="35%"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e8dfd1"/></radialGradient><linearGradient id="${g}" x1="0" x2="1"><stop offset="0" stop-color="#b8862b"/><stop offset=".5" stop-color="#f6dc8f"/><stop offset="1" stop-color="#9a6b1c"/></linearGradient></defs>
    <circle cx="50" cy="50" r="46" fill="url(#${m})" stroke="url(#${g})" stroke-width="5"/><circle cx="50" cy="50" r="38" fill="none" stroke="#c9a14a" stroke-width="1" stroke-dasharray="2 2.5"/>
    ${[0,45,90,135,180,225,270,315].map(a=>`<ellipse cx="50" cy="16" rx="2.6" ry="4.5" fill="#b71c3a" transform="rotate(${a} 50 50)"/>`).join('')}
    <text x="50" y="64" text-anchor="middle" font-family="Great Vibes,cursive" font-size="40" fill="#7a1f2b">S</text></svg>`; },
'''

def build(key):
    v = V[key]
    src = s.replace('const ART={\n', 'const ART={\n' + MEDAL)
    c0, c1, h0, h1, j0, j1 = blocks(src)
    js = COMMON_JS.replace('__INIT__', v['init']).replace('__STAGES__', v['stages'])
    out = src[:c0] + v['css'] + '\n' + src[c1:h0] + v['html'] + src[h1:j0] + js + src[j1:]
    return out

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'out'), exist_ok=True)
    for k in (sys.argv[1:] or V.keys()):
        open(os.path.join(ROOT, 'out', f'{k}.html'), 'w').write(build(k))
        print('built', k)
