import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HTML
old_html_pattern = r'  <!-- ===================== SERVICIOS — Workflow ===================== -->\n  <section class="wf-services" id="servicios">.*?</section>'
new_html = """  <!-- ===================== SERVICIOS — Proceso Industrial ===================== -->
  <section class="section-proceso" id="servicios">
    <div class="proceso-head fi">
      <span class="label">Nuestros Servicios</span>
      <h2>Un único partner para todo el proceso industrial</h2>
      <p>Un único partner para desarrollar, fabricar y envasar tu marca con estándares industriales.</p>
    </div>

    <div class="proceso-grid">
      <!-- 01 Formulación -->
      <a href="/formulacion-desarrollo" class="step fi">
        <img src="IMG/servicios/service_formulacion-desarrollo.png" alt="Formulación y Desarrollo" loading="lazy">
        <div class="step-content">
          <span class="step-label">01 / FORMULACIÓN</span>
          <h3 class="step-title">De la idea a la fórmula</h3>
          <p class="step-desc">Desarrollamos fórmulas viables, estables y listas para escalar industrialmente.</p>
        </div>
      </a>

      <!-- 02 Fabricación -->
      <a href="/fabricacion" class="step fi d1">
        <img src="IMG/servicios/service_fabricacion3.png" alt="Fabricación Industrial" loading="lazy">
        <div class="step-content">
          <span class="step-label">02 / FABRICACIÓN</span>
          <h3 class="step-title">Producción industrial propia</h3>
          <p class="step-desc">Producción con trazabilidad y capacidad desde lote piloto hasta gran serie.</p>
        </div>
      </a>

      <!-- 03 Copacking -->
      <a href="/copacking.html" class="step fi d2">
        <img src="IMG/servicios/service_copaking.png" alt="Copacking" loading="lazy">
        <div class="step-content">
          <span class="step-label">03 / COPACKING</span>
          <h3 class="step-title">Envasado multiformato</h3>
          <p class="step-desc">Más de 50 formatos con líneas propias. Stick packs, sachets, doypacks y botes.</p>
        </div>
      </a>
    </div>

    <!-- Trust strip -->
    <div class="proceso-trust fi">
      <p>
        <span>+30 líneas de envasado propias</span>
        <span class="proceso-trust-sep">·</span>
        <span>IFS Food Certified</span>
        <span class="proceso-trust-sep">·</span>
        <span>GMP Certified</span>
        <span class="proceso-trust-sep">·</span>
        <span>Desde lote piloto hasta gran serie</span>
      </p>
    </div>

    <div class="proceso-footer fi">
      <a href="/contacto" class="btn">Ver proceso completo →</a>
    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace CSS
old_css_pattern = r'    /\* ===================================================\n   SERVICIOS — Workflow 3 etapas\n=================================================== \*/.*?\n    /\* ===================================================\n   STATS CAPACIDAD INDUSTRIAL\n=================================================== \*/'

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
      max-width: 680px;
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
      max-width: 520px;
      margin: 0 auto;
    }

    .proceso-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      align-items: center;
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
      height: 320px;
      overflow: hidden;
      display: block;
      text-decoration: none;
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
      background: linear-gradient(180deg, rgba(0,0,30,0.4), rgba(0,0,40,0.8));
      transition: background 0.4s ease;
    }

    .step:hover img {
      transform: scale(1.04);
    }

    .step:hover::after {
      background: linear-gradient(180deg, rgba(0,0,30,0.3), rgba(0,0,40,0.9));
    }

    .step-content {
      position: absolute;
      left: 32px;
      bottom: 32px;
      z-index: 3;
      display: flex;
      flex-direction: column;
    }

    .step-label {
      font-size: 12px;
      letter-spacing: 2px;
      color: #C7A35D;
      margin-bottom: 8px;
      font-weight: 700;
    }

    .step-title {
      font-size: 26px;
      color: white;
      font-weight: 600;
      font-family: 'DM Serif Display', Georgia, serif;
      margin: 0 0 8px 0;
      line-height: 1.1;
    }

    .step-desc {
      font-size: 14px;
      color: rgba(255,255,255,0.85);
      max-width: 280px;
      margin: 0;
      line-height: 1.5;
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
    @media (max-width: 900px) {
      .proceso-grid {
        grid-template-columns: 1fr;
      }
      .proceso-grid::before {
        display: none;
      }
      .step {
        height: 280px;
      }
    }

    /* ===================================================
   STATS CAPACIDAD INDUSTRIAL
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
