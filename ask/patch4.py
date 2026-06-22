import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HTML
old_html_pattern = r'  <section class="sectores" id="sectores">.*?</section>'
new_html = """  <section class="sectores" id="sectores">
    <div class="container">
      <div class="sectores-head fi">
        <span class="label">Sectores</span>
        <h2 class="section-title">Fabricamos para distintas industrias</h2>
        <p class="section-desc">Adaptamos formulación, fabricación y copacking a las exigencias de cada sector.</p>
      </div>
    </div>

    <!-- GRID VISUAL ASIMÉTRICO (FULL WIDTH) -->
    <div class="sectores-grid">
      
      <!-- Fila 1: 2/3 y 1/3 -->
      <a href="/sectores/nutricion-deportiva" class="sector-visual sector-visual--span4 fi">
        <img src="IMG/sectores/sector_nutricion-deportiva.png" alt="Nutrición Deportiva" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Nutrición deportiva</h3>
        </div>
      </a>

      <a href="/sectores/complementos-alimenticios" class="sector-visual sector-visual--span2 fi d1">
        <img src="IMG/sectores/sector_complementos-alimenticios.png" alt="Complementos Alimenticios" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Complementos alimenticios</h3>
        </div>
      </a>

      <!-- Fila 2: 1/3 y 2/3 -->
      <a href="/sectores/cosmetica" class="sector-visual sector-visual--span2 fi">
        <img src="IMG/sectores/sector_cosmetica.png" alt="Cosmética" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Cosmética</h3>
        </div>
      </a>

      <a href="/sectores/alimentacion-funcional" class="sector-visual sector-visual--span4 fi d1">
        <img src="IMG/sectores/sector_alimentacion.png" alt="Alimentación Funcional" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Alimentación funcional</h3>
        </div>
      </a>

      <!-- Fila 3: 1/2 y 1/2 -->
      <a href="/sectores/higiene" class="sector-visual sector-visual--span3 fi">
        <img src="IMG/sectores/sector_higiene.png" alt="Higiene" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Higiene</h3>
        </div>
      </a>

      <a href="/sectores/veterinaria" class="sector-visual sector-visual--span3 fi d1">
        <img src="IMG/sectores/sector_veterinaria.png" alt="Veterinaria" loading="lazy">
        <div class="sector-visual-content">
          <span class="sector-visual-label">SECTOR</span>
          <h3>Veterinaria</h3>
        </div>
      </a>

    </div>

    <!-- CTA FINAL -->
    <div class="container">
      <div class="sectores-footer fi">
        <a href="/contacto" class="sector-footer-cta">¿Tu sector no aparece? Cuéntanos tu proyecto →</a>
      </div>
    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace CSS
old_css_pattern = r'    /\* ===================================================\n   SECTORES — Visual editorial 3×2\n=================================================== \*/.*?\n    /\* ===================================================\n   ENV3 — Rediseño visual industrial B2B\n=================================================== \*/'

new_css = """    /* ===================================================
   SECTORES — Visual editorial Asimétrico B2B
=================================================== */
    .sectores {
      padding: 100px 0;
      background: var(--bg);
    }

    .sectores-head {
      text-align: center;
      max-width: 820px;
      margin: 0 auto 64px;
    }

    .sectores-head .section-desc {
      margin: 0 auto;
      max-width: 600px;
    }

    .sectores-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 4px;
      width: 100%;
    }

    .sector-visual {
      position: relative;
      overflow: hidden;
      display: block;
      cursor: pointer;
      height: 440px;
      background: #111;
      text-decoration: none;
    }

    .sector-visual--span4 { grid-column: span 4; }
    .sector-visual--span2 { grid-column: span 2; }
    .sector-visual--span3 { grid-column: span 3; }

    .sector-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .sector-visual:hover img {
      transform: scale(1.03);
    }

    /* Subtle overlay fade-in */
    .sector-visual::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0) 40%);
      transition: background 0.4s ease;
      pointer-events: none;
    }

    .sector-visual:hover::after {
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.2) 100%);
    }

    .sector-visual-content {
      position: absolute;
      left: 40px;
      bottom: 40px;
      z-index: 2;
      display: flex;
      flex-direction: column;
      pointer-events: none;
    }

    .sector-visual-label {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.7);
      margin-bottom: 8px;
    }

    .sector-visual h3 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: 2.2rem;
      color: #fff;
      margin: 0;
      line-height: 1.1;
      text-shadow: 0 2px 12px rgba(0,0,0,0.4);
    }

    .sectores-footer {
      text-align: center;
      margin-top: 64px;
    }

    .sector-footer-cta {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--navy);
      border-bottom: 2px solid var(--gold);
      padding-bottom: 2px;
      transition: var(--tr);
      text-decoration: none;
    }

    .sector-footer-cta:hover {
      color: var(--gold);
      gap: 10px;
    }

    /* RESPONSIVE */
    @media (max-width: 1024px) {
      .sector-visual {
        height: 360px;
      }
      .sector-visual-content {
        left: 32px;
        bottom: 32px;
      }
      .sector-visual h3 {
        font-size: 1.8rem;
      }
    }

    @media (max-width: 768px) {
      .sectores {
        padding: 72px 0;
      }
      .sectores-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .sector-visual--span4, 
      .sector-visual--span2, 
      .sector-visual--span3 {
        grid-column: span 1;
      }
      .sector-visual {
        height: 280px;
      }
      .sector-visual-content {
        left: 24px;
        bottom: 24px;
      }
      .sector-visual h3 {
        font-size: 1.5rem;
      }
    }

    @media (max-width: 600px) {
      .sectores-grid {
        grid-template-columns: 1fr;
        gap: 2px;
      }
      .sector-visual--span4, 
      .sector-visual--span2, 
      .sector-visual--span3 {
        grid-column: span 1;
      }
      .sector-visual {
        height: 260px;
      }
    }

    /* ===================================================
   ENV3 — Rediseño visual industrial B2B
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
