import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove old facilities block
# Search using regex to match the old block between <!-- ===================== FACILITIES ===================== --> and </section> right before <!-- ===================== FINANCIACIÓN INSTITUCIONAL ===================== -->
pattern_html_old = r'  <!-- ===================== FACILITIES ===================== -->\n  <section class="facilities fi">.*?  </section>\n\n'
content = re.sub(pattern_html_old, '  <!-- Old facilities removed -->\n\n', content, flags=re.DOTALL)


# 2. Insert new facilities block before CONTACT
new_html = """  <!-- ===================== FACILITIES ===================== -->
  <section class="facilities">
    <div class="container">

      <div class="fac-head fi">
        <span class="label">Instalaciones</span>
        <h2 class="section-title">
          Capacidad industrial real
        </h2>
        <p class="section-desc" 
           style="margin:0 auto">
          Dos plantas propias en Alhama de Murcia. 
          Más de 30 líneas de envasado. 
          Certificación IFS Food y GMP activas 
          en todos los procesos.
        </p>
      </div>

      <!-- Grid principal: 2 columnas grandes -->
      <div class="fac-grid">

        <!-- Instalación 1: Línea de envasado flexible -->
        <div class="fac-card fac-card--large fi">
          <div class="fac-img-wrap">
            <img 
              src="IMG/sectores/complementos-alimenticios.jpg"
              alt="Línea de envasado flexible — doypacks y sachets — Mix Pak System"
              class="fac-img"
              loading="lazy">
            <div class="fac-overlay">
              <span class="fac-tag">Envasado Flexible</span>
            </div>
          </div>
          <div class="fac-body">
            <h3>Líneas de envasado flexible</h3>
            <p>Capacidad para doypacks, sachets, 
            stick packs y formatos especiales. 
            Control automatizado de peso y sellado 
            con trazabilidad lote a lote.</p>
            <div class="fac-stats">
              <div class="fac-stat">
                <strong>+30</strong>
                <span>líneas propias</span>
              </div>
              <div class="fac-stat">
                <strong>IFS</strong>
                <span>Food Certified</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Instalación 2: Línea rígida / higiene -->
        <div class="fac-card fac-card--large fi d1">
          <div class="fac-img-wrap">
            <img 
              src="IMG/sectores/higiene.jpg"
              alt="Línea de envasado rígido — botellas y botes — Mix Pak System"
              class="fac-img"
              loading="lazy">
            <div class="fac-overlay">
              <span class="fac-tag">Envasado Rígido</span>
            </div>
          </div>
          <div class="fac-body">
            <h3>Líneas de envasado rígido</h3>
            <p>Llenado y acondicionado de botellas, 
            botes y envases rígidos. Capacidad para 
            sectores de higiene, cosmética y 
            complementos alimenticios.</p>
            <div class="fac-stats">
              <div class="fac-stat">
                <strong>GMP</strong>
                <span>Certified</span>
              </div>
              <div class="fac-stat">
                <strong>2</strong>
                <span>plantas propias</span>
              </div>
            </div>
          </div>
        </div>

      </div><!-- /fac-grid -->

      <!-- Grid secundario: 3 columnas más pequeñas -->
      <div class="fac-grid-sm">

        <div class="fac-card-sm fi">
          <div class="fac-img-wrap fac-img-wrap--sm">
            <img 
              src="IMG/sectores/nutricion-deportiva.jpg"
              alt="Fabricación nutrición deportiva — Mix Pak System"
              class="fac-img"
              loading="lazy">
            <div class="fac-overlay">
              <span class="fac-tag">Nutrición deportiva</span>
            </div>
          </div>
          <div class="fac-body-sm">
            <h4>Botes y formatos deportivos</h4>
            <p>Llenado de proteínas y suplementos 
            en botes rígidos de gran volumen.</p>
          </div>
        </div>

        <div class="fac-card-sm fi d1">
          <div class="fac-img-wrap fac-img-wrap--sm">
            <img 
              src="IMG/instalaciones/sala-blanca-gmp.jpg"
              alt="Sala blanca GMP — fabricación certificada — Mix Pak System"
              class="fac-img"
              loading="lazy">
            <div class="fac-overlay">
              <span class="fac-tag">Sala blanca GMP</span>
            </div>
          </div>
          <div class="fac-body-sm">
            <h4>Sala blanca certificada</h4>
            <p>Entorno controlado GMP para 
            productos de alta exigencia regulatoria.</p>
          </div>
        </div>

        <div class="fac-card-sm fi d2">
          <div class="fac-img-wrap fac-img-wrap--sm">
            <img 
              src="IMG/sectores/alimentacion-funcional.jpg"
              alt="Fabricación alimentación funcional — Mix Pak System"
              class="fac-img"
              loading="lazy">
            <div class="fac-overlay">
              <span class="fac-tag">Alimentación funcional</span>
            </div>
          </div>
          <div class="fac-body-sm">
            <h4>Líneas multipropósito</h4>
            <p>Cambios ágiles de formato para 
            tiradas cortas y gran serie.</p>
          </div>
        </div>

      </div><!-- /fac-grid-sm -->

      <!-- Strip de datos -->
      <div class="fac-data-strip fi">
        <div class="fac-data-item">
          <svg width="18" height="18" 
               viewBox="0 0 24 24" fill="none"
               stroke="var(--gold)" stroke-width="1.8"
               stroke-linecap="round" 
               stroke-linejoin="round"
               aria-hidden="true">
            <path d="M21 10c0 7-9 13-9 13S3 17 3 10
                     a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <span>Plgno. Ind. Las Salinas, 
          Alhama de Murcia</span>
        </div>
        <div class="fac-data-sep">·</div>
        <div class="fac-data-item">
          <svg width="18" height="18" 
               viewBox="0 0 24 24" fill="none"
               stroke="var(--gold)" stroke-width="1.8"
               stroke-linecap="round" 
               stroke-linejoin="round"
               aria-hidden="true">
            <rect x="2" y="7" width="20" 
                  height="14" rx="1"/>
            <path d="M2 7l10-5 10 5"/>
            <path d="M9 21V12h6v9"/>
          </svg>
          <span>2 plantas de producción propias</span>
        </div>
        <div class="fac-data-sep">·</div>
        <div class="fac-data-item">
          <svg width="18" height="18" 
               viewBox="0 0 24 24" fill="none"
               stroke="var(--gold)" stroke-width="1.8"
               stroke-linecap="round" 
               stroke-linejoin="round"
               aria-hidden="true">
            <polyline points="22 12 18 12 15 21 
                              9 3 6 12 2 12"/>
          </svg>
          <span>Certificación IFS Food y GMP activas</span>
        </div>
      </div>

    </div>
  </section>

  <!-- ===================== CONTACT ===================== -->"""
content = content.replace('  <!-- ===================== CONTACT ===================== -->', new_html)

# 3. Replace old CSS
# Pattern to find old CSS from /* ===================================================\n       FACILITIES - Corporate Locations Info Block to the end of the media query for it.
pattern_css_old = r'    /\* ===================================================\n       FACILITIES - Corporate Locations Info Block\n       =================================================== \*/\n    \.facilities \{.*?\n      \.facilities \{\n        padding: 0 0 60px 0;\n      \}\n    \}'

new_css = """    /* ===================================================
       FACILITIES - Corporate Locations Info Block
       =================================================== */
    .facilities {
      padding: 90px 0 100px 0;
      background: var(--bg);
    }
    .fac-head {
      text-align: center;
      margin-bottom: 64px;
    }

    .fac-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }

    .fac-card {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--r);
      overflow: hidden;
      transition: var(--tr);
    }

    .fac-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--sh-lg);
      border-color: rgba(200,168,75,0.3);
    }

    .fac-img-wrap {
      position: relative;
      height: 280px;
      overflow: hidden;
    }

    .fac-img-wrap--sm {
      height: 200px;
    }

    .fac-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }

    .fac-card:hover .fac-img,
    .fac-card-sm:hover .fac-img {
      transform: scale(1.04);
    }

    .fac-overlay {
      position: absolute;
      top: 16px;
      left: 16px;
    }

    .fac-tag {
      background: rgba(6,12,36,0.75);
      color: rgba(255,255,255,0.9);
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 100px;
      backdrop-filter: blur(4px);
    }

    .fac-body {
      padding: 28px 28px 24px;
    }

    .fac-body h3 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: 1.3rem;
      color: var(--navy);
      margin-bottom: 10px;
    }

    .fac-body p {
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.7;
      margin-bottom: 20px;
    }

    .fac-stats {
      display: flex;
      gap: 28px;
    }

    .fac-stat {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .fac-stat strong {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--navy);
      line-height: 1;
    }

    .fac-stat span {
      font-size: 0.7rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }

    /* Grid secundario */
    .fac-grid-sm {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 36px;
    }

    .fac-card-sm {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--r);
      overflow: hidden;
      transition: var(--tr);
    }

    .fac-card-sm:hover {
      transform: translateY(-4px);
      box-shadow: var(--sh-lg);
      border-color: rgba(200,168,75,0.3);
    }

    .fac-body-sm {
      padding: 20px 20px 18px;
    }

    .fac-body-sm h4 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: 1.05rem;
      color: var(--navy);
      margin-bottom: 6px;
    }

    .fac-body-sm p {
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin: 0;
    }

    /* Data strip */
    .fac-data-strip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      padding: 24px 32px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--r);
      flex-wrap: wrap;
    }

    .fac-data-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .fac-data-sep {
      color: var(--border);
      font-size: 1.2rem;
    }

    /* Responsive */
    @media (max-width: 900px) {
      .fac-grid {
        grid-template-columns: 1fr;
      }
      .fac-grid-sm {
        grid-template-columns: 1fr 1fr;
      }
      .fac-img-wrap {
        height: 240px;
      }
    }

    @media (max-width: 600px) {
      .fac-grid-sm {
        grid-template-columns: 1fr;
      }
      .fac-data-strip {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
      }
      .fac-data-sep {
        display: none;
      }
    }"""
content = re.sub(pattern_css_old, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

