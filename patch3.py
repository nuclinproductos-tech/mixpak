import re

with open('/Users/anabelen/mixpaksystem/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Facilities HTML Block
old_html_pattern = r'  <!-- ===================== FACILITIES ===================== -->\n  <section class="facilities">.*?</section>'
new_html = """  <!-- ===================== FACILITIES ===================== -->
  <section class="facilities">
    <div class="fac-header fi">
      <span class="label">Instalaciones</span>
      <h2 class="section-title">Capacidad industrial real</h2>
      <p class="section-desc" style="margin:0 auto">
        Dos plantas propias en Alhama de Murcia. 
        Más de 30 líneas de envasado. 
        Certificación IFS Food y GMP activas.
      </p>
    </div>

    <div class="fac-carousel" id="facCarousel">

      <!-- Slides -->
      <div class="fac-slides" id="facSlides">

        <div class="fac-slide" data-index="0">
          <div class="fac-slide-bg">
            <img src="IMG/sectores/complementos-alimenticios.jpg"
                 alt="Líneas de envasado flexible — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Envasado Flexible</span>
            <h3 class="fac-slide-title">Líneas de envasado flexible</h3>
            <p class="fac-slide-dato">+30 líneas propias · IFS Food Certified</p>
          </div>
        </div>

        <div class="fac-slide" data-index="1">
          <div class="fac-slide-bg">
            <img src="IMG/sectores/higiene.jpg"
                 alt="Capacidad para envases rígidos — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Envasado Rígido</span>
            <h3 class="fac-slide-title">Capacidad para envases rígidos</h3>
            <p class="fac-slide-dato">Botellas, botes y envases de alta cadencia</p>
          </div>
        </div>

        <div class="fac-slide" data-index="2">
          <div class="fac-slide-bg">
            <img src="IMG/sectores/nutricion-deportiva.jpg"
                 alt="Fabricación de suplementos en serie — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Nutrición Deportiva</span>
            <h3 class="fac-slide-title">Fabricación de suplementos en serie</h3>
            <p class="fac-slide-dato">Botes, stick packs y formatos especiales</p>
          </div>
        </div>

        <div class="fac-slide" data-index="3">
          <div class="fac-slide-bg">
            <img src="IMG/instalaciones/sala-blanca-gmp.jpg"
                 alt="Entorno controlado certificado — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Sala Blanca GMP</span>
            <h3 class="fac-slide-title">Entorno controlado certificado</h3>
            <p class="fac-slide-dato">GMP Certified · Control microbiológico activo</p>
          </div>
        </div>

        <div class="fac-slide" data-index="4">
          <div class="fac-slide-bg">
            <img src="IMG/sectores/alimentacion-funcional.jpg"
                 alt="Líneas multipropósito de alta flexibilidad — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Alimentación Funcional</span>
            <h3 class="fac-slide-title">Líneas multipropósito de alta flexibilidad</h3>
            <p class="fac-slide-dato">Cambios rápidos de formato · Lote piloto a gran serie</p>
          </div>
        </div>

        <div class="fac-slide" data-index="5">
          <div class="fac-slide-bg">
            <img src="IMG/sectores/veterinaria.jpg"
                 alt="Producción para alimentación animal — Mix Pak System"
                 class="fac-slide-img" loading="lazy">
            <div class="fac-slide-overlay"></div>
          </div>
          <div class="fac-slide-content">
            <span class="fac-slide-tag">Veterinaria</span>
            <h3 class="fac-slide-title">Producción para alimentación animal</h3>
            <p class="fac-slide-dato">Doypacks y sachets con alta barrera</p>
          </div>
        </div>

      </div><!-- /fac-slides -->

      <!-- Flechas -->
      <button class="fac-arrow fac-arrow--prev" aria-label="Slide anterior">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"/>
        </svg>
      </button>
      <button class="fac-arrow fac-arrow--next" aria-label="Slide siguiente">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </button>

      <!-- Barra de progreso -->
      <div class="fac-progress-bar">
        <div class="fac-progress-fill" id="facProgress"></div>
      </div>

      <!-- Contador de slides -->
      <div class="fac-counter" aria-live="polite">
        <span id="facCurrent">01</span>
        <span class="fac-counter-sep">/</span>
        <span class="fac-counter-total">06</span>
      </div>

    </div><!-- /fac-carousel -->

  </section>"""
content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

# 2. Replace the CSS Block
old_css_pattern = r'    /\* ===================================================\n       FACILITIES - Corporate Locations Info Block\n       =================================================== \*/\n    \.facilities \{.*?\n      \.fac-data-sep \{\n        display: none;\n      \}\n    \}'

new_css = """    /* ===================================================
       FACILITIES - Corporate Locations Info Block
       =================================================== */
    .facilities {
      background: var(--bg);
      padding: 100px 0 0;
      border-bottom: 1px solid var(--border);
    }

    .fac-header {
      text-align: center;
      margin-bottom: 56px;
      padding: 0 24px;
    }

    .fac-header .section-desc {
      max-width: 560px;
    }

    /* ── Carrusel contenedor ── */
    .fac-carousel {
      position: relative;
      width: 100%;
      height: 560px;
      overflow: hidden;
      cursor: pointer;
    }

    /* ── Slides wrapper ── */
    .fac-slides {
      position: relative;
      width: 100%;
      height: 100%;
    }

    /* ── Slide individual ── */
    .fac-slide {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      clip-path: inset(0 100% 0 0);
      pointer-events: none;
      z-index: 1;
    }

    .fac-slide.is-active {
      clip-path: inset(0 0% 0 0);
      pointer-events: auto;
      z-index: 2;
    }

    /* Transición de entrada: wipe */
    .fac-slide.entering {
      animation: slideWipeIn 0.7s cubic-bezier(0.77, 0, 0.175, 1) forwards;
      z-index: 3;
    }

    /* Transición de salida: wipe out hacia la izquierda */
    .fac-slide.leaving {
      animation: slideWipeOut 0.7s cubic-bezier(0.77, 0, 0.175, 1) forwards;
      z-index: 2;
    }

    @keyframes slideWipeIn {
      from { clip-path: inset(0 100% 0 0); }
      to   { clip-path: inset(0 0% 0 0); }
    }

    @keyframes slideWipeOut {
      from { clip-path: inset(0 0% 0 0); }
      to   { clip-path: inset(0 0% 0 100%); }
    }

    /* ── Imagen de fondo con Ken Burns ── */
    .fac-slide-bg {
      position: absolute;
      inset: 0;
      overflow: hidden;
    }

    .fac-slide-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      transform: scale(1.0);
      transition: none;
      will-change: transform;
    }

    /* Ken Burns: solo en el slide activo */
    .fac-slide.is-active .fac-slide-img,
    .fac-slide.entering .fac-slide-img {
      transform: scale(1.08);
      transition: transform 5.7s linear;
    }

    /* ── Overlay ── */
    .fac-slide-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(
         135deg,
         rgba(0,0,102,0.82) 0%,
         rgba(6,12,36,0.55) 50%,
         rgba(0,0,102,0.75) 100%
       );
    }

    /* ── Contenido de texto ── */
    .fac-slide-content {
      position: absolute;
      bottom: 40px;
      left: 40px;
      z-index: 2;
      max-width: 600px;
    }
    .fac-slide-tag {
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      color: var(--gold);
      text-transform: uppercase;
      margin-bottom: 12px;
      display: block;
    }
    .fac-slide-title {
      font-family: 'DM Serif Display', serif;
      font-size: 2.4rem;
      color: #fff;
      line-height: 1.1;
      margin-bottom: 16px;
    }
    .fac-slide-dato {
      font-size: 0.95rem;
      color: rgba(255,255,255,0.8);
      margin: 0;
    }

    /* ── Progress Bar ── */
    .fac-progress-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: rgba(255,255,255,0.2);
      z-index: 10;
    }
    .fac-progress-fill {
      height: 100%;
      background: var(--gold);
      width: 0%;
    }
    .fac-progress-fill.animating {
      width: 100%;
      transition: width 5s linear;
    }

    /* ── Counter ── */
    .fac-counter {
      position: absolute;
      bottom: 40px;
      right: 40px;
      z-index: 10;
      color: #fff;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 1.1rem;
      display: flex;
      gap: 8px;
    }
    .fac-counter-sep { color: rgba(255,255,255,0.4); }
    .fac-counter-total { color: rgba(255,255,255,0.6); }

    /* ── Arrows ── */
    .fac-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(0,0,102,0.6);
      border: 1px solid rgba(255,255,255,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      opacity: 0;
      transition: opacity 0.3s ease, background 0.3s ease;
    }
    .fac-arrow:hover {
      background: rgba(0,0,102,0.9);
    }
    .fac-carousel:hover .fac-arrow {
      opacity: 1;
    }
    .fac-arrow--prev { left: 24px; }
    .fac-arrow--next { right: 24px; }

    @media (max-width: 768px) {
      .fac-slide-title { font-size: 1.8rem; }
      .fac-slide-content { bottom: 32px; left: 24px; }
      .fac-counter { bottom: 32px; right: 24px; }
      .fac-arrow--prev { left: 16px; }
      .fac-arrow--next { right: 16px; }
    }"""
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

# 3. Add JS
# Look for <script> block at the end of the body, just before </body>
js_code = """
  <script>
  // ===================== FACILITIES CAROUSEL =====================
  const facSlides = document.querySelectorAll('.fac-slide');
  if (facSlides.length > 0) {
    const totalFac = facSlides.length;
    let currentFac = 0;
    let facTimer;
    const facFill = document.getElementById('facProgress');
    const facCurrentCount = document.getElementById('facCurrent');
    const btnFacPrev = document.querySelector('.fac-arrow--prev');
    const btnFacNext = document.querySelector('.fac-arrow--next');
    const facCarousel = document.getElementById('facCarousel');

    function goToFacSlide(index) {
      const oldSlide = facSlides[currentFac];
      oldSlide.classList.remove('is-active', 'entering', 'leaving');
      oldSlide.classList.add('leaving');

      currentFac = (index + totalFac) % totalFac;
      const newSlide = facSlides[currentFac];
      
      facSlides.forEach(s => {
        if (s !== oldSlide && s !== newSlide) {
          s.classList.remove('is-active', 'entering', 'leaving');
        }
      });

      newSlide.classList.remove('leaving');
      newSlide.classList.add('is-active', 'entering');
      
      facCurrentCount.textContent = String(currentFac + 1).padStart(2, '0');
      
      resetFacProgress();
    }

    function nextFacSlide() { goToFacSlide(currentFac + 1); }
    function prevFacSlide() { goToFacSlide(currentFac - 1); }

    function resetFacProgress() {
      clearInterval(facTimer);
      facFill.classList.remove('animating');
      // force reflow
      void facFill.offsetWidth;
      facFill.classList.add('animating');
      facTimer = setInterval(nextFacSlide, 5000);
    }

    btnFacNext.addEventListener('click', (e) => {
      e.stopPropagation();
      nextFacSlide();
    });
    
    btnFacPrev.addEventListener('click', (e) => {
      e.stopPropagation();
      prevFacSlide();
    });

    // Initialize
    facSlides[0].classList.add('is-active', 'entering');
    facCurrentCount.textContent = '01';
    resetFacProgress();
  }
  </script>
"""
content = content.replace('</body>', js_code + '\\n</body>')

with open('/Users/anabelen/mixpaksystem/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
