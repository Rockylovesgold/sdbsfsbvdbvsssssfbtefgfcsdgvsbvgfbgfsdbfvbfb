# FULLY AUTOMATED WEBSITE GENERATOR
import os
import shutil

print("Generating website...")

# 1. Write index.html
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Hull Web Fixers – Web Design, AI & Ads (Updated)</title>
<meta name="description" content="Hull's digital growth agency. Stunning websites, Google &amp; Facebook Ads, and AI automation for East Yorkshire businesses."/>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
<!-- ═══ SECURITY META TAGS ═══ -->
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=(), payment=()">
<!-- ═══ FONTS ═══ -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=swap" rel="stylesheet"/>
<style>
:root{--bg:#060a14;--bg2:#0b1220;--bg3:#101a2e;--bdr:rgba(255,255,255,.07);--bdr2:rgba(255,255,255,.12);--amber:#F5A623;--amb2:#FCD34D;--teal:#0EA5E9;--tl2:#38BDF8;--txt:#94a3b8;--txt2:#cbd5e1;--white:#f1f5f9;--max:1200px;--r:1.25rem}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{overflow-x:hidden;font-size:16px}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);overflow-x:hidden;line-height:1.7;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Syne',sans-serif;color:var(--white);line-height:1.1}
a{text-decoration:none;color:inherit}
img{max-width:100%;display:block}
.wrap{width:100%;max-width:var(--max);margin-left:auto;margin-right:auto;padding-left:clamp(1.25rem,5vw,2.5rem);padding-right:clamp(1.25rem,5vw,2.5rem)}
section{width:100%}
#prog{position:fixed;top:0;left:0;height:3px;z-index:9999;width:0;transition:width .1s linear;background:linear-gradient(90deg,var(--amber),var(--teal),var(--amber))}
.navbar{position:fixed;top:0;left:0;right:0;z-index:800;background:rgba(6,10,20,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);transition:background .3s}
.navbar-inner{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo-wrap{display:flex;align-items:center;gap:.75rem;flex-shrink:0}
.logo-img{height:44px;width:auto;object-fit:contain}
.logo-text{display:flex;flex-direction:column}
.logo-text span:first-child{font-family:'Syne',sans-serif;font-weight:900;font-size:1rem;color:var(--white);line-height:1}
.logo-text span:last-child{font-size:.65rem;color:var(--amber);opacity:.8;letter-spacing:.05em}
.nav-links{display:flex;align-items:center;gap:2rem}
.nav-links a{color:var(--txt);font-size:.875rem;font-weight:500;transition:color .2s;white-space:nowrap}
.nav-links a:hover{color:var(--white)}
.nav-ai-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--amber);margin-right:.4rem;animation:pulse-dot 2s infinite;vertical-align:middle}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(.8)}}
.btn-nav{background:var(--amber);color:#0a0a0a;font-weight:700;border:none;border-radius:.7rem;padding:.6rem 1.4rem;font-size:.85rem;cursor:pointer;transition:box-shadow .3s,transform .2s;white-space:nowrap;display:inline-block;position:relative;overflow:hidden}
.btn-nav::after{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);animation:shimmer 3s infinite}
@keyframes shimmer{0%,100%{left:-100%}10%,30%{left:100%}}
.btn-nav:hover{box-shadow:0 0 28px rgba(245,166,35,.5);transform:translateY(-2px)}
.hmb{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:6px}
.hmb span{display:block;width:22px;height:2px;background:var(--white);border-radius:2px;transition:all .3s}
.hmb.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hmb.open span:nth-child(2){opacity:0;transform:scaleX(0)}
.hmb.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
#mob-menu{display:none;position:fixed;inset:0;z-index:790;background:rgba(6,10,20,.98);flex-direction:column;align-items:center;justify-content:center;gap:2rem}
#mob-menu.open{display:flex}
#mob-menu a{font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;color:var(--white);transition:color .2s}
#mob-menu a:hover{color:var(--amber)}
#mob-menu .btn-mob{background:var(--amber);color:#0a0a0a;padding:.9rem 2.5rem;border-radius:.9rem;font-size:1rem;font-weight:800;margin-top:1rem;font-family:'Syne',sans-serif}
.btn-primary{display:inline-flex;align-items:center;gap:.5rem;background:var(--amber);color:#0a0a0a;font-weight:700;padding:.9rem 2rem;border-radius:var(--r);font-size:.95rem;transition:box-shadow .35s,transform .25s;white-space:nowrap;border:none;cursor:pointer;font-family:'Inter',sans-serif;position:relative;overflow:hidden}
.btn-primary::after{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);transition:0.5s}
.btn-primary:hover::after{left:100%;transition:0.5s}
.btn-primary:hover{box-shadow:0 0 36px rgba(245,166,35,.55),0 10px 24px rgba(245,166,35,.2);transform:translateY(-3px)}
.btn-secondary{display:inline-flex;align-items:center;gap:.5rem;background:transparent;color:var(--txt2);font-weight:600;padding:.9rem 2rem;border-radius:var(--r);font-size:.95rem;border:1px solid var(--bdr2);transition:border-color .25s,background .25s,transform .25s;white-space:nowrap}
.btn-secondary:hover{border-color:rgba(245,166,35,.35);background:rgba(245,166,35,.05);transform:translateY(-2px)}
.pulse-anim{animation:halo 2.8s infinite}
@keyframes halo{0%,100%{box-shadow:0 0 0 0 rgba(245,166,35,.45)}60%{box-shadow:0 0 0 18px rgba(245,166,35,0)}}
.label-pill{display:inline-flex;align-items:center;gap:.4rem;background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.2);color:var(--amber);font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:.4rem 1rem;border-radius:9999px}
.accent-line{width:48px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--amber),var(--teal));margin-bottom:1rem}
.grad-amber{background:linear-gradient(120deg,var(--amber),var(--amb2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.grad-teal{background:linear-gradient(120deg,var(--teal),var(--tl2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.grad-both{background:linear-gradient(130deg,var(--amber) 0%,var(--teal) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.card{background:var(--bg2);border:1px solid var(--bdr);border-radius:var(--r);transition:transform .4s cubic-bezier(.25,.8,.25,1),border-color .35s,box-shadow .35s}
.card:hover{transform:translateY(-6px);border-color:rgba(245,166,35,.3);box-shadow:0 24px 56px rgba(0,0,0,.45),0 0 0 1px rgba(245,166,35,.05)}
.rv{opacity:0;transform:translateY(28px);transition:opacity .8s cubic-bezier(.25,.8,.25,1),transform .8s cubic-bezier(.25,.8,.25,1)}
.rv.vis{opacity:1;transform:translateY(0)}
.rv[data-d="1"]{transition-delay:.1s}.rv[data-d="2"]{transition-delay:.2s}.rv[data-d="3"]{transition-delay:.3s}.rv[data-d="4"]{transition-delay:.4s}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.cursor{display:inline-block;width:3px;height:.9em;background:var(--amber);margin-left:4px;vertical-align:middle;border-radius:2px;animation:blink .9s step-end infinite}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.float{animation:floaty 5s ease-in-out infinite}
.kcom-box{width:14px;height:22px;border:2px solid #fff;border-radius:2px 2px 0 0;position:relative;display:inline-block;vertical-align:middle;margin-right:6px;background:rgba(255,255,255,.1)}
.kcom-box::before{content:'';position:absolute;top:2px;left:2px;right:2px;height:12px;border:1px solid rgba(255,255,255,.5)}
/* Enhanced UI Animations */
.stagger-load > * {opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease}
.stagger-load.vis > * {opacity:1;transform:translateY(0)}
.stagger-load.vis > *:nth-child(1){transition-delay:0s}
.stagger-load.vis > *:nth-child(2){transition-delay:.1s}
.stagger-load.vis > *:nth-child(3){transition-delay:.2s}
.stagger-load.vis > *:nth-child(4){transition-delay:.3s}
.stagger-load.vis > *:nth-child(5){transition-delay:.4s}
/* Spotlight Hover */
.card-spot{position:relative;overflow:hidden;transition:transform .4s,border-color .35s,box-shadow .35s}
.card-spot::before{content:'';position:absolute;top:var(--y,0);left:var(--x,0);width:500px;height:500px;background:radial-gradient(circle,rgba(245,166,35,.15),transparent 70%);transform:translate(-50%,-50%);opacity:0;transition:opacity .4s;pointer-events:none;z-index:1}
.card-spot:hover::before{opacity:1}
@keyframes tick{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.ticker-track{display:flex;width:max-content;gap:3rem;align-items:center;animation:tick 45s linear infinite;will-change:transform}
details[open] .faq-body{animation:fopen .3s ease}
@keyframes fopen{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
details summary::-webkit-details-marker{display:none}
details summary{list-style:none}
.fi{width:100%;background:var(--bg);border:1px solid var(--bdr2);border-radius:.85rem;padding:.9rem 1.1rem;color:var(--white);font-size:.9rem;outline:none;font-family:'Inter',sans-serif;transition:border-color .25s,box-shadow .25s}
.fi::placeholder{color:#475569}
.fi:focus{border-color:rgba(245,166,35,.6);box-shadow:0 0 0 3px rgba(245,166,35,.1)}
select.fi option{background:var(--bg2);color:var(--white)}
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:120px 0 80px;overflow:hidden}
.hero canvas{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.hero-glows{position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse 60% 70% at 0% 60%,rgba(245,166,35,.07),transparent),radial-gradient(ellipse 55% 65% at 100% 35%,rgba(14,165,233,.06),transparent)}
.hero-bridge{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:100%;max-width:1400px;pointer-events:none;z-index:0;opacity:.04}
.hero-inner{position:relative;z-index:10;display:grid;grid-template-columns:1fr 480px;gap:4rem;align-items:center}
.hero-copy{max-width:620px}
.hero-copy h1{font-size:clamp(2.4rem,4.5vw,3.8rem);font-weight:900;margin:1.25rem 0;line-height:1.08}
.hero-copy p{font-size:clamp(.95rem,1.5vw,1.1rem);max-width:44ch;color:var(--txt);line-height:1.75;margin-bottom:2rem}
.hero-btns{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem}
.hero-trust{display:flex;flex-wrap:wrap;gap:1.25rem}
.hero-trust span{display:flex;align-items:center;gap:.4rem;font-size:.82rem;color:#64748b}
.hero-trust .ms{font-size:1.1rem;color:var(--amber);font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400}
.hero-card{background:var(--bg2);border:1px solid var(--bdr2);border-radius:1.5rem;overflow:hidden;box-shadow:0 32px 64px rgba(0,0,0,.5),0 0 80px rgba(14,165,233,.05)}
.hero-card-chrome{background:var(--bg3);padding:.75rem 1.25rem;display:flex;align-items:center;gap:.6rem;border-bottom:1px solid var(--bdr)}
.tc{width:11px;height:11px;border-radius:50%}
.tc1{background:rgba(239,68,68,.55)}.tc2{background:rgba(245,166,35,.55)}.tc3{background:rgba(34,197,94,.55)}
.url-bar{flex:1;height:26px;background:rgba(255,255,255,.04);border-radius:.4rem;display:flex;align-items:center;padding:0 .75rem;font-size:.7rem;color:#475569;font-family:monospace}
.hero-card-body{padding:1.25rem;display:flex;flex-direction:column;gap:1rem}
.metric-row{display:grid;grid-template-columns:1fr 1fr;gap:.75rem}
.metric{background:var(--bg3);border:1px solid var(--bdr);border-radius:1rem;padding:1rem}
.metric-label{font-size:.72rem;color:#64748b;margin-bottom:.4rem}
.metric-val{font-family:'Syne',sans-serif;font-size:1.9rem;font-weight:900;color:var(--white);line-height:1}
.metric-sub{font-size:.7rem;color:#22c55e;font-weight:700;margin-top:.25rem}
.chart-bars{display:flex;align-items:flex-end;gap:3px;height:32px;margin-top:.6rem}
.bar{flex:1;border-radius:2px 2px 0 0;background:rgba(245,166,35,.25)}.bar.hi{background:var(--amber)}
.ai-status{background:var(--bg3);border:1px solid rgba(14,165,233,.25);border-radius:1rem;padding:.85rem 1rem;display:flex;align-items:center;gap:.75rem}
.ai-icon{width:36px;height:36px;border-radius:.7rem;background:rgba(14,165,233,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.ai-icon .ms{color:var(--teal);font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400}
.ai-live{margin-left:auto;display:flex;align-items:center;gap:.35rem;font-size:.7rem;font-weight:700;color:#22c55e}
.dot-live{width:7px;height:7px;border-radius:50%;background:#22c55e;animation:pulse-dot 1.5s infinite}
.loc-pill{background:rgba(245,166,35,.04);border:1px solid rgba(245,166,35,.12);border-radius:.8rem;padding:.65rem 1rem;display:flex;align-items:center;justify-content:space-between}
.ticker-wrap{background:var(--bg2);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);padding:.85rem 0;overflow:hidden}
.ticker-item{color:#475569;font-weight:600;font-size:.78rem;white-space:nowrap;display:inline-flex;align-items:center;gap:.5rem}
.ticker-dot{width:5px;height:5px;border-radius:50%;background:var(--bdr2);display:inline-block}
.section{padding:clamp(3.5rem, 5vw, 6rem) 0;position:relative;z-index:1}
.section-sm{padding:3rem 0;position:relative;z-index:1}
/* Global Background Pattern */
.global-pat{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.03) 1px,transparent 1px);background-size:24px 24px;mask-image:linear-gradient(to bottom,transparent,black 20%,black 80%,transparent);pointer-events:none;z-index:-1}
/* New visually striking gradients */
.hero-glows{position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(circle at 15% 50%,rgba(245,166,35,.08),transparent 50%),radial-gradient(circle at 85% 30%,rgba(14,165,233,.08),transparent 50%)}
/* Enhanced Mobile Buttons */
@media(max-width:480px){
  .btn-primary,.btn-secondary{width:100%;justify-content:center;padding:1rem}
  .hero-btns{flex-direction:column;width:100%;gap:0.75rem}
  .hero-copy h1{font-size:2.4rem}
}
.section-header{text-align:center;margin-bottom:3.5rem}
.section-header h2{font-size:clamp(2rem,3.5vw,3rem);font-weight:900;margin-top:.5rem;margin-bottom:1rem}
.section-header p{color:var(--txt);max-width:46ch;margin:0 auto;font-size:1.05rem}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem}
.stat-card{background:var(--bg2);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem 1.5rem;text-align:center;transition:transform .4s,border-color .3s}
.stat-card:hover{transform:translateY(-5px);border-color:rgba(245,166,35,.25)}
.stat-num{font-family:'Syne',sans-serif;font-size:3rem;font-weight:900;line-height:1;display:block}
.stat-unit{font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:900}
.stat-label{color:var(--txt2);font-weight:600;font-size:.9rem;margin-top:.6rem;display:block}
.stat-sub{color:#475569;font-size:.75rem;margin-top:.2rem;display:block}
.services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}
.services-grid.stagger-load > * {opacity:0}
.svc-card{padding:2rem;display:flex;flex-direction:column}
.svc-icon{width:48px;height:48px;border-radius:.85rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;flex-shrink:0}
.svc-icon .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.5rem}
.svc-card h3{font-size:1.1rem;font-weight:700;margin-bottom:.6rem}
.svc-card p{font-size:.88rem;line-height:1.7;color:var(--txt);flex:1;max-width:34ch}
.svc-link{display:inline-flex;align-items:center;gap:.3rem;font-size:.82rem;font-weight:700;margin-top:1.25rem;transition:gap .25s}
.svc-link:hover{gap:.6rem}
.svc-link .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem}
.svc-link .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem}
.compare-wrap{border:1px solid var(--bdr2);border-radius:1.5rem;overflow:hidden;background:var(--bg2)}
.compare-header{background:var(--bg3);padding:1.5rem;border-bottom:1px solid var(--bdr);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1.5rem}
.compare-badge{width:40px;height:40px;border-radius:.75rem;background:var(--amber);color:#0a0a0a;font-size:.9rem;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:'Syne',sans-serif;box-shadow:0 4px 12px rgba(245,166,35,.3)}
.compare-stage{position:relative;height:450px;user-select:none;background:#000}
.compare-range{position:absolute;inset:0;width:100%;height:100%;opacity:0;z-index:20;cursor:ew-resize}
.compare-handle{position:absolute;top:0;bottom:0;width:44px;margin-left:-22px;display:flex;align-items:center;justify-content:center;pointer-events:none;z-index:20;left:50%}
.compare-handle-circle{width:40px;height:40px;border-radius:50%;background:var(--amber);display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(245,166,35,.65)}
.compare-handle-circle .ms{color:#0a0a0a;font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.2rem}
.ai-explainer{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:start;margin-bottom:3.5rem}
.ai-check{display:flex;align-items:flex-start;gap:.75rem;padding:.9rem 1rem;background:var(--bg);border:1px solid var(--bdr);border-radius:.85rem;margin-bottom:.6rem}
.ai-check .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem}
.ai-check strong{color:var(--white);font-size:.9rem;display:block}
.ai-check span{color:#64748b;font-size:.78rem}
.ai-net-wrap{background:var(--bg);border:1px solid var(--bdr2);border-radius:1.25rem;overflow:hidden;position:relative;min-height:320px}
.ai-cards{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
.ai-card{padding:2rem;display:flex;flex-direction:column;gap:1.25rem}
.ai-card-icon{width:56px;height:56px;border-radius:1rem;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.ai-card-icon .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.6rem}
.ai-card h3{font-size:1.15rem;font-weight:700;margin-bottom:.25rem}
.ai-card p{font-size:.88rem;line-height:1.7;color:var(--txt);max-width:38ch}
.ai-bullets{list-style:none;display:flex;flex-direction:column;gap:.6rem}
.ai-bullets li{display:flex;align-items:flex-start;gap:.6rem;font-size:.855rem;color:var(--txt2)}
.ai-bullets li .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:.95rem;flex-shrink:0;margin-top:.15rem}
.ai-cta{display:inline-flex;align-items:center;gap:.5rem;padding:.75rem 1.5rem;border-radius:.85rem;font-size:.85rem;font-weight:700;border:1px solid;transition:background .25s;margin-top:auto}
.ai-cta:hover{filter:brightness(1.15)}
.ads-grid{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem}
.ads-grid.stagger-load > * {opacity:0}
.ad-card{background:var(--bg2);border:1px solid var(--bdr);border-radius:1.5rem;padding:2.5rem;display:flex;flex-direction:column;gap:1.5rem;transition:transform .4s,border-color .3s}
.ad-card:hover{transform:translateY(-5px);border-color:rgba(245,166,35,.25)}
.ad-card h3{font-size:1.5rem;font-weight:800}
.ad-card p{font-size:.9rem;line-height:1.75;color:var(--txt);max-width:40ch}
.ad-bullets{list-style:none;display:flex;flex-direction:column;gap:.7rem}
.ad-bullets li{display:flex;align-items:flex-start;gap:.6rem;font-size:.875rem;color:var(--txt2)}
.ad-bullets li .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem;flex-shrink:0;margin-top:.1rem}
.ad-preview{background:var(--bg);border:1px solid var(--bdr);border-radius:1rem;padding:1rem}
.ad-preview-label{font-size:.7rem;color:#475569;text-transform:uppercase;letter-spacing:.08em;font-weight:600;margin-bottom:.75rem}
.search-result{padding:.75rem;border-radius:.6rem;margin-bottom:.5rem;border:1px solid}
.sr-top{display:flex;align-items:center;gap:.4rem;margin-bottom:.25rem}
.sr-badge{font-size:.6rem;padding:.15rem .4rem;border-radius:.25rem;font-weight:700;background:#166534;color:#4ade80}
.sr-domain{font-size:.7rem;color:#64748b}
.sr-title{font-size:.85rem;color:#60a5fa;font-weight:600}
.sr-desc{font-size:.72rem;color:#64748b;margin-top:.2rem}
.fb-mock{border-radius:.85rem;overflow:hidden;border:1px solid #3a3b3c;max-width:280px}
.fb-top{padding:.65rem .85rem;display:flex;align-items:center;gap:.6rem;border-bottom:1px solid #3a3b3c;background:#1c1e21}
.fb-av{width:30px;height:30px;border-radius:50%;background:var(--amber);display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:800;color:#0a0a0a;flex-shrink:0}
.fb-body{padding:.65rem .85rem;background:#1c1e21}
.fb-img{margin:.2rem -.85rem .2rem;height:60px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(245,166,35,.12),rgba(14,165,233,.08));border-top:1px solid #3a3b3c;border-bottom:1px solid #3a3b3c}
.fb-footer{padding:.5rem .85rem;background:#1c1e21;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #3a3b3c}
.fb-btn{background:#1877F2;color:white;font-size:.68rem;font-weight:700;padding:.3rem .7rem;border-radius:.35rem}
.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem}
.process-grid.stagger-load > * {opacity:0}
.proc-card{background:var(--bg2);border:1px solid var(--bdr);border-radius:var(--r);padding:1.75rem 1.25rem;text-align:center;position:relative;transition:transform .4s}
.proc-card:hover{transform:translateY(-5px)}
.proc-num{position:absolute;top:-14px;left:50%;transform:translateX(-50%);width:28px;height:28px;border-radius:50%;background:var(--amber);color:#0a0a0a;font-size:.75rem;font-weight:900;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif}
.proc-icon{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.8rem;color:var(--amber);margin:1rem 0 .75rem;display:block}
.proc-card h3{font-size:.95rem;font-weight:700;margin-bottom:.4rem}
.proc-card p{font-size:.82rem;color:var(--txt);max-width:24ch;margin:0 auto}
.faq-list{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:.75rem}
details.faq{background:var(--bg2);border:1px solid var(--bdr);border-radius:1rem;overflow:hidden;transition:border-color .25s}
details.faq[open]{border-color:rgba(245,166,35,.25)}
details.faq summary{display:flex;justify-content:space-between;align-items:flex-start;gap:1.5rem;padding:1.25rem 1.5rem;cursor:pointer;color:var(--white);font-weight:600;font-size:.95rem}
details.faq summary .chevron{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);transition:transform .3s;flex-shrink:0;font-size:1.3rem;margin-top:.05rem}
details.faq[open] summary .chevron{transform:rotate(180deg)}
.faq-body{padding:0 1.5rem 1.25rem;font-size:.9rem;color:var(--txt);line-height:1.75;border-top:1px solid var(--bdr);padding-top:1rem;max-width:58ch}
.contact-grid{display:grid;grid-template-columns:1fr 1.55fr;gap:3.5rem;align-items:start}
.contact-info h2{font-size:clamp(1.8rem,2.8vw,2.5rem);font-weight:900;margin-top:.5rem;margin-bottom:1rem}
.contact-info>p{font-size:.95rem;max-width:36ch;margin-bottom:2rem}
.contact-link{display:flex;align-items:center;gap:1rem;padding:1rem;background:var(--bg2);border:1px solid var(--bdr);border-radius:1rem;color:var(--white);transition:border-color .25s;margin-bottom:.6rem}
.contact-link:hover{border-color:rgba(245,166,35,.3)}
.contact-link .icon-wrap{width:40px;height:40px;border-radius:.75rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:rgba(245,166,35,.08)}
.contact-link .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)}
.contact-link strong{font-size:.9rem;font-weight:600;display:block}
.contact-link small{color:#64748b;font-size:.75rem}
.map-box{background:var(--bg);border:1px solid var(--bdr);border-radius:1rem;padding:1rem;overflow:hidden;margin-top:1rem}
.contact-form{background:var(--bg2);border:1px solid var(--bdr2);border-radius:1.5rem;padding:2.25rem;box-shadow:0 24px 64px rgba(0,0,0,.4)}
.contact-form h3{font-size:1.25rem;margin-bottom:.3rem}
.contact-form>p{font-size:.85rem;color:#64748b;margin-bottom:1.75rem}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.form-field{display:flex;flex-direction:column;gap:.4rem}
.form-field label{font-size:.72rem;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.07em}
.form-submit{width:100%;padding:1rem;background:var(--amber);color:#0a0a0a;font-weight:800;font-size:1rem;border:none;border-radius:var(--r);cursor:pointer;font-family:'Syne',sans-serif;display:flex;align-items:center;justify-content:center;gap:.5rem;transition:box-shadow .35s,transform .25s}
.form-submit:hover{box-shadow:0 0 40px rgba(245,166,35,.55);transform:translateY(-3px)}
.form-submit .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400}
.footer{background:var(--bg);border-top:1px solid var(--bdr);padding:4rem 0 2rem}
.footer-inner{display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:3rem}
.footer h4{font-size:.85rem;font-weight:700;color:var(--white);margin-bottom:1.1rem;font-family:'Syne',sans-serif}
.footer ul{list-style:none;display:flex;flex-direction:column;gap:.65rem}
.footer ul a{font-size:.85rem;color:#64748b;transition:color .2s}
.footer ul a:hover{color:var(--amber)}
.footer ul li{font-size:.85rem;color:#64748b}
.footer-bottom{border-top:1px solid var(--bdr);padding-top:1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem}
.footer-bottom p,.footer-bottom a{font-size:.78rem;color:#334155}
.footer-bottom a:hover{color:#64748b}
.footer-links{display:flex;gap:1.5rem}
.hull-banner{width:100%;height:64px;border-radius:1rem;overflow:hidden;position:relative;margin-bottom:2.5rem;background:linear-gradient(90deg,rgba(245,166,35,.03),rgba(14,165,233,.03))}
.hull-banner svg{position:absolute;inset:0;width:100%;height:100%}
.hull-banner-text{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.hull-banner-text p{font-size:.82rem;color:#475569;display:flex;align-items:center;gap:.5rem}
.hull-banner-text .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem}

/* Background Pattern (Consolidated) */
.bg-grid{background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);background-size:40px 40px;mask-image:linear-gradient(to bottom,transparent 5%,black 40%,black 80%,transparent 95%);opacity:0.7}
.ornament{position:absolute;width:400px;height:400px;background:radial-gradient(closest-side,rgba(245,166,35,.1),transparent);border-radius:50%;pointer-events:none;z-index:0;filter:blur(50px)}
/* Tech Marquee */
.tech-stack{padding:2rem 0;background:var(--bg2);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);overflow:hidden;position:relative}
.tech-track{display:flex;gap:4rem;animation:tick 30s linear infinite;width:max-content;opacity:.6}
.tech-item{font-size:1.5rem;color:var(--txt2);font-weight:700;display:flex;align-items:center;gap:.5rem;font-family:'Syne',sans-serif}
/* Recent Projects */
.project-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2.5rem}
.proj-card{background:var(--bg2);border:1px solid var(--bdr);border-radius:1rem;overflow:hidden;position:relative;group:1}
.proj-img{height:200px;background:var(--bg3);display:flex;align-items:center;justify-content:center;color:var(--txt2);font-size:.8rem;border-bottom:1px solid var(--bdr);overflow:hidden;position:relative}
.proj-fallback{position:absolute;inset:0;background:linear-gradient(135deg,rgba(245,166,35,.05),rgba(14,165,233,.05));display:flex;align-items:center;justify-content:center;flex-direction:column;gap:.5rem}
.proj-fallback .ms{font-size:3rem;opacity:.2;color:var(--txt)}
.proj-body{padding:1.25rem}
.proj-tag{font-size:.65rem;color:var(--amber);text-transform:uppercase;letter-spacing:.05em;font-weight:700;margin-bottom:.3rem;display:block}
.img-place{width:100%;height:100%;object-fit:cover}
.mock-browser{width:100%;height:100%;background:var(--bg3);display:flex;flex-direction:column;border-bottom:1px solid var(--bdr)}
.mock-header{height:12px;display:flex;align-items:center;gap:3px;padding:0 6px;border-bottom:1px solid var(--bdr2)}
.mock-dot{width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,.2)}
.mock-body{flex:1;padding:12px;display:flex;flex-direction:column;gap:6px;position:relative;overflow:hidden}
.mock-hero{width:100%;height:40%;background:linear-gradient(120deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border-radius:4px}
.mock-line{height:4px;background:rgba(255,255,255,.05);border-radius:2px;width:100%}
.mock-line.sm{width:60%}
/* Responsive Improvements */
/* Strict Mobile Override */
@media(max-width:767px){
  .hero-inner, .stats-grid, .services-grid, .project-grid, .process-grid, .contact-grid, .footer-inner, .ai-cards, .ads-grid{grid-template-columns:1fr !important;gap:2rem !important}
  .hero-btns{flex-direction:column;width:100%}
  .btn-primary, .btn-secondary{width:100%;justify-content:center}
  .hero-copy h1{font-size:2.4rem;line-height:1.1}
  .compare-stage{height:300px}
  .section{padding:3rem 0}
  .nav-links{display:none} 
  .hmb{display:flex}
  .contact-form{padding:1.5rem}
}
</style>
</head>
/* Image Loading & Empty Space Fixes */
.proj-card img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.proj-card:hover img{transform:scale(1.05)}
.placeholder-img{background:linear-gradient(135deg,var(--bg3),var(--bg2));width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.1)}

/* Device Adaptation Classes */
.is-mobile .hero-inner{gap:2rem}
.is-desktop .hero-inner{gap:5rem}

/* Visual Density */
.section{padding:clamp(4rem,10vw,8rem) 0}
.wrap{padding:0 2rem}
@media(max-width:768px){
  .section{padding:3.5rem 0}
  .wrap{padding:0 1.25rem}
}

/* ChatGPT Logo Container */
.chatgpt-partner{display:inline-flex;align-items:center;gap:.75rem;padding:.5rem 1rem;background:rgba(16,163,127,.1);border:1px solid rgba(16,163,127,.2);border-radius:1rem;margin-bottom:1.5rem}
.chatgpt-partner img{height:20px;width:auto}
.chatgpt-partner span{font-size:.85rem;font-weight:700;color:#10a37f}

</style>
<script>
// Device Detector
function updateDeviceClass(){
  const body = document.body;
  if(window.innerWidth < 768){
    body.classList.add('is-mobile');
    body.classList.remove('is-desktop');
  } else {
    body.classList.add('is-desktop');
    body.classList.remove('is-mobile');
  }
}
window.addEventListener('resize', updateDeviceClass);
document.addEventListener('DOMContentLoaded', updateDeviceClass);
</script>
</head>
<body class="is-desktop">
<nav class="navbar">
<div class="wrap navbar-inner">
  <a href="#" class="logo-wrap">
    <img src="nav_logo.png" alt="Hull Web Fixers" class="logo-img" onerror="this.style.display='none'">
    <div class="logo-text"><span>Hull Web Fixers</span><span>Digital Growth Agency</span></div>
  </a>
  <div class="nav-links">
    <a href="#services">Services</a>
    <a href="#portfolio">Portfolio</a>
    <a href="#ai"><span class="nav-ai-dot"></span>AI Automation</a>
    <a href="#ads">Advertising</a>
    <a href="#faq">FAQ</a>
  </div>
  <div style="display:flex;align-items:center;gap:.75rem">
    <a href="#contact" class="btn-nav">Get a Free Quote</a>
    <button class="hmb" id="hmb" onclick="toggleMob()" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</div>
</nav>

<section class="hero">
  <canvas id="pcv"></canvas>
  <div class="hero-glows"></div>
  <svg class="hero-bridge" viewBox="0 0 1600 420" fill="none" style="height:420px">
    <rect x="430" y="60" width="18" height="260" fill="#F5A623"/>
    <rect x="1152" y="60" width="18" height="260" fill="#F5A623"/>
    <path d="M439 64 Q800 -5 1161 64" stroke="#F5A623" stroke-width="5" fill="none"/>
    <line x1="439" y1="64" x2="240" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="439" y1="64" x2="340" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="439" y1="64" x2="440" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="439" y1="64" x2="540" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="439" y1="64" x2="640" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="439" y1="64" x2="740" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="860" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="960" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="1060" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="1160" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="1260" y2="320" stroke="#F5A623" stroke-width=".8"/>
    <line x1="1161" y1="64" x2="1360" y2="320" stroke="#F5A623" stroke-width=".8"/>
  </svg>
  <div class="wrap">
    <div class="hero-inner">
      <div class="hero-copy rv">
        <div class="chatgpt-partner">
          <img src="chatgpt_logo.png" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg'" alt="ChatGPT Logo">
          <span>Powered by OpenAI</span>
        </div>
        <div class="label-pill"><span style="width:7px;height:7px;border-radius:50%;background:#22c55e;display:inline-block;animation:pulse-dot 2s infinite"></span>Hull &amp; East Yorkshire's Digital Growth Team</div>
        <h1>We Build.<br/>We Automate.<br/><span class="grad-both" id="twt"></span><span class="cursor"></span></h1>
        <p>From stunning websites to AI automation and targeted advertising — we help Hull businesses grow faster, with less effort.</p>
        <div class="hero-btns">
          <a href="#contact" class="btn-primary pulse-anim">Get a Free Consultation<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.1rem">arrow_outward</span></a>
          <a href="#ai" class="btn-secondary"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.1rem;color:var(--amber)">smart_toy</span>Explore AI</a>
        </div>
        <div class="hero-trust">
          <span><span class="ms">verified</span>No-obligation quote</span>
          <span><i class="kcom-box"></i>Based in Hull, HU1</span>
          <span><span class="ms">schedule</span>Fast response</span>
        </div>
      </div>
      <div class="hero-card float rv" data-d="2">
        <div class="hero-card-chrome">
          <div class="tc tc1"></div><div class="tc tc2"></div><div class="tc tc3"></div>
          <div class="url-bar">yourhullbusiness.co.uk &#128274;</div>
        </div>
        <div class="hero-card-body">
          <div class="metric-row">
            <div class="metric">
              <div class="metric-label">Monthly Enquiries</div>
              <div class="metric-val">47</div>
              <div class="metric-sub">&#9650; 287% increase</div>
              <div class="chart-bars"><div class="bar" style="height:40%"></div><div class="bar" style="height:55%"></div><div class="bar" style="height:38%"></div><div class="bar" style="height:72%"></div><div class="bar" style="height:58%"></div><div class="bar hi" style="height:100%"></div></div>
            </div>
            <div class="metric">
              <div class="metric-label">Ad Return (ROAS)</div>
              <div class="metric-val">4.2<span style="font-size:1.2rem">x</span></div>
              <div class="metric-sub">avg. across Hull clients</div>
              <div style="margin-top:.6rem;height:5px;background:var(--bdr);border-radius:99px"><div style="height:100%;width:85%;background:linear-gradient(90deg,var(--amber),var(--teal));border-radius:99px"></div></div>
            </div>
          </div>
          <div class="ai-status">
            <div class="ai-icon"><span class="ms">smart_toy</span></div>
            <div><div style="color:var(--white);font-weight:600;font-size:.88rem">AI Receptionist — Active</div><div style="color:#64748b;font-size:.75rem">5 calls handled today &middot; 0 missed</div></div>
            <div class="ai-live"><div class="dot-live"></div>LIVE</div>
          </div>
          <div class="loc-pill">
            <span style="display:flex;align-items:center;gap:.35rem;color:var(--white);font-size:.85rem;font-weight:600"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem">location_on</span>Hull, East Yorkshire</span>
            <span style="color:#64748b;font-size:.75rem">Covering HU1–HU17</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<div class="ticker-wrap"><div style="overflow:hidden"><div class="ticker-track">
<span class="ticker-item"><span class="ticker-dot"></span>Website Redesign</span>
<span class="ticker-item"><span class="ticker-dot"></span>Google Ads</span>
<span class="ticker-item"><span class="ticker-dot"></span>AI Receptionist</span>
<span class="ticker-item"><span class="ticker-dot"></span>Bespoke Backend Systems</span>
<span class="ticker-item"><span class="ticker-dot"></span>Facebook &amp; Instagram Ads</span>
<span class="ticker-item"><span class="ticker-dot"></span>Client Follow-Up Automation</span>
<span class="ticker-item"><span class="ticker-dot"></span>Local SEO</span>
<span class="ticker-item"><span class="ticker-dot"></span>Workflow Automation</span>
<span class="ticker-item"><span class="ticker-dot"></span>E-Commerce</span>
<span class="ticker-item"><span class="ticker-dot"></span>CRM Development</span>
<span class="ticker-item"><span class="ticker-dot"></span>Hull City Centre</span>
<span class="ticker-item"><span class="ticker-dot"></span>East Yorkshire</span>
<span class="ticker-item"><span class="ticker-dot"></span>Beverley</span>
<span class="ticker-item"><span class="ticker-dot"></span>Hessle &amp; Humber</span>
<span class="ticker-item"><span class="ticker-dot"></span>Website Redesign</span>
<span class="ticker-item"><span class="ticker-dot"></span>Google Ads</span>
<span class="ticker-item"><span class="ticker-dot"></span>AI Receptionist</span>
<span class="ticker-item"><span class="ticker-dot"></span>Bespoke Backend Systems</span>
<span class="ticker-item"><span class="ticker-dot"></span>Facebook &amp; Instagram Ads</span>
<span class="ticker-item"><span class="ticker-dot"></span>Client Follow-Up Automation</span>
<span class="ticker-item"><span class="ticker-dot"></span>Local SEO</span>
<span class="ticker-item"><span class="ticker-dot"></span>Workflow Automation</span>
<span class="ticker-item"><span class="ticker-dot"></span>E-Commerce</span>
<span class="ticker-item"><span class="ticker-dot"></span>CRM Development</span>
<span class="ticker-item"><span class="ticker-dot"></span>Hull City Centre</span>
<span class="ticker-item"><span class="ticker-dot"></span>East Yorkshire</span>
<span class="ticker-item"><span class="ticker-dot"></span>Beverley</span>
<span class="ticker-item"><span class="ticker-dot"></span>Hessle &amp; Humber</span>
</div></div></div>

<section class="section-sm" style="background:var(--bg)">
<div class="wrap">
<p style="text-align:center;color:#334155;font-size:.75rem;margin-bottom:1.75rem">Indicative averages across client base — your results will vary by sector and budget</p>
<div class="stats-grid rv">
  <div class="stat-card"><span class="stat-num grad-amber cs" data-t="287">0</span><span class="stat-unit grad-amber">%</span><span class="stat-label">More enquiries</span><span class="stat-sub">within 90 days, on average</span></div>
  <div class="stat-card"><span class="stat-num grad-amber cs" data-t="4">0</span><span class="stat-unit grad-amber">x</span><span class="stat-label">Return on ad spend</span><span class="stat-sub">Google &amp; Facebook average</span></div>
  <div class="stat-card"><span class="stat-num grad-teal cs" data-t="60">0</span><span class="stat-unit grad-teal">%</span><span class="stat-label">Admin time saved</span><span class="stat-sub">with AI automation</span></div>
  <div class="stat-card"><span class="stat-num grad-teal cs" data-t="14">0</span><span class="stat-label">Day turnaround</span><span class="stat-sub">average brief to live website</span></div>
</div>
</div>
</section>

<!-- TECH STACK MARQUEE -->
<div class="tech-stack rv">
  <div class="tech-track">
    <div class="tech-item"><span class="material-symbols-outlined">code</span>HTML5</div>
    <div class="tech-item"><span class="material-symbols-outlined">css</span>CSS3</div>
    <div class="tech-item"><span class="material-symbols-outlined">javascript</span>JavaScript</div>
    <div class="tech-item"><span class="material-symbols-outlined">database</span>Python</div>
    <div class="tech-item" style="gap:8px;background:rgba(255,255,255,0.05);padding:0.2rem 0.6rem;border-radius:6px">
      <img src="chatgpt_logo.png" style="height:20px;width:auto" alt="ChatGPT">
      <span style="color:#fff">ChatGPT</span>
    </div>
    <div class="tech-item"><span class="material-symbols-outlined">analytics</span>Google Ads</div>
    <div class="tech-item"><span class="material-symbols-outlined">campaign</span>Meta Ads</div>
    <div class="tech-item"><span class="material-symbols-outlined">shopping_cart</span>Shopify</div>
    <div class="tech-item"><span class="material-symbols-outlined">payments</span>Stripe</div>
    <!-- Duplicate for loop -->
    <div class="tech-item"><span class="material-symbols-outlined">code</span>HTML5</div>
    <div class="tech-item"><span class="material-symbols-outlined">css</span>CSS3</div>
    <div class="tech-item"><span class="material-symbols-outlined">javascript</span>JavaScript</div>
    <div class="tech-item"><span class="material-symbols-outlined">database</span>Python</div>
    <div class="tech-item" style="gap:8px;background:rgba(255,255,255,0.05);padding:0.2rem 0.6rem;border-radius:6px">
       <img src="chatgpt_logo.png" style="height:20px;width:auto" alt="ChatGPT">
       <span style="color:#fff">ChatGPT</span>
    </div>
  </div>
</div>

<section id="services" class="section rv" style="background:transparent;position:relative">
<div class="global-pat"></div>
<div class="ornament" style="top:0;right:0;background:radial-gradient(circle,rgba(14,165,233,.08),transparent 70%)"></div>
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">What We Do</div>
  <h2>Everything Your Hull Business<br/>Needs to Grow Online</h2>
  <p>We're your full digital partner — web design, advertising and AI automation under one Hull roof.</p>
</div>
<div class="services-grid stagger-load">
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.18)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">design_services</span></div><h3>Website Redesign</h3><p>Modern, fast, conversion-focused websites that make customers choose you over competitors.</p><a href="#services" class="svc-link" style="color:var(--amber)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">arrow_forward</span></a></div>
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(14,165,233,.08);border:1px solid rgba(14,165,233,.18)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal)">ads_click</span></div><h3>Google Ads</h3><p>Be first when Hull residents search for your service — targeted campaigns that bring real enquiries.</p><a href="#ads" class="svc-link" style="color:var(--teal)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal)">arrow_forward</span></a></div>
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.18)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">campaign</span></div><h3>Facebook &amp; Instagram Ads</h3><p>Scroll-stopping social ads targeting Hull postcodes by age, location and interest. Creative included.</p><a href="#ads" class="svc-link" style="color:var(--amber)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">arrow_forward</span></a></div>
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(14,165,233,.08);border:1px solid rgba(14,165,233,.18)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal)">travel_explore</span></div><h3>Local SEO</h3><p>Rank above Hull competitors on Google Maps and organic search. Own your local visibility.</p><a href="#services" class="svc-link" style="color:var(--teal)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal)">arrow_forward</span></a></div>
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.18)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">shopping_cart</span></div><h3>E-Commerce</h3><p>Professional online shops for Hull businesses — from independent retailers to trade suppliers.</p><a href="#contact" class="svc-link" style="color:var(--amber)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">arrow_forward</span></a></div>
<div class="card svc-card rv card-spot"><div class="svc-icon" style="background:rgba(245,166,35,.1);border:1px solid rgba(245,166,35,.25)"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">smart_toy</span></div><h3>AI Automation <span style="font-size:.65rem;padding:.2rem .5rem;border-radius:4px;background:var(--amber);color:#0a0a0a;font-weight:800;vertical-align:middle">NEW</span></h3><p>AI receptionist, automated follow-ups, bespoke backend systems — working for you around the clock.</p><a href="#ai" class="svc-link" style="color:var(--amber)">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber)">arrow_forward</span></a></div>
</div></div></section>

<section id="portfolio" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">Our Work</div>
  <h2>Real Website Transformations</h2>
  <p>Drag the line to compare. These are the results a proper redesign delivers for a Hull business.</p>
</div>
<div class="compare-wrap">
  <div class="compare-header">
    <div style="display:flex;align-items:center;gap:.85rem"><div class="compare-badge">01</div><div><div style="color:var(--white);font-weight:600;font-size:.9rem">Local Hull Trade Business</div><div style="color:#64748b;font-size:.78rem">Website redesign project</div></div></div>
    <div style="display:flex;gap:1.5rem;font-size:.78rem;flex-wrap:wrap"><span style="color:#64748b">Before: <strong style="color:#f87171">~3 enquiries/mo</strong></span><span style="color:#64748b">After: <strong style="color:#4ade80">~25 enquiries/mo</strong></span></div>
  </div>
  <div class="compare-stage">
    <div style="position:absolute;inset:0;background:#060a14;display:flex;flex-direction:column">
      <div style="background:#0b1220;padding:.65rem 1.5rem;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.07)">
        <div style="display:flex;align-items:center;gap:.5rem"><div style="width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#F5A623,#D97706);display:flex;align-items:center;justify-content:center;font-size:.9rem">&#9889;</div><span style="color:white;font-weight:800;font-size:.85rem;font-family:Syne,sans-serif">New High-Converting Site</span></div>
        <div style="display:flex;gap:1.5rem;align-items:center"><span style="color:#64748b;font-size:.7rem">Services</span><span style="color:#64748b;font-size:.7rem">Areas</span><span style="background:#F5A623;color:#0a0a0a;font-size:.7rem;font-weight:700;padding:.3rem .9rem;border-radius:7px">Get Quote</span></div>
      </div>
      <div style="flex:1;display:grid;grid-template-columns:1fr 1fr">
        <div style="padding:2rem;display:flex;flex-direction:column;justify-content:center;gap:.9rem">
          <div style="font-size:.6rem;color:#F5A623;text-transform:uppercase;letter-spacing:.2em;font-weight:700">Hull &amp; East Yorkshire</div>
          <div style="font-size:1.6rem;font-weight:900;color:white;font-family:Syne,sans-serif;line-height:1.15">Reliable<br/><span style="color:#F5A623">Local Experts.</span></div>
          <div style="font-size:.77rem;color:#64748b;line-height:1.75;max-width:28ch">Fully insured, local professionals. Free quotes and same-week appointments.</div>
          <div style="display:flex;gap:.75rem"><div style="background:#F5A623;color:#0a0a0a;font-size:.75rem;font-weight:700;padding:.55rem 1.25rem;border-radius:8px">Free Quote</div><div style="border:1px solid rgba(255,255,255,.1);color:#94a3b8;font-size:.75rem;padding:.55rem 1.25rem;border-radius:8px">Our Services</div></div>
          <div style="display:flex;gap:1rem"><span style="font-size:.65rem;color:#4ade80">&#10003; Fully Insured</span></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;padding:1.5rem;gap:.65rem;align-content:center">
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(245,166,35,.1)"><div style="color:#F5A623;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">24/7</div><div style="color:#475569;font-size:.6rem">Emergency</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(14,165,233,.1)"><div style="color:#38BDF8;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">Fast</div><div style="color:#475569;font-size:.6rem">Response</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(245,166,35,.1)"><div style="color:#F5A623;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">Fixed</div><div style="color:#475569;font-size:.6rem">Pricing</div></div>
          <div style="background:rgba(255,255,255,.05);border-radius:10px;padding:.9rem;text-align:center;border:1px solid rgba(14,165,233,.1)"><div style="color:#38BDF8;font-size:1rem;font-weight:800;font-family:Syne,sans-serif">5.0 &#9733;</div><div style="color:#475569;font-size:.6rem">Google</div></div>
        </div>
      </div>
    </div>
    <div style="position:absolute;top:10px;right:12px;background:var(--amber);color:#0a0a0a;padding:.25rem .75rem;border-radius:99px;font-size:.7rem;font-weight:800;z-index:5">AFTER &#9654;</div>
    <div id="bao1" style="position:absolute;inset:0;height:100%;overflow:hidden;border-right:3px solid var(--amber);z-index:10;width:50%">
      <div style="position:absolute;inset:0;min-width:200%">
        <div style="min-width:50%;background:#d0cbc0;font-family:Arial,sans-serif;height:100%">
          <div style="background:#1a3c6e;color:#ffd700;padding:.5rem 1rem;font-weight:bold;font-size:.72rem;display:flex;justify-content:space-between"><span>OLD WEBSITE</span><span style="color:white;font-size:.6rem">Est. 2005</span></div>
          <div style="background:#2a5fa8;display:flex"><span style="color:white;font-size:.62rem;font-weight:bold;padding:.35rem .75rem;background:rgba(255,255,255,.2)">Home</span><span style="color:#cce;font-size:.62rem;padding:.35rem .75rem">About</span><span style="color:#cce;font-size:.62rem;padding:.35rem .75rem">Services</span></div>
          <table style="width:100%;border-collapse:collapse;background:#ece8df"><tr><td style="width:155px;background:#c5bfb3;padding:.7rem;vertical-align:top;border-right:2px solid #aaa"><div style="background:white;padding:.45rem;margin-bottom:.5rem;border:1px solid #bbb;font-size:.6rem"><b style="font-size:.65rem">Welcome</b><br/>We offer local services. Call for quote.</div><div style="font-size:.58rem;line-height:2;color:#333"><b>Links:</b><br/>&#x25BA; Page 1<br/>&#x25BA; Page 2</div></td><td style="padding:.7rem;vertical-align:top"><div style="font-size:.6rem;color:#c00;font-weight:bold;margin-bottom:.45rem">Welcome to our site</div><div style="margin-top:.6rem;background:#fffbe6;border:1px solid #cc9900;padding:.35rem;font-size:.56rem;color:#555">Text heavy, hard to read content goes here.</div></td></tr></table>
        </div>
      </div>
      <div style="position:absolute;top:10px;left:10px;background:rgba(10,10,10,.9);color:#f87171;padding:.25rem .75rem;border-radius:99px;font-size:.7rem;font-weight:800;pointer-events:none">&#9664; BEFORE</div>
    </div>
    <input type="range" min="0" max="100" value="50" class="compare-range" oninput="document.getElementById('bao1').style.width=this.value+'%';document.getElementById('bah1').style.left=this.value+'%'"/>
    <div id="bah1" class="compare-handle"><div class="compare-handle-circle"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:#0a0a0a;font-size:1.2rem">swap_horiz</span></div></div>
  </div>
</div>
<script>
// Prevent drag issues on touch
document.querySelectorAll('.compare-range').forEach(r=>{
  r.addEventListener('touchstart',e=>e.stopPropagation(),{passive:true});
});
</script>
<p style="text-align:center;color:#475569;font-size:.82rem;margin-top:1rem;display:flex;align-items:center;justify-content:center;gap:.4rem">
  <span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem">touch_app</span>Drag the handle to compare before &amp; after
</p>
</div>
</section>

<!-- RECENT PROJECTS -->
<section class="section rv" style="padding-top:0">
<div class="wrap">
  <div class="section-header" style="margin-bottom:2rem;text-align:left">
    <h3 style="font-size:1.5rem">Recent Live Projects</h3>
    <p style="margin:0;max-width:100%">A selection of work we've shipped for Hull clients recently.</p>
  </div>
  <div class="project-grid stagger-load">
    <div class="proj-card card-spot card" style="overflow:hidden">
      <div class="proj-img">
        <div class="proj-fallback"><span class="material-symbols-outlined ms">apartment</span><span>Property Agency</span></div>
        <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&q=80&w=800" alt="Property Agency" onerror="this.style.opacity='0'" style="position:relative;z-index:2">
      </div>
      <div class="proj-body">
        <span class="proj-tag">Property</span>
        <h4 style="font-size:1.1rem;margin-bottom:.5rem">Residential Property Agency</h4>
        <p style="font-size:.85rem;color:var(--txt)">Full rebrand and property listing backend for a leading local agency.</p>
      </div>
    </div>
    <div class="proj-card card-spot card" style="overflow:hidden">
      <div class="proj-img">
        <div class="proj-fallback"><span class="material-symbols-outlined ms">coffee</span><span>Coffee Subscription</span></div>
        <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&q=80&w=800" alt="Coffee Subscription" onerror="this.style.opacity='0'" style="position:relative;z-index:2">
      </div>
      <div class="proj-body">
        <span class="proj-tag">Hospitality</span>
        <h4 style="font-size:1.1rem;margin-bottom:.5rem">Coffee Subscription Service</h4>
        <p style="font-size:.85rem;color:var(--txt)">Subscription site with Stripe integration and local delivery automation.</p>
      </div>
    </div>
    <div class="proj-card card-spot card" style="overflow:hidden">
      <div class="proj-img">
        <div class="proj-fallback"><span class="material-symbols-outlined ms">fitness_center</span><span>Local Gym Portal</span></div>
        <img src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&q=80&w=800" alt="Local Gym Portal" onerror="this.style.opacity='0'" style="position:relative;z-index:2">
      </div>
      <div class="proj-body">
        <span class="proj-tag">Health</span>
        <h4 style="font-size:1.1rem;margin-bottom:.5rem">Gym Membership Portal</h4>
        <p style="font-size:.85rem;color:var(--txt)">Member portal and class booking app for a premium independent gym.</p>
      </div>
    </div>
  </div>
</div>
</section>

<section id="ai" class="section rv" style="background:var(--bg2);position:relative">
<div class="ornament" style="bottom:10%;left:-100px;background:radial-gradient(circle,rgba(245,166,35,.08),transparent 70%);width:500px;height:500px"></div>
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem;background:rgba(14,165,233,.08);border-color:rgba(14,165,233,.2);color:var(--teal)"><span style="width:7px;height:7px;border-radius:50%;background:var(--teal);display:inline-block;animation:pulse-dot 2s infinite"></span>AI-Powered Services</div>
  <h2>AI Automation for <span class="grad-teal">Hull Businesses</span></h2>
  <p>Stop losing time to repetitive tasks. We build AI-powered systems that work around the clock — even when you're out on a job.</p>
</div>
<div class="ai-explainer">
<div>
  <h3 style="font-size:1.5rem;margin-bottom:1rem">What does AI automation actually mean for your business?</h3>
  <p style="max-width:42ch;margin-bottom:1rem;font-size:.93rem">Think of it as hiring a brilliant digital team member who never sleeps, never forgets, and costs a fraction of a salary. They answer calls, follow up with leads, send reminders and update your systems — automatically.</p>
  <p style="max-width:42ch;margin-bottom:1.5rem;font-size:.93rem">For a Hull tradesperson, that means never missing a call while on a job. For a Beverley clinic, it's appointment reminders sending themselves. For an East Yorkshire retailer, abandoned basket emails go out without you lifting a finger.</p>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Zero technical knowledge needed</strong><span>We build it, maintain it. You just use it.</span></div></div>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Built around your Hull business</strong><span>Not generic software — designed for how you operate.</span></div></div>
  <div class="ai-check"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.1rem;flex-shrink:0;margin-top:.1rem">check_circle</span><div><strong>Typically saves 10+ hours of admin per week</strong><span>Time better spent winning and doing work.</span></div></div>
</div>
<div class="ai-net-wrap">
<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 480 320" fill="none">
  <line x1="240" y1="160" x2="80" y2="75" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="400" y2="75" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="60" y2="215" stroke="rgba(245,166,35,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="420" y2="215" stroke="rgba(245,166,35,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="160" y2="295" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="240" y1="160" x2="320" y2="295" stroke="rgba(14,165,233,.18)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="2s" repeatCount="indefinite" path="M240,160 L80,75"/><animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(245,166,35,.9)"><animateMotion dur="2.5s" repeatCount="indefinite" path="M240,160 L420,215"/><animate attributeName="opacity" values="0;1;0" dur="2.5s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="1.8s" repeatCount="indefinite" path="M80,75 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="1.8s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(245,166,35,.9)"><animateMotion dur="3s" repeatCount="indefinite" path="M60,215 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle>
  <circle r="5" fill="rgba(14,165,233,.9)"><animateMotion dur="2.2s" repeatCount="indefinite" path="M160,295 L240,160"/><animate attributeName="opacity" values="0;1;0" dur="2.2s" repeatCount="indefinite"/></circle>
  <circle cx="240" cy="160" r="45" fill="rgba(14,165,233,.06)" stroke="rgba(14,165,233,.35)" stroke-width="1.5"/>
  <circle cx="240" cy="160" r="30" fill="rgba(14,165,233,.1)" stroke="rgba(14,165,233,.25)" stroke-width="1.5"/>
  <circle cx="240" cy="160" r="45" fill="none" stroke="rgba(14,165,233,.25)" stroke-width="1"><animate attributeName="r" values="45;62" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values=".3;0" dur="2s" repeatCount="indefinite"/></circle>
  <circle cx="80" cy="75" r="24" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.4)" stroke-width="1.5"/>
  <circle cx="400" cy="75" r="24" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.4)" stroke-width="1.5"/>
  <circle cx="60" cy="215" r="20" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.35)" stroke-width="1.5"/>
  <circle cx="420" cy="215" r="20" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.35)" stroke-width="1.5"/>
  <circle cx="160" cy="295" r="18" fill="rgba(245,166,35,.07)" stroke="rgba(245,166,35,.3)" stroke-width="1.5"/>
  <circle cx="320" cy="295" r="18" fill="rgba(14,165,233,.07)" stroke="rgba(14,165,233,.3)" stroke-width="1.5"/>
</svg>
<div style="position:relative;z-index:10;padding:1.75rem;display:flex;flex-direction:column;justify-content:space-between;min-height:320px">
  <div style="display:flex;justify-content:space-between"><div style="text-align:center;width:70px"><p style="color:var(--amber);font-size:.75rem;font-weight:700">Calls</p><p style="color:#334155;font-size:.68rem">AI answers</p></div><div style="text-align:center;width:70px"><p style="color:var(--teal);font-size:.75rem;font-weight:700">CRM</p><p style="color:#334155;font-size:.68rem">auto-updated</p></div></div>
  <div style="text-align:center"><div style="width:60px;height:60px;border-radius:1rem;background:linear-gradient(135deg,rgba(14,165,233,.18),rgba(245,166,35,.1));border:1px solid rgba(14,165,233,.4);display:flex;align-items:center;justify-content:center;margin:0 auto 8px"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.75rem">smart_toy</span></div><p style="color:var(--white);font-weight:700;font-size:.9rem">AI Hub</p><p style="color:#334155;font-size:.7rem;display:flex;align-items:center;justify-content:center;gap:.3rem;margin-top:.2rem"><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;animation:pulse-dot 1.5s infinite"></span>Always active</p></div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.5rem"><div style="text-align:center"><p style="color:var(--amber);font-size:.7rem;font-weight:700">Follow-ups</p><p style="color:#334155;font-size:.65rem">automated</p></div><div></div><div style="text-align:center"><p style="color:var(--teal);font-size:.7rem;font-weight:700">Bookings</p><p style="color:#334155;font-size:.65rem">auto-captured</p></div></div>
</div>
</div>
</div>
<div class="ai-cards">
<div class="card ai-card"><div class="ai-card-icon" style="background:rgba(14,165,233,.1);border:1px solid rgba(14,165,233,.2)"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.6rem">call</span></div><div><h3>AI Receptionist &amp; Call Handling</h3><p>Never miss an enquiry again. Our AI answers calls 24/7, collects customer details, handles FAQs and alerts you instantly.</p></div><ul class="ai-bullets"><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Covers nights, weekends, bank holidays and busy periods</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Learns your services, pricing and availability</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Sends you a call summary by text after every call</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Qualifies leads so you focus on real opportunities</li></ul><a href="#contact" class="ai-cta" style="background:rgba(14,165,233,.2);border-color:rgba(14,165,233,.35);color:var(--teal)">Enquire<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem">arrow_forward</span></a></div>
<div class="card ai-card"><div class="ai-card-icon" style="background:rgba(245,166,35,.1);border:1px solid rgba(245,166,35,.2)"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1.6rem">mark_email_read</span></div><div><h3>Automated Client Follow-Up</h3><p>Most businesses lose customers by forgetting to follow up. Our system sends the right message at the right time — automatically.</p></div><ul class="ai-bullets"><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Quote follow-ups at 24hrs, 3 days and 1 week — email &amp; SMS</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Post-job review requests to build your Google rating</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Re-engagement sequences for cold leads and past customers</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Personalised with customer names and enquiry details</li></ul><a href="#contact" class="ai-cta" style="background:rgba(245,166,35,.15);border-color:rgba(245,166,35,.3);color:var(--amber)">Enquire<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem">arrow_forward</span></a></div>
<div class="card ai-card"><div class="ai-card-icon" style="background:rgba(14,165,233,.1);border:1px solid rgba(14,165,233,.2)"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1.6rem">account_tree</span></div><div><h3>Business Workflow Automation</h3><p>We map how your business works, then automate the repetitive handoffs — from first enquiry to completed job.</p></div><ul class="ai-bullets"><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Booking confirmations and appointment reminders automated</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Automatic quote generation from enquiry form submissions</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Connects to WhatsApp, email, Google Sheets and more</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Saves an average of 10+ hours of admin every week</li></ul><a href="#contact" class="ai-cta" style="background:rgba(14,165,233,.2);border-color:rgba(14,165,233,.35);color:var(--teal)">Enquire<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem">arrow_forward</span></a></div>
<div class="card ai-card"><div class="ai-card-icon" style="background:rgba(245,166,35,.1);border:1px solid rgba(245,166,35,.22)"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1.6rem">developer_board</span></div><div><h3>Bespoke Backend Systems</h3><p>Custom dashboards, CRM systems, job management portals and client portals — built precisely around how your Hull business operates.</p></div><ul class="ai-bullets"><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Custom CRM — every customer, quote, job and invoice in one place</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Job management portals for Hull trade &amp; service businesses</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Live reporting dashboards — see performance at a glance</li><li><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:.95rem;flex-shrink:0;margin-top:.15rem">verified</span>Client portals — customers book, pay and track online</li></ul><a href="#contact" class="ai-cta" style="background:rgba(245,166,35,.18);border-color:rgba(245,166,35,.35);color:var(--amber)">Enquire<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem">arrow_forward</span></a></div>
</div></div></section>

<section id="ads" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">Paid Advertising</div>
  <h2>Ads That Bring Real Customers</h2>
  <p>We manage everything — strategy, creative, targeting and reporting. You just watch the enquiries come in.</p>
</div>
<div class="ads-grid stagger-load">

<!-- Google -->
<div class="ad-card card-spot">
  <div style="display:flex;align-items:center;gap:.75rem">
    <svg width="32" height="32" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
    <h3>Google Ads</h3>
  </div>
  <p>Be first when Hull residents search for your service. We make sure your business appears at the very top — above your competitors.</p>
  <ul class="ad-bullets">
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Targeted to Hull, Beverley, Hessle &amp; East Yorkshire only</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Search campaigns built and continuously optimised</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Plain-English monthly reporting — no jargon</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Average 4x return on ad spend across our clients</li>
  </ul>
  <div class="ad-preview">
    <div class="ad-preview-label">How you appear in Google</div>
    <div class="search-result" style="border-color:rgba(245,166,35,.2);background:rgba(245,166,35,.03)">
      <div class="sr-top"><span class="sr-badge">Ad</span><span class="sr-domain">yourbusiness.co.uk</span></div>
      <div class="sr-title">Hull [Your Trade] — Free Quote Today</div>
      <div class="sr-desc">Local, reliable &amp; insured. Serving Hull &amp; East Yorkshire. &#9733;&#9733;&#9733;&#9733;&#9733;</div>
    </div>
    <div class="search-result" style="border-color:var(--bdr);opacity:.3">
      <span class="sr-domain">competitor.co.uk</span>
      <div class="sr-desc">Hull trade services and repairs...</div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin-top:.75rem">
      <div style="text-align:center;background:var(--bg2);border-radius:.6rem;padding:.6rem"><div style="color:var(--amber);font-weight:800;font-size:1rem;font-family:Syne,sans-serif">4x</div><div style="color:#475569;font-size:.65rem">avg ROI</div></div>
      <div style="text-align:center;background:var(--bg2);border-radius:.6rem;padding:.6rem"><div style="color:var(--amber);font-weight:800;font-size:1rem;font-family:Syne,sans-serif">£1.40</div><div style="color:#475569;font-size:.65rem">avg/click</div></div>
      <div style="text-align:center;background:var(--bg2);border-radius:.6rem;padding:.6rem"><div style="color:var(--amber);font-weight:800;font-size:1rem;font-family:Syne,sans-serif">4.8%</div><div style="color:#475569;font-size:.65rem">click rate</div></div>
    </div>
    <p style="color:#334155;font-size:.7rem;text-align:center;margin-top:.4rem">*Average figures, your results will vary</p>
  </div>
  <a href="#contact" class="btn-primary">Enquire About Google Ads<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400">ads_click</span></a>
</div>

<!-- Facebook -->
<div class="ad-card card-spot">
  <div style="display:flex;align-items:center;gap:.75rem">
    <svg width="32" height="32" viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
    <h3>Facebook &amp; Instagram Ads</h3>
  </div>
  <p>Reach the right Hull residents where they spend their time online. Precisely targeted campaigns with creative included.</p>
  <ul class="ad-bullets">
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Postcode targeting — HU1 through to HU17 and beyond</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Ad images and copy written for you as part of the service</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Retargeting — re-engage website visitors who didn't enquire</li>
    <li><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--teal);font-size:1rem;flex-shrink:0;margin-top:.1rem">check_circle</span>Typical 3–5x return for Hull service and product businesses</li>
  </ul>
  <div class="ad-preview">
    <div class="ad-preview-label">Sample Ad Preview</div>
    <div class="fb-mock">
      <div class="fb-top">
        <div class="fb-av">YB</div>
        <div><div style="color:white;font-size:.72rem;font-weight:600">Your Hull Business</div><div style="color:#64748b;font-size:.65rem">Sponsored · Hull, East Yorkshire</div></div>
      </div>
      <div class="fb-body"><p style="color:#d1d5db;font-size:.72rem;line-height:1.5">Looking for a reliable local service in Hull? Free quotes · Fast response · Fully insured.</p></div>
      <div class="fb-img"><p style="color:var(--amber);font-weight:900;font-size:.9rem;font-family:Syne,sans-serif">FREE QUOTE · HULL &amp; EAST YORKS</p></div>
      <div class="fb-footer"><p style="color:white;font-size:.72rem;font-weight:600">Get Your Free Quote</p><span class="fb-btn">Learn More</span></div>
    </div>
  </div>
  <a href="#contact" class="btn-primary" style="background:#1877F2;box-shadow:none">Enquire About Social Ads<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400">campaign</span></a>
</div>
</div>
</div>
</section>

<section class="section-sm rv" style="background:var(--bg2)">
<div class="wrap">
<div class="section-header">
  <h2>How We Work</h2>
  <p>Simple, transparent and built around you — no jargon, no surprises.</p>
</div>
<div class="process-grid stagger-load">
<div class="proc-card card-spot"><div class="proc-num">1</div><span class="proc-icon ms">search</span><h3>Free Consultation</h3><p>We understand your goals and business — completely free, zero obligation.</p></div>
<div class="proc-card card-spot"><div class="proc-num">2</div><span class="proc-icon ms">description</span><h3>Bespoke Proposal</h3><p>A clear plan with exact deliverables and honest costs. No hidden fees.</p></div>
<div class="proc-card card-spot"><div class="proc-num">3</div><span class="proc-icon ms">build</span><h3>We Build It</h3><p>Our team gets to work. Regular check-ins and feedback throughout.</p></div>
<div class="proc-card card-spot"><div class="proc-num">4</div><span class="proc-icon ms">rocket_launch</span><h3>Launch &amp; Grow</h3><p>You go live. For ads, we track and optimise from day one.</p></div>
</div></div></section>

<section id="faq" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">FAQ</div>
  <h2>Common Questions</h2>
  <p>Honest answers from a Hull digital agency.</p>
</div>
<div class="faq-list">
<details class="faq"><summary>How much does a website cost?<span class="chevron ms">expand_more</span></summary><div class="faq-body">Every project is different, so we don't list generic prices — we give a tailored quote after understanding what you actually need. Reach out and we'll give you an honest ballpark the same day, completely free.</div></details>
<details class="faq"><summary>How long does a new website take?<span class="chevron ms">expand_more</span></summary><div class="faq-body">Most straightforward websites take 10–14 working days from confirmed brief to going live. E-commerce or bespoke projects take 4–6 weeks. You'll get an accurate timeline in your proposal, and we stick to it.</div></details>
<details class="faq"><summary>Do you work with businesses outside Hull city centre?<span class="chevron ms">expand_more</span></summary><div class="faq-body">Absolutely. We work across all of East Yorkshire — Beverley, Hessle, Cottingham, Brough, Bridlington, Goole and everything in between. We can meet in person or work entirely remotely.</div></details>
<details class="faq"><summary>Is AI automation complicated for me to use?<span class="chevron ms">expand_more</span></summary><div class="faq-body">Not at all from your side. We handle everything technical. You'll have a couple of conversations about how your business runs, then we build and test everything. By the time you see it, it simply works.</div></details>
<details class="faq"><summary>What budget do I need for Google Ads?<span class="chevron ms">expand_more</span></summary><div class="faq-body">You set a monthly budget that goes direct to Google — we recommend starting from £200–300/month for local Hull campaigns. We charge a management fee on top. You pay per click, and we track every penny with monthly reports.</div></details>
<details class="faq"><summary>Can I try ads before committing long-term?<span class="chevron ms">expand_more</span></summary><div class="faq-body">Yes — we recommend a 3-month test period, which is enough time to see meaningful data and optimise properly. No long tie-in contracts beyond that.</div></details>
<details class="faq"><summary>What is a Bespoke Backend System?<span class="chevron ms">expand_more</span></summary><div class="faq-body">It's custom software built specifically for your business — for example, a dashboard showing all your jobs, quotes, customers and invoices in one place. Designed around exactly how you work, not generic off-the-shelf software.</div></details>
</div></div></section>

<section id="contact" class="section rv" style="background:var(--bg3);position:relative;overflow:hidden">
<div class="ornament" style="top:50%;left:50%;transform:translate(-50%,-50%);width:800px;height:800px;background:radial-gradient(circle,rgba(14,165,233,.04),transparent 70%)"></div>
<div class="wrap">
<div class="contact-grid">
<div class="contact-info">
  <div class="accent-line"></div>
  <div class="label-pill" style="margin-bottom:.75rem">Get in Touch</div>
  <h2>Let's Grow Your<br/>Hull Business</h2>
  <p>Tell us about your business and goals. We'll come back with honest advice and a no-obligation quote.</p>
  <a href="mailto:hello@hullwebfixers.co.uk" class="contact-link">
    <div class="icon-wrap"><span class="ms">mail</span></div>
    <div><strong>hello@hullwebfixers.co.uk</strong><small>Email us anytime</small></div>
  </a>
  <div class="map-box">
    <svg viewBox="0 0 300 110" fill="none" width="100%">
      <path d="M0 55 Q75 38 150 50 Q225 65 300 38" stroke="rgba(14,165,233,.22)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <path d="M0 55 Q75 38 150 50 Q225 65 300 38" stroke="rgba(14,165,233,.1)" stroke-width="28" fill="none" stroke-linecap="round"/>
      <circle cx="138" cy="47" r="9" fill="var(--amber)" opacity=".9"/>
      <circle cx="138" cy="47" r="16" fill="var(--amber)" opacity=".14"/>
      <circle cx="138" cy="47" r="23" fill="var(--amber)" opacity=".06"/>
      <line x1="98" y1="22" x2="98" y2="82" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/>
      <line x1="108" y1="22" x2="108" y2="82" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/>
      <path d="M98 25 Q103 12 108 25" stroke="rgba(245,166,35,.4)" stroke-width="1.5" fill="none"/>
      <text x="143" y="44" fill="#F5A623" font-size="7.5" font-family="Syne,sans-serif" font-weight="700">HULL</text>
      <text x="55" y="33" fill="#475569" font-size="6">Humber</text>
      <text x="195" y="65" fill="#475569" font-size="6">Estuary</text>
      <text x="63" y="70" fill="#475569" font-size="5.5">Humber Bridge</text>
      <circle cx="182" cy="35" r="3" fill="#334155"/>
      <text x="187" y="36" fill="#475569" font-size="5.5">Beverley</text>
      <circle cx="112" cy="70" r="3" fill="#334155"/>
      <text x="117" y="73" fill="#475569" font-size="5.5">Hessle</text>
    </svg>
    <p style="text-align:center;font-size:.72rem;color:#334155;margin-top:.3rem">Serving Hull HU1–HU17 and all of East Yorkshire</p>
  </div>
</div>
<div class="contact-form">
  <h3>Send an Enquiry</h3>
  <p>Fill in the form and we'll get back with advice and a no-obligation quote.</p>
  <form action="https://formspree.io/f/mlgwwjyn" method="POST">
    <!-- Honeypot -->
    <div style="position:absolute;left:-9999px;top:-9999px;opacity:0;pointer-events:none" aria-hidden="true">
      <label for="company_website">Company website (leave blank)</label>
      <input type="text" id="company_website" name="_gotcha" tabindex="-1" autocomplete="off"/>
    </div>
    <div class="form-row" style="margin-bottom:1rem">
      <div class="form-field"><label for="name">Your Name *</label><input id="name" name="name" type="text" placeholder="John Smith" required class="fi" autocomplete="name"/></div>
      <div class="form-field"><label for="email">Email Address *</label><input id="email" name="email" type="email" placeholder="john@business.co.uk" required class="fi" autocomplete="email"/></div>
    </div>
    <div class="form-field" style="margin-bottom:1rem"><label for="business">Business Name</label><input id="business" name="business" type="text" placeholder="Your Business Ltd" class="fi" autocomplete="organization"/></div>
    <div class="form-field" style="margin-bottom:1rem">
      <label for="service">I'm Interested In... *</label>
      <select id="service" name="service" required class="fi">
        <option value="">Select a service...</option>
        <option>Website Redesign / Rebuild</option>
        <option>Google Ads Management</option>
        <option>Facebook &amp; Instagram Ads</option>
        <option>AI Receptionist</option>
        <option>Automated Client Follow-Up</option>
        <option>Business Workflow Automation</option>
        <option>Bespoke Backend System / CRM</option>
        <option>Local SEO</option>
        <option>E-Commerce Setup</option>
        <option>Not sure — need advice</option>
      </select>
    </div>
    <div class="form-field" style="margin-bottom:1rem">
      <label for="message">About Your Business &amp; Goals *</label>
      <textarea id="message" name="message" rows="4" required placeholder="e.g. We're a Hull-based trade business looking for more enquiries from Google..." class="fi" style="resize:vertical"></textarea>
    </div>
    <input type="hidden" name="_subject" value="New enquiry from hullwebfixers.co.uk"/>
    <button type="submit" class="form-submit">Send Enquiry<span class="ms">send</span></button>
  </form>
</div>
</div>
</div>
</section>

<!-- FOOTER -->
<footer class="footer">
<div class="wrap">
  <div class="hull-banner">
    <svg viewBox="0 0 1440 64" preserveAspectRatio="xMidYMax slice" fill="none" style="opacity:.12">
      <rect x="200" y="4" width="8" height="60" fill="#F5A623"/>
      <rect x="1232" y="4" width="8" height="60" fill="#F5A623"/>
      <path d="M204 5 Q720 -6 1234 5" stroke="#F5A623" stroke-width="2" fill="none"/>
      <line x1="204" y1="5" x2="100" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="204" y1="5" x2="280" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="204" y1="5" x2="450" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="204" y1="5" x2="620" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="1234" y1="5" x2="820" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="1234" y1="5" x2="980" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="1234" y1="5" x2="1150" y2="64" stroke="#F5A623" stroke-width=".7"/>
      <line x1="1234" y1="5" x2="1340" y2="64" stroke="#F5A623" stroke-width=".7"/>
    </svg>
    <div class="hull-banner-text"><p><i class="kcom-box"></i>Proudly built and based in Hull, East Yorkshire</p></div>
  </div>
  <div class="footer-inner">
    <div>
      <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1rem">
        <svg width="32" height="32" viewBox="0 0 40 40" fill="none">
          <rect width="40" height="40" rx="8" fill="#F5A623"/>
          <path d="M10 20L18 28L30 14" stroke="#0a0a0a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <p style="font-size:.85rem;color:#475569;max-width:28ch;line-height:1.7">Hull's digital growth agency — web design, AI automation and paid advertising.</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul><li><a href="#services">Website Redesign</a></li><li><a href="#ads">Google Ads</a></li><li><a href="#ads">Facebook &amp; Instagram Ads</a></li><li><a href="#ai">AI Receptionist</a></li><li><a href="#ai">Workflow Automation</a></li><li><a href="#ai">Bespoke CRM &amp; Systems</a></li><li><a href="#services">Local SEO</a></li></ul>
    </div>
    <div>
      <h4>Areas We Cover</h4>
      <ul><li>Hull City Centre</li><li>Beverley &amp; East Riding</li><li>Hessle &amp; Swanland</li><li>Cottingham</li><li>Brough &amp; Elloughton</li><li>Bridlington</li><li>Goole &amp; Surrounding Areas</li></ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li style="display:flex;align-items:flex-start;gap:.5rem"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem;flex-shrink:0;margin-top:.05rem">location_on</span>Hull, East Yorkshire, HU1</li>
        <li style="display:flex;align-items:center;gap:.5rem"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:var(--amber);font-size:1rem">mail</span><a href="mailto:hello@hullwebfixers.co.uk">hello@hullwebfixers.co.uk</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2025 Hull Web Fixers. All rights reserved. Built in Hull, East Yorkshire.</p>
    <div class="footer-links"><a href="#">Privacy Policy</a><a href="#">Terms</a></div>
  </div>
</div>
</footer>

<!-- GDPR Cookie -->
<div id="cookie-bar" role="dialog" aria-label="Cookie consent" style="
  position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%);
  max-width:640px;width:calc(100% - 2rem);
  background:#0b1220;border:1px solid rgba(245,166,35,.25);
  border-radius:1.25rem;padding:1.25rem 1.5rem;
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;
  z-index:9998;box-shadow:0 24px 64px rgba(0,0,0,.7);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
">
  <div style="display:flex;align-items:flex-start;gap:.75rem;flex:1;min-width:0">
    <span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:#F5A623;font-size:1.3rem;flex-shrink:0;margin-top:.05rem">cookie</span>
    <div>
      <p style="color:#f1f5f9;font-weight:700;font-size:.88rem;margin-bottom:.2rem">We use cookies</p>
      <p style="color:#64748b;font-size:.78rem;line-height:1.55">We use essential cookies to make this site work. No tracking or marketing cookies are set without your consent. By clicking Accept, you agree to our <a href="#" style="color:#F5A623;text-decoration:underline">Privacy Policy</a>.</p>
    </div>
  </div>
  <div style="display:flex;gap:.6rem;flex-shrink:0">
    <button onclick="decCookies()" style="background:transparent;border:1px solid rgba(255,255,255,.12);color:#94a3b8;font-size:.8rem;font-weight:600;padding:.5rem 1.1rem;border-radius:.7rem;cursor:pointer;white-space:nowrap;font-family:'Inter',sans-serif">Decline</button>
    <button onclick="accCookies()" style="background:#F5A623;border:none;color:#0a0a0a;font-size:.8rem;font-weight:800;padding:.5rem 1.25rem;border-radius:.7rem;cursor:pointer;white-space:nowrap;font-family:'Syne',sans-serif">Accept</button>
  </div>
</div>

<script>
window.addEventListener('scroll',()=>{
  const s=document.documentElement;
  document.getElementById('prog').style.width=((s.scrollTop/(s.scrollHeight-s.clientHeight))*100)+'%';
});
window.addEventListener('scroll',()=>{
  document.querySelector('.navbar').style.background=window.scrollY>60?'rgba(6,10,20,.98)':'rgba(6,10,20,.92)';
});
function toggleMob(){
  document.getElementById('mob-menu').classList.toggle('open');
  document.getElementById('hmb').classList.toggle('open');
}
function closeMob(){
  document.getElementById('mob-menu').classList.remove('open');
  document.getElementById('hmb').classList.remove('open');
}
(function(){
  const words=['We Grow.','We Automate.','We Deliver.','We Get Results.'];
  let wi=0,ci=0,del=false,pausing=false;
  const el=document.getElementById('twt');
  if(!el)return;
  function type(){
    if(pausing)return;
    const w=words[wi];
    if(!del){
      el.textContent=w.slice(0,++ci);
      if(ci===w.length){del=true;pausing=true;setTimeout(()=>{pausing=false;type();},2200);return;}
    }else{
      el.textContent=w.slice(0,--ci);
      if(ci===0){del=false;wi=(wi+1)%words.length;}
    }
    setTimeout(type,del?50:110);
  }
  setTimeout(type,800);
})();
(function(){
  const c=document.getElementById('pcv');
  if(!c)return;
  const ctx=c.getContext('2d');
  let pts=[];
  function resize(){c.width=c.offsetWidth;c.height=c.offsetHeight;init();}
  function init(){
    pts=[];
    const n=Math.max(20,Math.floor(c.width*c.height/14000));
    for(let i=0;i<n;i++)pts.push({x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,r:Math.random()*1.5+.4,a:Math.random()*.25+.06,col:Math.random()>.5?'245,166,35':'14,165,233'});
  }
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    pts.forEach(p=>{
      p.x+=p.vx;p.y+=p.vy;
      if(p.x<0||p.x>c.width)p.vx*=-1;
      if(p.y<0||p.y>c.height)p.vy*=-1;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle='rgba('+p.col+','+p.a+')';ctx.fill();
    });
    pts.forEach((a,i)=>{
      for(let j=i+1;j<pts.length;j++){
        const b=pts[j],d=Math.hypot(a.x-b.x,a.y-b.y);
        if(d<120){ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle='rgba(245,166,35,'+(0.045*(1-d/120))+')';ctx.lineWidth=.5;ctx.stroke();}
      }
    });
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize',resize);
  resize();draw();
})();
const ro=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('vis');}),{threshold:.06,rootMargin:'0px 0px -24px 0px'});
document.querySelectorAll('.rv, .stagger-load').forEach(el=>ro.observe(el));
document.querySelectorAll('.card-spot').forEach(card=>{
  card.addEventListener('mousemove',e=>{
    const rect=card.getBoundingClientRect();
    const x=e.clientX-rect.left;
    const y=e.clientY-rect.top;
    card.style.setProperty('--x',x+'px');
    card.style.setProperty('--y',y+'px');
  });
});
const co=new IntersectionObserver(entries=>entries.forEach(e=>{
  if(e.isIntersecting){
    const el=e.target,t=+el.dataset.t,step=t/65;
    let c=0;
    const iv=setInterval(()=>{c=Math.min(c+step,t);el.textContent=Math.floor(c);if(c>=t)clearInterval(iv);},18);
    co.unobserve(el);
  }
}),{threshold:.6});
document.querySelectorAll('.cs').forEach(el=>co.observe(el));
(function(){if(localStorage.getItem('cookie_consent')){document.getElementById('cookie-bar').style.display='none';}})();
function accCookies(){localStorage.setItem('cookie_consent','accepted');document.getElementById('cookie-bar').style.display='none';}
function decCookies(){localStorage.setItem('cookie_consent','declined');document.getElementById('cookie-bar').style.display='none';}
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("- index.html written ({} bytes)".format(len(html)))

# 2. Setup logo
logo_src = "ChatGPT Image Feb 19, 2026, 11_43_56 PM.png"
logo_dst = "logo.png"

if os.path.exists(logo_src):
    try:
        shutil.copy(logo_src, logo_dst)
        print("- Logo copied to {}".format(logo_dst))
    except Exception as e:
        print("- Warning: Could not copy logo: {}".format(e))
else:
    if not os.path.exists(logo_dst):
        print("- Warning: Source logo '{}' not found and '{}' missing.".format(logo_src, logo_dst))
    else:
        print("- Logo '{}' already exists.".format(logo_dst))

print("\nSUCCESS! Website is ready.")
print("Open index.html in your browser to view.")
