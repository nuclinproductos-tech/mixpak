import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HTML
old_html_pattern = r'  <!-- ===================== SERVICIOS — Proceso Industrial ===================== -->\n  <section class="section-proceso" id="servicios">.*?</section>'
new_html = """  <!-- ===================== SERVICIOS — Control Center ===================== -->
  <section class="services-premium" id="servicios">
    <div class="container">
      <div class="proceso-head fi">
        <span class="label">Nuestros Servicios</span>
        <h2>Servicios industriales para lanzar y escalar tu producto</h2>
        <p>Integramos formulación, fabricación y copacking para convertir una idea en producto terminado.</p>
      </div>

      <div class="services-premium-layout">
        <!-- LEFT: Visual -->
        <div class="services-visual fi">
          <img src="IMG/servicios/service_fabricacion3.png" alt="Instalaciones industriales Mix Pak" loading="lazy">
        </div>

        <!-- RIGHT: Stack -->
        <div class="service-stack">
          <!-- 01 Formulación -->
          <div class="service-step fi d1">
            <div class="service-step-number">01</div>
            <h3>Formulación y Desarrollo</h3>
            <p>Fórmulas a medida, prototipos y documentación técnica para fabricar con seguridad.</p>
            <a href="/formulacion-desarrollo" class="service-cta">Ver formulación &rarr;</a>
          </div>

          <!-- 02 Fabricación -->
          <div class="service-step fi d2">
            <div class="service-step-number">02</div>
            <h3>Fabricación</h3>
            <p>Producción propia con trazabilidad, control de calidad y capacidad de escalado.</p>
            <a href="/fabricacion" class="service-cta">Ver fabricación &rarr;</a>
          </div>

          <!-- 03 Copacking -->
          <div class="service-step fi d3">
            <div class="service-step-number">03</div>
            <h3>Copacking</h3>
            <p>Envasado en stick packs, sachets, doypacks, botes y formatos especiales.</p>
            <a href="/copacking.html" class="service-cta">Ver copacking &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Trust strip -->
      <div class="proceso-trust fi">
        <p>
          +30 líneas propias
          <span class="proceso-trust-sep">&middot;</span>
          +50 formatos
          <span class="proceso-trust-sep">&middot;</span>
          IFS Food
          <span class="proceso-trust-sep">&middot;</span>
          GMP
        </p>
      </div>

    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace CSS
old_css_pattern = r'    /\* ===================================================\n   SERVICIOS — Proceso Industrial Horizontal\n=================================================== \*/.*?\n    /\* ===================================================\n   STATS CAPACIDAD INDUSTRIAL\n=================================================== \*/'

new_css = """    /* ===================================================
   SERVICIOS — Premium Control Center
=================================================== */
    .services-premium {
      padding: 90px 0;
      background: #fff;
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

    .services-premium-layout {
      display: grid;
      grid-template-columns: 1.15fr .85fr;
      gap: 64px;
      align-items: center;
    }

    .services-visual img {
      width: 100%;
      height: 620px;
      object-fit: cover;
      border-radius: 0;
    }

    .service-stack {
      position: relative;
    }

    .service-stack::before {
      content: "";
      position: absolute;
      left: 18px;
      top: 20px;
      bottom: 20px;
      width: 1px;
      background: rgba(200,168,75,.45);
    }

    .service-step {
      position: relative;
      padding: 0 0 34px 56px;
    }

    .service-step:last-child {
      padding-bottom: 0;
    }

    .service-step-number {
      position: absolute;
      left: 0;
      top: 0;
      color: #C8A84B;
      font-weight: 800;
      font-size: 1.1rem;
      background: #fff;
      padding-bottom: 8px;
    }

    .service-step h3 {
      color: #000066;
      font-size: 1.7rem;
      font-family: 'DM Serif Display', Georgia, serif;
      margin: 0 0 8px 0;
      line-height: 1.2;
    }

    .service-step p {
      color: #667085;
      font-size: .95rem;
      line-height: 1.6;
      margin: 0 0 16px 0;
    }

    .service-cta {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: .85rem;
      font-weight: 700;
      color: var(--navy);
      text-decoration: none;
      border-bottom: 1.5px solid var(--gold);
      padding-bottom: 2px;
      transition: color .2s ease, gap .2s ease;
    }

    .service-cta:hover {
      color: var(--gold);
      gap: 10px;
    }

    .proceso-trust {
      text-align: center;
      margin-top: 64px;
    }

    .proceso-trust p {
      font-size: 0.9rem;
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

    @media (max-width: 960px) {
      .services-premium-layout {
        grid-template-columns: 1fr;
        gap: 48px;
      }
      .services-visual img {
        height: 320px;
      }
    }

    /* ===================================================
   STATS CAPACIDAD INDUSTRIAL
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
