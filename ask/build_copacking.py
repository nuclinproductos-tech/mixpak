import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_start = html.find('<head>')
head_end = html.find('</head>') + 7
head = html[head_start:head_end]

nav_start = html.find('<nav class="nav" id="nav">')
nav_end = html.find('</nav>', html.find('</nav>', nav_start) + 1) + 6 # second nav
nav = html[nav_start:nav_end]

footer_start = html.find('<footer class="footer-unified">')
footer = html[footer_start:]

# Modify head for SEO
head = re.sub(r'<title>.*?</title>', '<title>Copacking Industrial | Envasado a Terceros — Mix Pak System</title>', head, flags=re.DOTALL)
head = re.sub(r'<meta name="description".*?>', '<meta name="description" content="Servicio de copacking industrial en España. Más de 30 líneas de envasado propias. Stick packs, sachets, doypacks y +50 formatos. Certificación IFS y GMP. Solicita presupuesto sin compromiso.">', head, flags=re.DOTALL)

seo_add = """  <link rel="canonical" href="https://mixpaksystem.com/copacking">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Copacking Industrial",
    "provider": {
      "@type": "Organization",
      "name": "Mix Pak System",
      "url": "https://mixpaksystem.com"
    },
    "description": "Servicio de copacking y envasado industrial a terceros con más de 30 líneas propias y certificación IFS y GMP",
    "areaServed": "España",
    "serviceType": "Copacking"
  }
  </script>
"""
head = head.replace('</head>', seo_add + '</head>')

# Ensure nav copacking link is active
nav = nav.replace('href="/copacking.html"', 'href="/copacking.html" class="nav-active"')

# Extracted envases HTML
envases_html = """
  <!-- ===================== FORMATOS ===================== -->
  <section class="env3" id="formatos" style="background:var(--bg); padding:100px 0;">
    <div class="container">

      <!-- 1. HEADER -->
      <div class="env3-header fi">
        <span class="label">Formatos disponibles</span>
        <h2 class="section-title" style="text-align:center;">Elige tu formato de envasado</h2>
        <p class="section-desc" style="max-width:560px;margin:0 auto;text-align:center;">Más de 50 formatos disponibles. Adaptamos cualquier solución a las necesidades de tu producto, dosis, material y mercado.</p>
      </div>

      <!-- 2. SHOWCASE -->
      <div class="env3-showcase fi">
        <!-- Stick Pack -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envase-stick.png" alt="Stick Pack" loading="lazy"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Stick Pack</h3><p class="env3-use">Monodosis de bolsillo, fácil apertura</p>
            <div class="env3-tags"><span>Polvos</span><span>Bebidas</span><span>Farmacia</span></div>
          </div>
        </div>
        <!-- Sachet -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envase-sachet.png" alt="Sachet" loading="lazy"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Sachet</h3><p class="env3-use">Sobre flexible para polvos y líquidos</p>
            <div class="env3-tags"><span>Suplementos</span><span>Cosmética</span><span>Alimentación</span></div>
          </div>
        </div>
        <!-- Flow Pack -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envase-flow-pack.png" alt="Flow Pack" loading="lazy" class="env3-img-wide"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Flow Pack</h3><p class="env3-use">Alta velocidad para sólidos y tabletas</p>
            <div class="env3-tags"><span>Snacks</span><span>Tablets</span><span>Higiene</span></div>
          </div>
        </div>
        <!-- Doypack -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envase-doypack.png" alt="Doypack" loading="lazy"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Doypack</h3><p class="env3-use">Bolsa de pie con zip, estable en lineal</p>
            <div class="env3-tags"><span>Proteínas</span><span>Snacks</span><span>Gran formato</span></div>
          </div>
        </div>
        <!-- Bote -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envases-botes.png" alt="Bote" loading="lazy"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Bote rígido</h3><p class="env3-use">PET/HDPE con tapa de rosca, percepción premium</p>
            <div class="env3-tags"><span>Suplementos</span><span>Farmacia</span><span>Nutrición</span></div>
          </div>
        </div>
        <!-- Tarro -->
        <div class="env3-item">
          <div class="env3-img-wrap"><img src="envases/envase-jar.png" alt="Tarro" loading="lazy" class="env3-img-sqr"></div>
          <div class="env3-item-body">
            <h3 class="env3-name">Tarro / Jar</h3><p class="env3-use">Envase premium de boca ancha para texturas densas</p>
            <div class="env3-tags"><span>Cosmética</span><span>Cremas</span><span>Polvos</span></div>
          </div>
        </div>
      </div>
      
      <!-- Special format CTA -->
      <div class="special-format-cta fi">
        <p class="special-title">¿No encuentras el formato que necesitas?</p>
        <p class="special-desc">Fabricamos formatos especiales y personalizados para proyectos con requerimientos específicos.</p>
        <a href="/contacto" class="btn-special">Consultar formato especial &rarr;</a>
      </div>
    </div>
  </section>
"""

custom_styles = """
  <style>
    /* HERO COPACKING */
    .cp-hero { height: 480px; position: relative; display: flex; align-items: center; justify-content: center; background: #000; text-align: center; }
    .cp-hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
    .cp-hero-overlay { position: absolute; inset: 0; background: rgba(6,12,36,0.75); }
    .cp-hero-content { position: relative; z-index: 2; padding: 0 24px; display: flex; flex-direction: column; align-items: center; margin-top: 60px; }
    .cp-breadcrumb { font-size: 0.72rem; color: rgba(255,255,255,0.45); margin-bottom: 24px; font-weight: 500; letter-spacing: 0.05em; }
    .cp-breadcrumb span { color: var(--gold); margin: 0 6px; }
    .cp-hero-label { font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--gold); margin-bottom: 16px; font-weight: 700; }
    .cp-hero h1 { font-family: 'DM Serif Display', serif; font-size: clamp(2.4rem, 4vw, 3.8rem); color: #fff; margin-bottom: 16px; line-height: 1.1; }
    .cp-hero-sub { font-family: 'Inter', sans-serif; font-weight: 300; font-size: 1.05rem; color: rgba(255,255,255,0.75); max-width: 640px; margin-bottom: 32px; line-height: 1.6; }
    .cp-hero-btns { display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
    .cp-btn-pri { background: var(--gold); color: var(--navy); font-weight: 700; padding: 14px 28px; border-radius: 100px; display: inline-block; transition: all 0.2s; font-size:0.95rem; }
    .cp-btn-pri:hover { background: var(--gold-dark); transform: translateY(-2px); }
    .cp-btn-sec { background: transparent; border: 1px solid rgba(255,255,255,0.4); color: #fff; font-weight: 600; padding: 14px 28px; border-radius: 100px; display: inline-block; transition: all 0.2s; font-size:0.95rem; }
    .cp-btn-sec:hover { background: rgba(255,255,255,0.1); border-color: #fff; }

    /* SECCION 2: INTRO */
    .cp-intro { background: var(--white); padding: 80px 0; }
    .cp-intro-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
    .cp-intro-text h2 { font-size: clamp(1.8rem, 2.8vw, 2.6rem); margin-bottom: 24px; }
    .cp-intro-text p { color: var(--text-muted); margin-bottom: 20px; font-size: 1.05rem; }
    .cp-intro-cta { display: inline-flex; align-items: center; color: var(--gold); font-weight: 600; margin-top: 12px; transition: color 0.2s; font-size: 0.95rem; }
    .cp-intro-cta:hover { color: var(--gold-dark); }
    .cp-stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .cp-stat { background: var(--bg); border-radius: var(--r); padding: 28px 24px; text-align: center; }
    .cp-stat-num { display: block; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 2rem; color: var(--navy); margin-bottom: 8px; line-height: 1; }
    .cp-stat-label { font-weight: 400; font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em; }

    /* FORMATOS CTA INFERIOR */
    .special-format-cta { background: var(--navy); padding: 48px; border-radius: var(--r); text-align: center; margin-top: 48px; }
    .special-title { font-family: 'Inter', sans-serif; font-weight: 500; font-size: 1.1rem; color: #fff; margin-bottom: 8px; }
    .special-desc { color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-bottom: 24px; }
    .btn-special { color: var(--gold); font-weight: 600; transition: opacity 0.2s; font-size: 0.95rem; }
    .btn-special:hover { opacity: 0.8; }

    /* CATALOGO ENVASES */
    .cp-catalogo { background: var(--white); padding: 80px 0; }
    .cp-cat-grid { display: grid; grid-template-columns: 45% 55%; gap: 64px; align-items: center; }
    .cp-cat-list { list-style: none; margin: 24px 0 32px; }
    .cp-cat-list li { position: relative; padding-left: 24px; margin-bottom: 12px; color: var(--text); font-size: 1.05rem; }
    .cp-cat-list li::before { content: "•"; position: absolute; left: 0; color: var(--gold); font-size: 1.2rem; line-height: 1; top: 2px; }
    .cp-cat-img img { width: 100%; border-radius: var(--r); object-fit: cover; box-shadow: var(--sh-lg); }

    /* PROCESO DE TRABAJO */
    .cp-proceso { background: var(--bg); padding: 100px 0; }
    .cp-proc-header { text-align: center; margin-bottom: 64px; }
    .cp-proc-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
    .cp-proc-card { background: var(--white); border: 1px solid var(--border); border-radius: var(--r); padding: 32px 28px; }
    .cp-proc-num { display: block; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 2.4rem; color: var(--gold); opacity: 0.4; margin-bottom: 16px; line-height: 1; }
    .cp-proc-card h3 { font-size: 1.3rem; margin-bottom: 12px; }
    .cp-proc-card p { font-size: 0.875rem; color: var(--text-muted); line-height: 1.7; }

    /* SECTORES PILLS */
    .cp-sectores { background: var(--white); padding: 80px 0; }
    .cp-sec-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 48px; }
    .cp-sec-pill { display: flex; align-items: center; gap: 12px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--r); padding: 20px 24px; transition: all 0.2s ease; }
    .cp-sec-pill:hover { border-color: var(--gold); transform: translateY(-2px); box-shadow: var(--sh); }
    .cp-sec-icon { flex-shrink: 0; stroke: var(--gold); stroke-width: 1.5; fill: none; }
    .cp-sec-name { font-weight: 500; font-size: 0.95rem; color: var(--navy); }
    .cp-sec-arr { margin-left: auto; color: var(--text-muted); font-weight: 400; font-size: 1.2rem; }

    /* FORM CTA */
    .cp-form-sec { background: var(--navy); padding: 100px 0; color: #fff; }
    .cp-form-grid { display: grid; grid-template-columns: 40% 60%; gap: 64px; align-items: flex-start; }
    .cp-form-text h2 { color: #fff; font-size: clamp(1.8rem, 3vw, 2.8rem); margin-bottom: 16px; }
    .cp-form-text p { color: rgba(255,255,255,0.65); margin-bottom: 32px; font-size: 1.05rem; }
    .cp-form-guarantees { list-style: none; }
    .cp-form-guarantees li { font-size: 0.875rem; color: rgba(255,255,255,0.75); margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
    .cp-form-guarantees li::before { content: "✓"; color: var(--gold); font-weight: bold; }
    .cp-form-box { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--r); padding: 40px 36px; }
    .cp-input-group { margin-bottom: 16px; }
    .cp-input { width: 100%; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 14px 16px; border-radius: 8px; font-family: 'Inter', sans-serif; font-size: 0.95rem; transition: border 0.2s; }
    .cp-input:focus { outline: none; border-color: var(--gold); }
    .cp-input::placeholder { color: rgba(255,255,255,0.4); }
    .cp-select { appearance: none; background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23FFFFFF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E"); background-repeat: no-repeat; background-position: right 16px top 50%; background-size: 10px auto; }
    .cp-input option { background: var(--navy); color: #fff; }
    .cp-check-wrap { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 24px; }
    .cp-check-wrap input { margin-top: 4px; }
    .cp-check-label { font-size: 0.78rem; color: rgba(255,255,255,0.5); line-height: 1.5; }
    .cp-submit { width: 100%; background: var(--gold); color: var(--navy); font-family: 'Inter', sans-serif; font-weight: 800; padding: 16px; border-radius: 100px; border: none; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; }
    .cp-submit:hover { background: var(--gold-dark); transform: translateY(-1px); }
    .cp-form-note { font-size: 0.72rem; color: rgba(255,255,255,0.35); text-align: center; margin-top: 16px; }

    @media (max-width: 1024px) {
      .cp-intro-grid, .cp-cat-grid, .cp-form-grid { grid-template-columns: 1fr; gap: 40px; }
      .cp-proc-grid { grid-template-columns: repeat(2, 1fr); }
      .cp-sec-grid { grid-template-columns: repeat(2, 1fr); }
      .cp-intro-text { order: 1; }
      .cp-stats-grid { order: 2; }
      .cp-cat-text { order: 1; }
      .cp-cat-img { order: 2; }
      .cp-form-text { order: 1; }
      .cp-form-box { order: 2; }
    }
    @media (max-width: 768px) {
      .cp-proc-grid { grid-template-columns: 1fr; }
      .cp-sec-grid { grid-template-columns: 1fr; }
      .cp-stats-grid { grid-template-columns: 1fr; }
      .cp-form-box { padding: 24px; }
    }
  </style>
"""

html_body = f"""
<body>
  {nav}

  <!-- SECCION 1: HERO -->
  <section class="cp-hero">
    <img src="IMG/servicios/copacking-linea.jpg" alt="Copacking Industrial" class="cp-hero-bg">
    <div class="cp-hero-overlay"></div>
    <div class="cp-hero-content fi">
      <div class="cp-breadcrumb">Inicio <span>›</span> Copacking</div>
      <div class="cp-hero-label">SERVICIO</div>
      <h1>Copacking industrial a medida</h1>
      <p class="cp-hero-sub">Envasamos tu producto con la tecnología, los formatos y los estándares de calidad que tu marca necesita.</p>
      <div class="cp-hero-btns">
        <a href="#contacto" class="cp-btn-pri">Solicitar presupuesto &rarr;</a>
        <a href="#formatos" class="cp-btn-sec">Ver formatos disponibles</a>
      </div>
    </div>
  </section>

  <!-- SECCION 2: INTRO -->
  <section class="cp-intro">
    <div class="container">
      <div class="cp-intro-grid">
        <div class="cp-intro-text fi">
          <span class="label">Qué es el copacking</span>
          <h2>Tu producto, nuestra tecnología,<br>tu marca en el mercado.</h2>
          <p>El copacking es la externalización completa del proceso de envasado. Tú aportas el producto o la fórmula, nosotros nos encargamos de envasarlo, acondicionarlo y entregarlo listo para distribución o venta, con todos los controles de calidad aplicados.</p>
          <p>En Mix Pak System trabajamos con más de 30 líneas de envasado propias, capaces de gestionar desde lotes piloto hasta producciones en serie de millones de unidades.</p>
          <a href="/empresa.html" class="cp-intro-cta">Ver nuestras instalaciones &rarr;</a>
        </div>
        <div class="cp-stats-grid fi">
          <div class="cp-stat"><span class="cp-stat-num">+30</span><span class="cp-stat-label">Líneas de envasado propias</span></div>
          <div class="cp-stat"><span class="cp-stat-num">+50</span><span class="cp-stat-label">Formatos disponibles</span></div>
          <div class="cp-stat"><span class="cp-stat-num">IFS · GMP</span><span class="cp-stat-label">Calidad certificada</span></div>
          <div class="cp-stat"><span class="cp-stat-num">Piloto</span><span class="cp-stat-label">Hasta gran serie</span></div>
        </div>
      </div>
    </div>
  </section>

  {envases_html}

  <!-- SECCION 4: CATALOGO -->
  <section class="cp-catalogo">
    <div class="container">
      <div class="cp-cat-grid">
        <div class="cp-cat-text fi">
          <span class="label">Nuestra capacidad</span>
          <h2>Si tiene forma, lo envasamos.</h2>
          <p>Desde el sachet monodosis más pequeño hasta el doypack de gran formato. Trabajamos con plástico flexible, aluminio, PET, HDPE, vidrio y materiales especiales con barrera activa.</p>
          <ul class="cp-cat-list">
            <li>Packaging flexible monocapa y multicapa</li>
            <li>Alta barrera contra O2 y humedad</li>
            <li>Materiales reciclables y sostenibles</li>
            <li>Envasado activo MAP y nitrógeno</li>
            <li>Termosellado, zipper y abre-fácil</li>
          </ul>
          <a href="/contacto?tipo=muestra" class="cp-intro-cta">Solicitar muestra de formato &rarr;</a>
        </div>
        <div class="cp-cat-img fi">
          <img src="IMG/formatos/catalogo-envases.jpg" alt="Catálogo completo de formatos de envasado Mix Pak System — más de 50 formatos disponibles">
        </div>
      </div>
    </div>
  </section>

  <!-- SECCION 5: PROCESO -->
  <section class="cp-proceso">
    <div class="container">
      <div class="cp-proc-header fi">
        <span class="label">Cómo trabajamos</span>
        <h2 class="section-title">De tu briefing al producto envasado</h2>
        <p class="section-desc" style="margin:0 auto">Un proceso claro, trazable y sin sorpresas.</p>
      </div>
      <div class="cp-proc-grid">
        <div class="cp-proc-card fi">
          <span class="cp-proc-num">01</span>
          <h3>Briefing y NDA</h3>
          <p>Firmamos acuerdo de confidencialidad antes de cualquier conversación técnica. Tu proyecto está protegido desde el primer día.</p>
        </div>
        <div class="cp-proc-card fi" style="transition-delay: 100ms">
          <span class="cp-proc-num">02</span>
          <h3>Selección de formato</h3>
          <p>Te asesoramos en la elección del formato óptimo para tu producto: material, barrera, sellado y presentación final.</p>
        </div>
        <div class="cp-proc-card fi" style="transition-delay: 200ms">
          <span class="cp-proc-num">03</span>
          <h3>Lote piloto</h3>
          <p>Producimos un lote de validación para verificar parámetros técnicos, rendimiento y calidad antes de la producción en serie.</p>
        </div>
        <div class="cp-proc-card fi" style="transition-delay: 300ms">
          <span class="cp-proc-num">04</span>
          <h3>Producción y entrega</h3>
          <p>Producción con trazabilidad lote a lote, control IFS y GMP, y entrega con documentación técnica completa.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECCION 6: SECTORES -->
  <section class="cp-sectores">
    <div class="container">
      <div class="cp-proc-header fi">
        <span class="label">Sectores</span>
        <h2 class="section-title" style="max-width:560px; margin:0 auto">Copacking especializado por industria</h2>
      </div>
      <div class="cp-sec-grid fi">
        <a href="/sectores/nutricion-deportiva" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          <span class="cp-sec-name">Nutrición deportiva</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
        <a href="/sectores/complementos-alimenticios" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
          <span class="cp-sec-name">Complementos alimenticios</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
        <a href="/sectores/cosmetica" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="6.5"/></svg>
          <span class="cp-sec-name">Cosmética</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
        <a href="/sectores/alimentacion-funcional" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
          <span class="cp-sec-name">Alimentación funcional</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
        <a href="/sectores/higiene" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span class="cp-sec-name">Higiene</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
        <a href="/sectores/veterinaria" class="cp-sec-pill">
          <svg class="cp-sec-icon" width="20" height="20" viewBox="0 0 24 24"><path d="M12 11v6"/><path d="M9 14h6"/><path d="M21.5 8.5c-1.3-1-3-1-4 0-1-1-2.7-1-4 0-1-1-2.7-1-4 0-1-1-2.7-1-4 0"/></svg>
          <span class="cp-sec-name">Veterinaria</span>
          <span class="cp-sec-arr">&rarr;</span>
        </a>
      </div>
    </div>
  </section>

  <!-- SECCION 7: FORMULARIO CTA -->
  <section class="cp-form-sec" id="contacto">
    <div class="container">
      <div class="cp-form-grid">
        <div class="cp-form-text fi">
          <h2>¿Listo para empezar?</h2>
          <p>Cuéntanos tu proyecto. En menos de 24 horas tienes respuesta de nuestro equipo técnico.</p>
          <ul class="cp-form-guarantees">
            <li>NDA firmado antes de la primera reunión</li>
            <li>Presupuesto sin compromiso</li>
            <li>Respuesta en menos de 24h</li>
            <li>Asesoramiento técnico incluido</li>
          </ul>
        </div>
        <div class="cp-form-box fi">
          <form id="cp-form">
            <div class="cp-input-group">
              <input type="text" class="cp-input" placeholder="Nombre completo" required>
            </div>
            <div class="cp-input-group">
              <input type="text" class="cp-input" placeholder="Empresa" required>
            </div>
            <div style="display:flex; gap:16px;">
              <div class="cp-input-group" style="flex:1">
                <input type="email" class="cp-input" placeholder="Email" required>
              </div>
              <div class="cp-input-group" style="flex:1">
                <input type="tel" class="cp-input" placeholder="Teléfono">
              </div>
            </div>
            <div class="cp-input-group">
              <select class="cp-input cp-select" required>
                <option value="" disabled selected>Selecciona un formato</option>
                <option value="stick">Stick Pack</option>
                <option value="sachet">Sachet</option>
                <option value="flowpack">Flow Pack</option>
                <option value="doypack">Doypack</option>
                <option value="bote">Bote rígido</option>
                <option value="tarro">Tarro / Jar</option>
                <option value="especial">Formato especial</option>
              </select>
            </div>
            <div class="cp-input-group">
              <select class="cp-input cp-select" required>
                <option value="" disabled selected>Volumen estimado</option>
                <option value="piloto">Lote piloto (<5.000 uds)</option>
                <option value="pequena">Pequeña serie (5.000–50.000 uds)</option>
                <option value="media">Media serie (50.000–500.000 uds)</option>
                <option value="gran">Gran serie (>500.000 uds)</option>
              </select>
            </div>
            <div class="cp-input-group">
              <textarea class="cp-input" rows="4" placeholder="Describe brevemente tu producto, necesidades especiales, plazos o cualquier información relevante para el presupuesto." required></textarea>
            </div>
            <div class="cp-check-wrap">
              <input type="checkbox" id="cp-check" required>
              <label for="cp-check" class="cp-check-label">Acepto la política de privacidad y el tratamiento de mis datos para recibir respuesta a mi consulta.</label>
            </div>
            <button type="submit" class="cp-submit">Solicitar presupuesto &rarr;</button>
            <p class="cp-form-note">Firmamos NDA antes de cualquier reunión técnica. Tu información es estrictamente confidencial.</p>
          </form>
        </div>
      </div>
    </div>
  </section>

  {footer}
"""

full_html = head + custom_styles + "</head>\n" + html_body

with open('copacking.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated copacking.html!")
