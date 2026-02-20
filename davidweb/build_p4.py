f = open('index.html','a',encoding='utf-8')

# ADS SECTION
f.write(r"""
<section id="ads" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">Paid Advertising</div>
  <h2>Ads That Bring Real Customers</h2>
  <p>We manage everything — strategy, creative, targeting and reporting. You just watch the enquiries come in.</p>
</div>
<div class="ads-grid">

<!-- Google -->
<div class="ad-card">
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
<div class="ad-card">
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
""")

# PROCESS
f.write(r"""
<section class="section-sm rv" style="background:var(--bg2)">
<div class="wrap">
<div class="section-header">
  <h2>How We Work</h2>
  <p>Simple, transparent and built around you — no jargon, no surprises.</p>
</div>
<div class="process-grid">
""")
steps=[("search","1","Free Consultation","We understand your goals and business — completely free, zero obligation."),("description","2","Bespoke Proposal","A clear plan with exact deliverables and honest costs. No hidden fees."),("build","3","We Build It","Our team gets to work. Regular check-ins and feedback throughout."),("rocket_launch","4","Launch &amp; Grow","You go live. For ads, we track and optimise from day one.")]
for icon,num,title,desc in steps:
    f.write(f'<div class="proc-card"><div class="proc-num">{num}</div><span class="proc-icon ms">{icon}</span><h3>{title}</h3><p>{desc}</p></div>\n')
f.write("</div></div></section>\n")
f.close()
print("ads+process ok")
