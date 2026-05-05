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

      <!-- GRID VISUAL COMPACTO 3x2 -->
      <div class="sectores-grid">
        
        <a href="/sectores/nutricion-deportiva" class="sector-item fi">
          <img src="IMG/sectores/sector_nutricion-deportiva.png" alt="Nutrición Deportiva" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Nutrición deportiva</h3>
          </div>
        </a>

        <a href="/sectores/complementos-alimenticios" class="sector-item fi d1">
          <img src="IMG/sectores/sector_complementos-alimenticios.png" alt="Complementos Alimenticios" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Complementos alimenticios</h3>
          </div>
        </a>

        <a href="/sectores/cosmetica" class="sector-item fi d2">
          <img src="IMG/sectores/sector_cosmetica.png" alt="Cosmética" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Cosmética</h3>
          </div>
        </a>

        <a href="/sectores/alimentacion-funcional" class="sector-item fi">
          <img src="IMG/sectores/sector_alimentacion.png" alt="Alimentación Funcional" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Alimentación funcional</h3>
          </div>
        </a>

        <a href="/sectores/higiene" class="sector-item fi d1">
          <img src="IMG/sectores/sector_higiene.png" alt="Higiene" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Higiene</h3>
          </div>
        </a>

        <a href="/sectores/veterinaria" class="sector-item fi d2">
          <img src="IMG/sectores/sector_veterinaria.png" alt="Veterinaria" loading="lazy">
          <div class="sector-item-content">
            <span class="sector-item-label">SECTOR</span>
            <h3>Veterinaria</h3>
          </div>
        </a>

      </div>

      <!-- CTA FINAL -->
      <div class="sectores-footer fi">
        <a href="/contacto" class="sector-footer-cta">¿Tu sector no aparece? Cuéntanos tu proyecto →</a>
      </div>
    </div>
  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace CSS
old_css_pattern = r'    /\* ===================================================\n   SECTORES — Visual editorial Asimétrico B2B\n=================================================== \*/.*?\n    /\* ===================================================\n   ENV3 — Rediseño visual industrial B2B\n=================================================== \*/'

new_css = """    /* ===================================================
   SECTORES — Grid Compacto 3x2 B2B
=================================================== */
    .sectores {
      padding: 80px 0;
      background: var(--bg);
    }

    .sectores-head {
      text-align: center;
      max-width: 820px;
      margin: 0 auto 40px;
    }

    .sectores-head .section-desc {
      margin: 0 auto;
      max-width: 600px;
    }

    .sectores-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }

    .sector-item {
      position: relative;
      height: 240px;
      overflow: hidden;
      border-radius: 0;
      display: block;
      cursor: pointer;
      background: #111;
      text-decoration: none;
    }

    .sector-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .sector-item:hover img {
      transform: scale(1.03);
    }

    .sector-item::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 45%, rgba(0,0,55,.72) 100%);
      transition: background 0.4s ease;
      pointer-events: none;
    }

    .sector-item:hover::after {
      background: linear-gradient(180deg, transparent 35%, rgba(0,0,55,.85) 100%);
    }

    .sector-item-content {
      position: absolute;
      left: 20px;
      bottom: 20px;
      z-index: 2;
      display: flex;
      flex-direction: column;
      pointer-events: none;
    }

    .sector-item-label {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 6px;
    }

    .sector-item h3 {
      font-family: 'DM Serif Display', Georgia, serif;
      font-size: 1.6rem;
      color: #fff;
      margin: 0;
      line-height: 1.1;
      text-shadow: 0 2px 12px rgba(0,0,0,0.4);
    }

    .sectores-footer {
      text-align: center;
      margin-top: 48px;
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
    @media (max-width: 900px) {
      .sectores-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 600px) {
      .sectores {
        padding: 60px 0;
      }
      .sectores-grid {
        grid-template-columns: 1fr;
        gap: 12px;
      }
      .sector-item {
        height: 190px;
      }
      .sector-item-content {
        left: 16px;
        bottom: 16px;
      }
      .sector-item h3 {
        font-size: 1.4rem;
      }
    }

    /* ===================================================
   ENV3 — Rediseño visual industrial B2B
=================================================== */"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
