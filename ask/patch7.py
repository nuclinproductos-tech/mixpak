import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML Replace
old_html_pattern = r'  <!-- ===================== SERVICIOS — Proceso Industrial ===================== -->\n  <section class="section-proceso" id="servicios">.*?</section>'
new_html = """  <!-- ===================== SERVICIOS — Proceso Industrial ===================== -->
  <section class="section-proceso" id="servicios">
    <div class="proceso-head fi">
      <span class="label">Nuestros Servicios</span>
      <h2>Servicios industriales para lanzar y escalar tu producto</h2>
      <p>Puedes contratar cada servicio por separado o integrar todo el proceso con un único partner: formulación, fabricación y copacking.</p>
    </div>

    <div class="proceso-grid">
      <!-- 01 Formulación -->
      <div class="step fi">
        <img src="IMG/servicios/service_formulacion-desarrollo.png" alt="Formulación y Desarrollo" loading="lazy">
        <div class="step-content">
          <span class="step-label">SERVICIO 01</span>
          <h3 class="step-title">Formulación y Desarrollo</h3>
          <p class="step-desc">Creamos fórmulas a medida, prototipos y documentación técnica para productos listos para fabricar.</p>
          <ul class="step-bullets">
            <li>Fórmulas a medida</li>
            <li>Prototipos y validación</li>
            <li>NDA desde el inicio</li>
          </ul>
          <a href="/formulacion-desarrollo" class="step-cta">Ver formulación &rarr;</a>
        </div>
      </div>

      <!-- 02 Fabricación -->
      <div class="step fi d1">
        <img src="IMG/servicios/service_fabricacion3.png" alt="Fabricación Industrial" loading="lazy">
        <div class="step-content">
          <span class="step-label">SERVICIO 02</span>
          <h3 class="step-title">Fabricación</h3>
          <p class="step-desc">Producimos en instalaciones propias con control de calidad, trazabilidad y capacidad de escalado industrial.</p>
          <ul class="step-bullets">
            <li>Mezclado y producción</li>
            <li>Control lote a lote</li>
            <li>Escalado industrial</li>
          </ul>
          <a href="/fabricacion" class="step-cta">Ver fabricación &rarr;</a>
        </div>
      </div>

      <!-- 03 Copacking -->
      <div class="step fi d2">
        <img src="IMG/servicios/service_copaking.png" alt="Copacking" loading="lazy">
        <div class="step-content">
          <span class="step-label">SERVICIO 03</span>
          <h3 class="step-title">Copacking</h3>
          <p class="step-desc">Envasamos tu producto en stick packs, sachets, doypacks, botes y formatos especiales.</p>
          <ul class="step-bullets">
            <li>+30 líneas propias</li>
            <li>+50 formatos</li>
            <li>Lote piloto a gran serie</li>
          </ul>
          <a href="/copacking.html" class="step-cta">Ver copacking &rarr;</a>
        </div>
      </div>
    </div>

    <!-- Trust strip -->
    <div class="proceso-trust fi">
      <p>
        Formulación
        <span class="proceso-trust-sep">&middot;</span>
        Fabricación propia
        <span class="proceso-trust-sep">&middot;</span>
        Copacking
        <span class="proceso-trust-sep">&middot;</span>
        +50 formatos
        <span class="proceso-trust-sep">&middot;</span>
        IFS Food
        <span class="proceso-trust-sep">&middot;</span>
        GMP
      </p>
    </div>

    <div class="proceso-footer fi">
      <a href="/contacto" class="btn">Cuéntanos qué necesitas fabricar &rarr;</a>
    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. CSS Replace
old_css_pattern = r'    /\* ===================================================\n   SERVICIOS — Proceso Industrial Horizontal\n=================================================== \*/.*?\n    /\* ===================================================\n   STATS CAPACIDAD INDUSTRIAL\n=================================================== \*/'

new_css = """    /* ===================================================
   SERVICIOS — Proceso Industrial Horizontal
=================================================== */
    .section-proceso {
      background: var(--bg);
      padding: 80px 0;
      position: relative;
    }

    .proceso-head {
      text-align: center;
      max-width: 760px;
      margin: 0 auto 56px;
      padding: 0 24px;
    }

    .proceso-head h2 {
      font-size: clamp(1.95rem, 3vw, 2.7rem);
      color: var(--navy);
      margin-bottom: 14px;
      line-height: 1.1;
    }

    .proceso-head p {
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.7;
      max-width: 600px;
      margin: 0 auto;
    }

    .proceso-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      align-items: stretch;
      gap: 0;
      position: relative;
      max-width: 1440px;
      margin: 0 auto;
    }

    /* Horizontal line connecting steps */
    .proceso-grid::before {
      content: "";
      position: absolute;
      top: 50%;
      left: 10%;
      right: 10%;
      height: 1px;
      background: rgba(199,163,93,0.3);
      z-index: 2;
      pointer-events: none;
    }

    .step {
      position: relative;
      height: 480px;
      overflow: hidden;
      display: block;
    }

    .step img {
      position: absolute;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .step::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,25,0.3) 0%, rgba(0,0,35,0.7) 40%, rgba(0,0,45,0.92) 100%);
      transition: background 0.4s ease;
    }

    .step:hover img {
      transform: scale(1.04);
    }

    .step:hover::after {
      background: linear-gradient(180deg, rgba(0,0,25,0.3) 0%, rgba(0,0,35,0.75) 40%, rgba(0,0,45,0.98) 100%);
    }

    .step-content {
      position: absolute;
      left: 32px;
      right: 32px;
      bottom: 40px;
      z-index: 3;
      display: flex;
      flex-direction: column;
      pointer-events: none;
    }

    .step-label {
      font-size: 11px;
      letter-spacing: 2px;
      color: #C7A35D;
      margin-bottom: 8px;
      font-weight: 700;
      text-transform: uppercase;
    }

    .step-title {
      font-size: 28px;
      color: white;
      font-weight: 600;
      font-family: 'DM Serif Display', Georgia, serif;
      margin: 0 0 12px 0;
      line-height: 1.1;
    }

    .step-desc {
      font-size: 14px;
      color: rgba(255,255,255,0.85);
      margin: 0 0 16px 0;
      line-height: 1.5;
    }

    .step-bullets {
      list-style: none;
      padding: 0;
      margin: 0 0 24px 0;
    }

    .step-bullets li {
      position: relative;
      padding-left: 14px;
      font-size: 13px;
      color: rgba(255,255,255,0.75);
      margin-bottom: 6px;
    }

    .step-bullets li::before {
      content: "·";
      position: absolute;
      left: 0;
      color: #C7A35D;
      font-weight: bold;
    }

    .step-cta {
      align-self: flex-start;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      border-bottom: 1px solid #C7A35D;
      padding-bottom: 2px;
      transition: color 0.3s ease, border-color 0.3s ease;
      pointer-events: auto; /* ensure it's clickable */
    }

    .step-cta:hover {
      color: #C7A35D;
    }

    .proceso-trust {
      text-align: center;
      margin-top: 40px;
      padding: 0 24px;
    }

    .proceso-trust p {
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0;
    }

    .proceso-trust-sep {
      margin: 0 14px;
      color: rgba(200, 168, 75, 0.6);
      font-size: 0.9rem;
    }

    .proceso-footer {
      text-align: center;
      margin-top: 32px;
    }

    /* RESPONSIVE */
    @media (max-width: 1024px) {
      .step {
        height: 520px;
      }
      .step-title {
        font-size: 24px;
      }
    }

    @media (max-width: 900px) {
      .proceso-grid {
        grid-template-columns: 1fr;
      }
      .proceso-grid::before {
        display: none;
      }
      .step {
        height: 380px;
      }
    }

    /* ===================================================
   STATS CAPACIDAD INDUSTRIAL
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
