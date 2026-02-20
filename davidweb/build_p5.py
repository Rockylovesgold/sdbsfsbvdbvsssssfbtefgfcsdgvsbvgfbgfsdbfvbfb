f = open('index.html','a',encoding='utf-8')

# FAQ
f.write(r"""
<section id="faq" class="section rv" style="background:var(--bg)">
<div class="wrap">
<div class="section-header">
  <div class="accent-line" style="margin:0 auto"></div>
  <div class="label-pill" style="margin-bottom:.75rem">FAQ</div>
  <h2>Common Questions</h2>
  <p>Honest answers from a Hull digital agency.</p>
</div>
<div class="faq-list">
""")
faqs=[
    ("How much does a website cost?","Every project is different, so we don't list generic prices — we give a tailored quote after understanding what you actually need. Reach out and we'll give you an honest ballpark the same day, completely free."),
    ("How long does a new website take?","Most straightforward websites take 10–14 working days from confirmed brief to going live. E-commerce or bespoke projects take 4–6 weeks. You'll get an accurate timeline in your proposal, and we stick to it."),
    ("Do you work with businesses outside Hull city centre?","Absolutely. We work across all of East Yorkshire — Beverley, Hessle, Cottingham, Brough, Bridlington, Goole and everything in between. We can meet in person or work entirely remotely."),
    ("Is AI automation complicated for me to use?","Not at all from your side. We handle everything technical. You'll have a couple of conversations about how your business runs, then we build and test everything. By the time you see it, it simply works."),
    ("What budget do I need for Google Ads?","You set a monthly budget that goes direct to Google — we recommend starting from £200–300/month for local Hull campaigns. We charge a management fee on top. You pay per click, and we track every penny with monthly reports."),
    ("Can I try ads before committing long-term?","Yes — we recommend a 3-month test period, which is enough time to see meaningful data and optimise properly. No long tie-in contracts beyond that."),
    ("What is a Bespoke Backend System?","It's custom software built specifically for your business — for example, a dashboard showing all your jobs, quotes, customers and invoices in one place. Designed around exactly how you work, not generic off-the-shelf software."),
]
for q,a in faqs:
    f.write(f'<details class="faq"><summary>{q}<span class="chevron ms">expand_more</span></summary><div class="faq-body">{a}</div></details>\n')
f.write("</div></div></section>\n")

# CONTACT
f.write(r"""
<section id="contact" class="section rv" style="background:var(--bg2)">
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
    <svg viewBox="0 0 1440 64" preserveAspectRatio="none" fill="none" style="opacity:.12">
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
    <div class="hull-banner-text"><p><span class="ms">location_on</span>Proudly built and based in Hull, East Yorkshire</p></div>
  </div>
  <div class="footer-inner">
    <div>
      <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1rem"><img src="logo.png" alt="Hull Web Fixers" style="height:40px;width:auto"/></div>
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
document.querySelectorAll('.rv').forEach(el=>ro.observe(el));
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
""")
f.close()
print("built ok")
