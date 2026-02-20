"""
MASTER BUILD — writes the complete index.html with all sections + security applied.
Run once. Produces the full site.
"""
import re

HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Hull Web Fixers – Web Design, AI Automation &amp; Digital Ads</title>
<meta name="description" content="Hull's digital growth agency. Stunning websites, Google &amp; Facebook Ads, and AI automation for East Yorkshire businesses."/>
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
.btn-nav{background:var(--amber);color:#0a0a0a;font-weight:700;border:none;border-radius:.7rem;padding:.6rem 1.4rem;font-size:.85rem;cursor:pointer;transition:box-shadow .3s,transform .2s;white-space:nowrap;display:inline-block}
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
.btn-primary{display:inline-flex;align-items:center;gap:.5rem;background:var(--amber);color:#0a0a0a;font-weight:700;padding:.9rem 2rem;border-radius:var(--r);font-size:.95rem;transition:box-shadow .35s,transform .25s;white-space:nowrap;border:none;cursor:pointer;font-family:'Inter',sans-serif}
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
.section{padding:6rem 0}.section-sm{padding:4rem 0}
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
.svc-card{padding:2rem;display:flex;flex-direction:column}
.svc-icon{width:48px;height:48px;border-radius:.85rem;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;flex-shrink:0}
.svc-icon .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.5rem}
.svc-card h3{font-size:1.1rem;font-weight:700;margin-bottom:.6rem}
.svc-card p{font-size:.88rem;line-height:1.7;color:var(--txt);flex:1;max-width:34ch}
.svc-link{display:inline-flex;align-items:center;gap:.3rem;font-size:.82rem;font-weight:700;margin-top:1.25rem;transition:gap .25s}
.svc-link:hover{gap:.6rem}
.svc-link .ms{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1rem}
.compare-wrap{border:1px solid var(--bdr2);border-radius:1.5rem;overflow:hidden}
.compare-header{background:var(--bg2);padding:1rem 1.5rem;border-bottom:1px solid var(--bdr);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem}
.compare-badge{width:32px;height:32px;border-radius:.55rem;background:var(--amber);color:#0a0a0a;font-size:.75rem;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:'Syne',sans-serif}
.compare-stage{position:relative;height:380px;user-select:none}
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
@media(max-width:1100px){.hero-inner{grid-template-columns:1fr}.hero-card{max-width:540px}.stats-grid{grid-template-columns:repeat(2,1fr)}.ai-explainer{grid-template-columns:1fr}.contact-grid{grid-template-columns:1fr}.footer-inner{grid-template-columns:repeat(2,1fr)}}
@media(max-width:900px){.services-grid{grid-template-columns:repeat(2,1fr)}.ads-grid{grid-template-columns:1fr}.process-grid{grid-template-columns:repeat(2,1fr)}.ai-cards{grid-template-columns:1fr}}
@media(max-width:700px){.nav-links,.btn-nav{display:none}.hmb{display:flex}.services-grid{grid-template-columns:1fr}.process-grid{grid-template-columns:1fr 1fr}.stats-grid{grid-template-columns:1fr 1fr}.form-row{grid-template-columns:1fr}.footer-inner{grid-template-columns:1fr}}
@media(max-width:480px){.process-grid{grid-template-columns:1fr}.hero-copy h1{font-size:2.1rem}}
</style>
</head>
<body>
<div id="prog"></div>
<div id="mob-menu">
  <a href="#services" onclick="closeMob()">Services</a>
  <a href="#portfolio" onclick="closeMob()">Portfolio</a>
  <a href="#ai" onclick="closeMob()"><span class="nav-ai-dot"></span>AI Automation</a>
  <a href="#ads" onclick="closeMob()">Advertising</a>
  <a href="#contact" onclick="closeMob()">Contact</a>
  <a href="#contact" onclick="closeMob()" class="btn-mob pulse-anim">Get a Free Quote</a>
</div>
<nav class="navbar">
<div class="wrap navbar-inner">
  <a href="#" class="logo-wrap">
    <img src="logo.png" alt="Hull Web Fixers logo" class="logo-img"/>
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
"""

with open('index.html','w',encoding='utf-8') as f:
    f.write(HEAD)
print("p1 ok")
