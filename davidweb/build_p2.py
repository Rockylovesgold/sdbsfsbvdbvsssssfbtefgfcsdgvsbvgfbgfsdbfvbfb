f = open('index.html','a',encoding='utf-8')
f.write(r"""
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
        <div class="label-pill"><span style="width:7px;height:7px;border-radius:50%;background:#22c55e;display:inline-block;animation:pulse-dot 2s infinite"></span>Hull &amp; East Yorkshire's Digital Growth Team</div>
        <h1>We Build.<br/>We Automate.<br/><span class="grad-both" id="twt"></span><span class="cursor"></span></h1>
        <p>From stunning websites to AI automation and targeted advertising — we help Hull businesses grow faster, with less effort.</p>
        <div class="hero-btns">
          <a href="#contact" class="btn-primary pulse-anim">Get a Free Consultation<span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.1rem">arrow_outward</span></a>
          <a href="#ai" class="btn-secondary"><span style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;font-size:1.1rem;color:var(--amber)">smart_toy</span>Explore AI</a>
        </div>
        <div class="hero-trust">
          <span><span class="ms">verified</span>No-obligation quote</span>
          <span><span class="ms">location_on</span>Based in Hull, HU1</span>
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
""")

# TICKER
f.write('<div class="ticker-wrap"><div style="overflow:hidden"><div class="ticker-track">\n')
items=['Website Redesign','Google Ads','AI Receptionist','Bespoke Backend Systems','Facebook &amp; Instagram Ads','Client Follow-Up Automation','Local SEO','Workflow Automation','E-Commerce','CRM Development','Hull City Centre','East Yorkshire','Beverley','Hessle &amp; Humber']
for x in items*2:
    f.write(f'<span class="ticker-item"><span class="ticker-dot"></span>{x}</span>\n')
f.write("</div></div></div>\n")

# STATS
f.write(r"""
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
""")

# SERVICES
f.write(r"""
<section id="services" class="section rv" style="background:var(--bg2)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">What We Do</div>
  <h2>Everything Your Hull Business<br/>Needs to Grow Online</h2>
  <p>We're your full digital partner — web design, advertising and AI automation under one Hull roof.</p>
</div>
<div class="services-grid">
""")
svcs=[
  ('design_services','rgba(245,166,35,.08)','rgba(245,166,35,.18)','var(--amber)','#services','var(--amber)','Website Redesign','Modern, fast, conversion-focused websites that make customers choose you over competitors.'),
  ('ads_click','rgba(14,165,233,.08)','rgba(14,165,233,.18)','var(--teal)','#ads','var(--teal)','Google Ads','Be first when Hull residents search for your service — targeted campaigns that bring real enquiries.'),
  ('campaign','rgba(245,166,35,.08)','rgba(245,166,35,.18)','var(--amber)','#ads','var(--amber)','Facebook &amp; Instagram Ads','Scroll-stopping social ads targeting Hull postcodes by age, location and interest. Creative included.'),
  ('travel_explore','rgba(14,165,233,.08)','rgba(14,165,233,.18)','var(--teal)','#services','var(--teal)','Local SEO','Rank above Hull competitors on Google Maps and organic search. Own your local visibility.'),
  ('shopping_cart','rgba(245,166,35,.08)','rgba(245,166,35,.18)','var(--amber)','#contact','var(--amber)','E-Commerce','Professional online shops for Hull businesses — from independent retailers to trade suppliers.'),
  ('smart_toy','rgba(245,166,35,.1)','rgba(245,166,35,.25)','var(--amber)','#ai','var(--amber)','AI Automation <span style="font-size:.65rem;padding:.2rem .5rem;border-radius:4px;background:var(--amber);color:#0a0a0a;font-weight:800;vertical-align:middle">NEW</span>','AI receptionist, automated follow-ups, bespoke backend systems — working for you around the clock.'),
]
for icon,bg,bdr,clr,href,lclr,name,desc in svcs:
    f.write(f"""<div class="card svc-card rv"><div class="svc-icon" style="background:{bg};border:1px solid {bdr}"><span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:{clr}">{icon}</span></div><h3>{name}</h3><p>{desc}</p><a href="{href}" class="svc-link" style="color:{lclr}">Enquire<span class="ms" style="font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400;color:{lclr}">arrow_forward</span></a></div>\n""")
f.write("</div></div></section>\n")
f.close()
print("hero+ticker+stats+services ok")
