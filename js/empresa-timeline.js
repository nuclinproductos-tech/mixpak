/*
 * Empresa · Trayectoria: línea del tiempo horizontal (ES/EN/PT).
 * Mejora progresiva sobre el marcado existente (#trayectoria .timeline-track > .tl-item):
 *  - Escritorio: la sección se fija y el scroll vertical desplaza la pista en horizontal;
 *    el eje dorado se dibuja con el avance y cada hito despliega su tallo y su texto al llegar al centro.
 *  - Móvil, pantallas bajas y prefers-reduced-motion: la misma composición en vertical (eje a la izquierda).
 *  - Sin JS: se mantiene la lista vertical original.
 * Referencia de interacción: "Product Timeline" (21st.dev/@hyperiux, MIT). Reescrito en vanilla JS, sin GSAP ni Lenis.
 */
(function () {
  'use strict';

  var section = document.getElementById('trayectoria');
  var track = section && section.querySelector('.timeline-track');
  if (!track) return;
  var items = Array.prototype.slice.call(track.querySelectorAll('.tl-item'));
  if (!items.length) return;

  function el(tag, cls) { var n = document.createElement(tag); if (cls) n.className = cls; return n; }

  /* ---------- Montaje: se reutilizan los nodos originales (no hay contenido duplicado) ---------- */
  var years = items.map(function (it) { var y = it.querySelector('.tl-year'); return y ? y.textContent.trim() : ''; }).filter(Boolean);
  var eyebrow = section.querySelector('.section-head .eyebrow');

  var scroller = el('div', 'tlh-scroller');
  var pin = el('div', 'tlh-pin');
  var rail = el('div', 'tlh-rail');
  rail.setAttribute('role', 'list');
  if (track.getAttribute('aria-label')) rail.setAttribute('aria-label', track.getAttribute('aria-label'));

  var axis = el('div', 'tlh-axis'); axis.setAttribute('aria-hidden', 'true');
  var axisFill = el('div', 'tlh-axis-fill');
  axis.appendChild(axisFill);
  axis.appendChild(el('span', 'tlh-axis-end'));
  rail.appendChild(axis);

  var intro = el('div', 'tlh-intro');
  intro.setAttribute('aria-hidden', 'true');
  var introTitle = el('p', 'tlh-intro-title');
  introTitle.textContent = eyebrow ? eyebrow.textContent.trim() : '';
  var introYears = el('p', 'tlh-intro-years');
  introYears.textContent = years.length > 1 ? years[0] + ' — ' + years[years.length - 1] : (years[0] || '');
  intro.appendChild(introTitle);
  intro.appendChild(el('span', 'tlh-intro-dot'));
  intro.appendChild(introYears);
  rail.appendChild(intro);

  var marks = items.map(function (it, i) {
    var m = el('article', 'tlh-m ' + (i % 2 ? 'tlh-m--down' : 'tlh-m--up'));
    m.setAttribute('role', 'listitem');
    var content = it.querySelector('.tl-content');
    var photo = it.querySelector('.tl-photo');
    m.appendChild(el('span', 'tlh-stem'));
    m.appendChild(el('span', 'tlh-dot'));
    if (content) { content.classList.add('tlh-copy'); m.appendChild(content); }
    if (photo) { photo.classList.add('tlh-photo'); m.appendChild(photo); }
    rail.appendChild(m);
    return m;
  });

  pin.appendChild(rail);
  scroller.appendChild(pin);
  track.parentNode.insertBefore(scroller, track.nextSibling);
  track.parentNode.removeChild(track);
  // la pista ocupa todo el ancho: se saca del .container
  var container = scroller.parentNode;
  if (container && container.classList.contains('container') && container.parentNode === section) {
    section.appendChild(scroller);
  }
  section.classList.add('tlh-on');

  // las imágenes quedan fuera de pantalla en horizontal y "lazy" no las pediría a tiempo
  if ('IntersectionObserver' in window) {
    var near = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return;
      rail.querySelectorAll('img[loading="lazy"]').forEach(function (im) { im.loading = 'eager'; });
      near.disconnect();
    }, { rootMargin: '800px 0px' });
    near.observe(section);
  }

  /* ---------- Estado ---------- */
  var mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var mode = '';            // 'pin' | 'stack'
  var dist = 0;             // recorrido horizontal total (px)
  var railW = 0, vw = 0;
  var cur = 0, target = 0, raf = 0;
  var markX = [];           // centro de cada hito en la pista
  var lastTop = -1;         // alto de la cabecera fija en la última medición

  // alto estable de lo fijo arriba (barra superior visible + cabecera); no se lee en cada scroll
  // porque la cabecera anima su alto y una lectura a mitad de transición dejaría la sección mal fijada
  function headerH() {
    var h = document.getElementById('site-header');
    var bar = document.querySelector('.topbar');
    var t = h ? h.offsetHeight : 0;
    if (bar && bar.offsetParent !== null && getComputedStyle(bar).position !== 'static') t += bar.offsetHeight;
    else if (h) t = Math.max(t, Math.round(h.getBoundingClientRect().bottom));
    return t;
  }

  function wantPin() {
    return !mqReduce.matches && window.innerWidth >= 900 && window.innerHeight >= 700;
  }

  function measure() {
    var pinMode = wantPin();
    mode = pinMode ? 'pin' : 'stack';
    section.classList.toggle('tlh-pin-mode', pinMode);
    section.classList.toggle('tlh-stack-mode', !pinMode);
    lastTop = headerH();
    section.style.setProperty('--tlh-top', lastTop + 'px');
    vw = pin.clientWidth;
    rail.style.transform = '';
    railW = rail.scrollWidth;
    markX = marks.map(function (m) { return m.offsetLeft + 28; });
    dist = Math.max(0, railW - vw);
    scroller.style.height = pinMode ? (pin.offsetHeight + dist) + 'px' : '';
    if (!pinMode) { cur = target = 0; axisFill.style.transform = ''; }
    update(true);
  }

  // progreso de la sección fijada → desplazamiento objetivo
  function readScroll() {
    if (mode !== 'pin') return;
    var r = scroller.getBoundingClientRect();
    var span = scroller.offsetHeight - pin.offsetHeight;
    // la sección queda fijada cuando su borde llega bajo la cabecera (lastTop), no al borde de la ventana
    var p = span > 0 ? Math.min(1, Math.max(0, (lastTop - r.top) / span)) : 0;
    target = p * dist;
  }

  // Vertical: el eje se dibuja con el scroll y cada hito aparece al entrar en pantalla
  function paintStack() {
    var vh = window.innerHeight;
    var r = rail.getBoundingClientRect();
    var drawn = Math.min(1, Math.max(0, (vh * 0.72 - r.top) / Math.max(1, r.height)));
    axisFill.style.transform = 'scaleY(' + drawn.toFixed(4) + ')';
    for (var i = 0; i < marks.length; i++) {
      if (!marks[i].classList.contains('is-on') && marks[i].getBoundingClientRect().top < vh * 0.86) marks[i].classList.add('is-on');
    }
  }

  function paint() {
    if (mode !== 'pin') { paintStack(); return; }
    rail.style.transform = 'translate3d(' + (-cur).toFixed(1) + 'px,0,0)';
    // eje dibujado hasta algo más allá del centro de la pantalla
    // el trazo va algo por delante del centro y llega justo al punto final al acabar el recorrido
    var aL = axis.offsetLeft, aW = axis.offsetWidth || 1, lead = vw * 0.62;
    var k = dist ? cur / dist : 1;
    var drawn = cur + lead + k * (aL + aW - dist - lead);
    axisFill.style.transform = 'scaleX(' + Math.min(1, Math.max(0, (drawn - aL) / aW)).toFixed(4) + ')';
    for (var i = 0; i < marks.length; i++) {
      if (!marks[i].classList.contains('is-on') && markX[i] - cur < vw * 0.7) marks[i].classList.add('is-on');
    }
  }

  function loop() {
    raf = 0;
    var d = target - cur;
    cur += d * 0.14;               // suavizado tipo "smooth scroll", sin secuestrar la rueda
    if (Math.abs(d) < 0.5) cur = target;
    paint();
    if (cur !== target) raf = requestAnimationFrame(loop);
  }

  function update(now) {
    readScroll();
    if (now || mode !== 'pin') { cur = target; paint(); return; }
    if (!raf) raf = requestAnimationFrame(loop);
  }

  window.addEventListener('scroll', function () {
    if (mode === 'pin') update(); else paintStack();
  }, { passive: true });
  window.addEventListener('resize', function () { measure(); });
  if (mqReduce.addEventListener) mqReduce.addEventListener('change', measure);
  else if (mqReduce.addListener) mqReduce.addListener(measure);

  // las imágenes y las fuentes cambian el ancho real de la pista
  rail.addEventListener('load', measure, true);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
  window.addEventListener('load', measure);

  measure();
})();
