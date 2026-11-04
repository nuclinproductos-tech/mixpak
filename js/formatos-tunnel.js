/*
 * Formatos · túnel en perspectiva (home ES).
 * Reproduce "Perspective Tunnel Hero" (21st.dev/@daiwiikharihar, MIT) en vanilla JS:
 * los formatos salen del fondo distribuidos en espiral áurea (137,5°) y vuelan hacia la cámara
 * en el eje Z según el progreso del scroll (suavizado con muelle), con paralaje del cursor.
 * Mismos parámetros que el original: escalonado i/N·0,45 + tramo 0,55, Z −1700→500 (móvil −1200→350),
 * opacidad [0, .18, .82, .98] → [0, 1, 1, 0], título 0,7→1→1,35, perspectiva 1200 (móvil 900).
 * Lee las fichas del HTML (.le-card); sin JS o sin <dialog> queda la cuadrícula estática.
 */
(function () {
  'use strict';

  var section = document.querySelector('.ft-section');
  if (!section) return;
  var scroller = section.querySelector('.ft-scroller');
  var stage = section.querySelector('.ft-stage');
  var tunnel = section.querySelector('.ft-tunnel');
  var head = section.querySelector('.ft-head');
  var hint = section.querySelector('.ft-hint');
  var dialog = section.querySelector('.le-dialog');
  var sheet = dialog && dialog.querySelector('.le-sheet');
  var sheetBody = dialog && dialog.querySelector('.le-sheet-body');
  var cards = Array.prototype.slice.call(section.querySelectorAll('.le-card'));
  if (!scroller || !stage || !tunnel || !cards.length || !dialog || typeof dialog.showModal !== 'function') return;

  var mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var hoverable = window.matchMedia('(hover: hover) and (pointer: fine)');
  var hint_ = section.getAttribute('data-hint') || '';
  var N = cards.length;

  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function clamp(v, a, b) { return v < a ? a : v > b ? b : v; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  // interpolación por tramos, como useTransform de framer-motion
  function map(v, xs, ys) {
    if (v <= xs[0]) return ys[0];
    for (var i = 1; i < xs.length; i++) {
      if (v <= xs[i]) return lerp(ys[i - 1], ys[i], (v - xs[i - 1]) / (xs[i] - xs[i - 1]));
    }
    return ys[ys.length - 1];
  }

  /* ---------- Tarjetas del túnel (a partir de las fichas) ---------- */
  tunnel.setAttribute('role', 'group');
  var items = cards.map(function (card, i) {
    var name = card.querySelector('.le-card-name').textContent.trim();
    var b = el('button', 'ft-card');
    b.type = 'button';
    b.setAttribute('aria-label', name + (hint_ ? ', ' + hint_ : ''));
    var inner = el('span', 'ft-card-inner');
    var img = el('img');
    img.src = card.getAttribute('data-card-src') || card.querySelector('img').getAttribute('src');
    img.alt = '';
    img.width = +card.getAttribute('data-card-w') || 240;
    img.height = +card.getAttribute('data-card-h') || 300;
    img.decoding = 'async';
    img.draggable = false;
    inner.appendChild(img);
    inner.appendChild(el('span', 'ft-card-label', name));
    b.appendChild(inner);
    b.addEventListener('click', function () { openSheet(i, b); });
    b.addEventListener('focus', function () { if (b.matches(':focus-visible')) focusCard(i); });
    tunnel.appendChild(b);
    var a = i * 137.5 * Math.PI / 180;
    return {
      btn: b,
      cos: Math.cos(a),
      sin: Math.sin(a),
      rfx: 0.28 + (i % 3) * 0.08,
      rfy: 0.26 + (i % 2) * 0.09,
      rot: (i % 2 === 0 ? 1 : -1) * (3 + (i % 5) * 2),
      start: i / N * 0.45
    };
  });

  section.classList.add('ft-on');

  /* ---------- Estado ---------- */
  var W = 1440, H = 900, mobile = false, top = 0, span = 1, staticMode = false;
  var target = 0, prog = 0, vel = 0;                 // progreso del scroll y muelle (80 / 30)
  var ptx = 0, pty = 0, px = 0, py = 0, pvx = 0, pvy = 0;   // paralaje del cursor (60 / 25, masa 0,5)
  var raf = 0, last = 0, inView = false;

  function headerH() {
    var h = document.getElementById('site-header');
    var bar = document.querySelector('.topbar');
    var t = h ? h.offsetHeight : 0;
    if (bar && bar.offsetParent !== null && getComputedStyle(bar).position !== 'static') t += bar.offsetHeight;
    return t;
  }

  function measure() {
    staticMode = mqReduce.matches;
    section.classList.toggle('ft-static', staticMode);
    top = staticMode ? 0 : headerH();
    section.style.setProperty('--ft-top', top + 'px');
    W = stage.clientWidth;
    H = stage.clientHeight;
    mobile = window.innerWidth < 768;
    var cw = mobile ? clamp(W * 0.38, 130, 180) : clamp(W * 0.18, 180, 270);
    section.style.setProperty('--ft-card-w', cw.toFixed(0) + 'px');
    // recorrido del scroll mientras la escena está fijada (equivale al giro de rueda del original)
    span = staticMode ? 0 : Math.round(window.innerHeight * (mobile ? 2.4 : 2.8));
    scroller.style.height = staticMode ? '' : (stage.offsetHeight + span) + 'px';
    readScroll();
    if (staticMode) { prog = target; clearTransforms(); }
    render();
  }

  function readScroll() {
    if (staticMode || !span) { target = 0; return; }
    var r = scroller.getBoundingClientRect();
    target = clamp((top - r.top) / span, 0, 1);
  }

  function clearTransforms() {
    items.forEach(function (it) { it.btn.style.transform = ''; it.btn.style.opacity = ''; it.btn.classList.add('is-live'); });
    if (head) { head.style.transform = ''; head.style.opacity = ''; }
  }

  function render() {
    if (staticMode) return;
    var zFrom = mobile ? -1200 : -1700, zTo = mobile ? 350 : 500, par = mobile ? 20 : 45;
    for (var i = 0; i < items.length; i++) {
      var it = items[i];
      var y = clamp((prog - it.start) / 0.55, 0, 1);
      var z = lerp(zFrom, zTo, y);
      var op = map(y, [0, 0.18, 0.82, 0.98], [0, 1, 1, 0]);
      var x = it.cos * (W * it.rfx) - px * par;
      var yy = it.sin * (H * it.rfy) - py * par;
      var s = it.btn.style;
      s.transform = 'translate3d(calc(-50% + ' + x.toFixed(1) + 'px), calc(-50% + ' + yy.toFixed(1) + 'px), ' + z.toFixed(1) + 'px) rotateZ(' + it.rot + 'deg)';
      s.opacity = op.toFixed(3);
      s.zIndex = i + 1;
      it.btn.classList.toggle('is-live', op > 0.35);
    }
    if (head) {
      head.style.transform = 'scale(' + map(prog, [0, 0.5, 1], [0.7, 1, 1.35]).toFixed(4) + ')';
      head.style.opacity = map(prog, [0, 0.12, 0.85, 1], [0.25, 1, 1, 0]).toFixed(3);
    }
    if (hint) hint.style.opacity = map(prog, [0, 0.12], [1, 0]).toFixed(3);
  }

  // muelle amortiguado (integración semi-implícita en subpasos)
  function spring(x, v, to, k, c, m, dt) {
    var steps = Math.max(1, Math.ceil(dt / 0.008)), h = dt / steps;
    for (var i = 0; i < steps; i++) { v += ((k * (to - x) - c * v) / m) * h; x += v * h; }
    return [x, v];
  }

  function tick(t) {
    raf = 0;
    var dt = last ? Math.min((t - last) / 1000, 0.05) : 0.016;
    last = t;
    var r = spring(prog, vel, target, 80, 30, 1, dt); prog = r[0]; vel = r[1];
    var rx = spring(px, pvx, ptx, 60, 25, 0.5, dt); px = rx[0]; pvx = rx[1];
    var ry = spring(py, pvy, pty, 60, 25, 0.5, dt); py = ry[0]; pvy = ry[1];
    var settled = Math.abs(target - prog) < 1e-4 && Math.abs(vel) < 1e-4 &&
      Math.abs(ptx - px) < 1e-3 && Math.abs(pty - py) < 1e-3;
    if (settled) { prog = target; px = ptx; py = pty; vel = pvx = pvy = 0; }
    render();
    if (!settled) schedule(); else last = 0;
  }

  function schedule() {
    if (!raf && inView && !document.hidden && !staticMode) raf = requestAnimationFrame(tick);
  }

  window.addEventListener('scroll', function () { readScroll(); schedule(); }, { passive: true });
  window.addEventListener('resize', measure);
  if (mqReduce.addEventListener) mqReduce.addEventListener('change', measure);
  else if (mqReduce.addListener) mqReduce.addListener(measure);
  document.addEventListener('visibilitychange', function () { if (!document.hidden) schedule(); });

  window.addEventListener('pointermove', function (e) {
    if (!inView || !hoverable.matches || staticMode) return;
    ptx = (e.clientX / window.innerWidth - 0.5) * 2;
    pty = (e.clientY / window.innerHeight - 0.5) * 2;
    schedule();
  }, { passive: true });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (en) {
      inView = en[0].isIntersecting;
      if (inView) { readScroll(); schedule(); }
    }, { rootMargin: '200px 0px' }).observe(scroller);
  } else inView = true;

  // Teclado: al enfocar una tarjeta, el scroll lleva el túnel al momento en que esa tarjeta está en primer plano
  function focusCard(i) {
    if (staticMode || !span) return;
    var p = items[i].start + 0.55 * 0.55;
    var scTop = scroller.getBoundingClientRect().top + window.pageYOffset;
    window.scrollTo({ top: Math.round(scTop - top + p * span), behavior: 'auto' });
  }

  /* ---------- Ficha técnica (diálogo) ---------- */
  var returnTo = null, closing = false;
  var html = document.documentElement;

  function push(obj) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(obj);
  }

  function openSheet(i, opener) {
    if (closing) return;
    var card = cards[i];
    var clone = card.cloneNode(true);
    clone.removeAttribute('id');
    clone.classList.add('le-card--sheet');
    var title = clone.querySelector('.le-card-name');
    if (title) title.id = 'le-dialog-title';
    clone.setAttribute('aria-labelledby', 'le-dialog-title');
    var img = clone.querySelector('img');
    if (img) img.removeAttribute('loading');
    var cta = clone.querySelector('.le-cta');
    if (cta) cta.addEventListener('click', onCta);
    if (sheetBody.replaceChildren) sheetBody.replaceChildren(clone);
    else { sheetBody.innerHTML = ''; sheetBody.appendChild(clone); }
    sheetBody.scrollTop = 0;
    returnTo = opener || null;
    var sbw = window.innerWidth - html.clientWidth;
    html.style.overflow = 'hidden';
    if (sbw > 0) document.body.style.paddingRight = sbw + 'px';
    dialog.showModal();
    void sheet.offsetWidth;
    dialog.classList.add('is-open');
    push({ event: 'select_format', formato: card.getAttribute('data-nombre-es') });
  }

  function closeSheet(restoreFocus, done) {
    if (!dialog.open || closing) return;
    closing = true;
    dialog.classList.remove('is-open');
    var finished = false;
    function finish() {
      if (finished) return;
      finished = true;
      sheet.removeEventListener('transitionend', onEnd);
      dialog.close();
      html.style.overflow = '';
      document.body.style.paddingRight = '';
      closing = false;
      if (restoreFocus !== false && returnTo && document.contains(returnTo)) returnTo.focus({ preventScroll: true });
      if (done) done();
    }
    function onEnd(e) { if (e.target === sheet) finish(); }
    sheet.addEventListener('transitionend', onEnd);
    setTimeout(finish, mqReduce.matches ? 200 : 420);
  }

  dialog.addEventListener('cancel', function (e) { e.preventDefault(); closeSheet(); });   // Escape
  dialog.addEventListener('click', function (e) { if (e.target === dialog) closeSheet(); });
  var closeBtn = dialog.querySelector('.le-close');
  if (closeBtn) closeBtn.addEventListener('click', function () { closeSheet(); });

  // Foco atrapado dentro de la ficha
  dialog.addEventListener('keydown', function (e) {
    if (e.key !== 'Tab') return;
    var f = Array.prototype.filter.call(
      dialog.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'),
      function (n) { return n.offsetParent !== null || n === document.activeElement; });
    if (!f.length) return;
    var first = f[0], lastEl = f[f.length - 1];
    if (e.shiftKey && (document.activeElement === first || !dialog.contains(document.activeElement))) { e.preventDefault(); lastEl.focus(); }
    else if (!e.shiftKey && document.activeElement === lastEl) { e.preventDefault(); first.focus(); }
  });

  // CTA de la ficha → formulario comercial existente
  function onCta(e) {
    e.preventDefault();
    var formato = this.getAttribute('data-formato') || '';
    var hash = (this.getAttribute('href') || '').replace(/^#/, '');
    push({ event: 'format_cta_click', formato: formato });
    closeSheet(false, function () {
      var target = (hash && document.getElementById(hash)) || document.getElementById('cform');
      if (target) {
        var y = target.getBoundingClientRect().top + window.pageYOffset - 78;
        window.scrollTo({ top: y, behavior: mqReduce.matches ? 'auto' : 'smooth' });
      }
    });
  }

  measure();
  window.addEventListener('load', measure);
})();
