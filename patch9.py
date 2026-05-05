import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HTML
old_html_pattern = r'  <!-- ===================== SERVICIOS — Control Center ===================== -->\n  <section class="services-premium" id="servicios">.*?</section>'
new_html = """  <!-- ===================== SERVICIOS — Premium Editorial ===================== -->
  <section class="services-editorial" id="servicios">
    <div class="container">
      <div class="services-head fi">
        <span class="label">SERVICIOS INDUSTRIALES</span>
        <h2>Un único partner para desarrollar, fabricar y envasar tu producto</h2>
        <p>Integramos formulación y desarrollo, fabricación, copaking y envasado para convertir una idea en un producto listo para el mercado.</p>
      </div>

      <div class="services-grid">
        <!-- 01 -->
        <div class="service-col fi">
          <div class="service-img">
            <img src="IMG/servicios/service_formulacion-desarrollo.png" alt="Formulación y desarrollo" loading="lazy">
          </div>
          <div class="service-content">
            <div class="service-num">01</div>
            <h3>Formulación y desarrollo</h3>
            <p>Desarrollamos fórmulas a medida, prototipos y documentación técnica para crear productos viables, estables y escalables.</p>
          </div>
        </div>

        <!-- 02 -->
        <div class="service-col fi d1">
          <div class="service-img">
            <img src="IMG/servicios/service_fabricacion3.png" alt="Fabricación" loading="lazy">
          </div>
          <div class="service-content">
            <div class="service-num">02</div>
            <h3>Fabricación</h3>
            <p>Producimos en instalaciones propias con control de calidad, trazabilidad y capacidad de escalado industrial.</p>
          </div>
        </div>

        <!-- 03 -->
        <div class="service-col fi d2">
          <div class="service-img">
            <img src="IMG/servicios/service_copaking.png" alt="Copaking" loading="lazy">
          </div>
          <div class="service-content">
            <div class="service-num">03</div>
            <h3>Copaking</h3>
            <p>Acondicionamos y preparamos producto para terceros con procesos flexibles y adaptados a cada proyecto.</p>
          </div>
        </div>

        <!-- 04 -->
        <div class="service-col fi d3">
          <div class="service-img">
            <img src="img/recursos/all-productos.png" alt="Envasado" loading="lazy">
          </div>
          <div class="service-content">
            <div class="service-num">04</div>
            <h3>Envasado</h3>
            <p>Envasamos en stick packs, sachets, doypacks, botes y formatos especiales.</p>
          </div>
        </div>
      </div>

      <div class="services-footer fi">
        <a href="/contacto" class="btn">Ver servicios</a>
      </div>
    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace CSS
old_css_pattern = r'    /\* ===================================================\n   SERVICIOS — Premium Control Center\n=================================================== \*/.*?\n    /\* ===================================================\n   STATS CAPACIDAD INDUSTRIAL\n=================================================== \*/'

new_css = """    /* ===================================================
   SERVICIOS — Premium Editorial Process
=================================================== */
    .services-editorial {
      background: #fff;
      padding: 100px 0;
    }

    .services-head {
      text-align: center;
      max-width: 800px;
      margin: 0 auto 64px;
      padding: 0 24px;
    }

    .services-head .label {
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.15em;
      color: var(--gold);
      margin-bottom: 16px;
      display: inline-block;
      font-size: 0.75rem;
    }

    .services-head h2 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: clamp(2rem, 3.5vw, 2.8rem);
      color: var(--navy);
      margin-bottom: 16px;
      line-height: 1.15;
    }

    .services-head p {
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 650px;
      margin: 0 auto;
    }

    .services-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 32px;
      padding: 0 24px;
      max-width: 1300px;
      margin: 0 auto;
    }

    .service-col {
      display: flex;
      flex-direction: column;
      position: relative;
    }

    /* Thin divider lines between columns */
    .service-col:not(:last-child)::after {
      content: "";
      position: absolute;
      top: 0;
      right: -16px;
      width: 1px;
      height: 100%;
      background: rgba(0,0,102,0.06);
    }

    .service-img {
      width: 100%;
      aspect-ratio: 4/5;
      overflow: hidden;
      margin-bottom: 24px;
      background: #f8f9fb; /* fallback */
    }

    .service-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }

    .service-col:hover .service-img img {
      transform: scale(1.04);
    }

    .service-content {
      display: flex;
      flex-direction: column;
      padding-right: 12px;
    }

    .service-num {
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--gold);
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(200, 168, 75, 0.3);
    }

    .service-content h3 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: 1.35rem;
      color: var(--navy);
      margin-bottom: 10px;
      line-height: 1.2;
    }

    .service-content p {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin: 0;
    }

    .services-footer {
      text-align: center;
      margin-top: 64px;
    }

    /* RESPONSIVE */
    @media (max-width: 1024px) {
      .services-grid {
        grid-template-columns: repeat(2, 1fr);
        row-gap: 48px;
        column-gap: 32px;
      }
      .service-col:not(:last-child)::after {
        display: none;
      }
      .service-col:nth-child(1)::after,
      .service-col:nth-child(3)::after {
        content: "";
        display: block;
        position: absolute;
        top: 0;
        right: -16px;
        width: 1px;
        height: 100%;
        background: rgba(0,0,102,0.06);
      }
    }

    @media (max-width: 640px) {
      .services-grid {
        grid-template-columns: 1fr;
        row-gap: 48px;
      }
      .service-col::after {
        display: none !important;
      }
      .service-img {
        aspect-ratio: 16/9;
      }
    }

    /* ===================================================
   STATS CAPACIDAD INDUSTRIAL
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
