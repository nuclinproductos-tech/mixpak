/* Sectores · interacciones (sin dependencias)
   1. Productos: rejilla solo con CSS (sin JS).
   2. Anillo de formatos: gira con flechas, teclado, arrastre y scroll.
   3. Pista de proceso: el corredor avanza con el scroll y enciende cada fase. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v) { return Math.max(0, Math.min(1, v)); };
  var jobs = [];

  /* ---------- 2. Anillo de formatos ---------- */
  var ring = document.querySelector('[data-sx-ring]');
  if (ring) {
    var track = ring.querySelector('.sx-ring-track');
    var stage = ring.querySelector('.sx-ring-stage');
    var cards = ring.querySelectorAll('.sx-ring-card');
    var now = ring.querySelector('.sx-ring-now');
    var n = cards.length, step = 360 / n;
    var base = 0, drag = 0, scroll = 0, front = -1;
    var paint = function () {
      var r = base + drag + scroll;
      track.style.setProperty('--r', r.toFixed(2) + 'deg');
      var best = 0, bc = -2;
      for (var k = 0; k < n; k++) {
        var a = (k * step + r) * Math.PI / 180;
        var c = Math.cos(a);
        cards[k].style.setProperty('--f', (.18 + .82 * Math.max(0, c)).toFixed(3));
        if (c > bc) { bc = c; best = k; }
      }
      if (best !== front) {
        front = best;
        for (var m = 0; m < n; m++) cards[m].classList.toggle('is-front', m === best);
        if (now) {
          now.querySelector('b').textContent = cards[best].querySelector('figcaption').textContent;
          now.querySelector('span').textContent = (best < 9 ? '0' : '') + (best + 1) + ' / ' + (n < 10 ? '0' : '') + n;
        }
      }
    };
    var go = function (dir) { base -= dir * step; paint(); };
    ring.querySelector('[data-dir="-1"]').addEventListener('click', function () { go(-1); });
    ring.querySelector('[data-dir="1"]').addEventListener('click', function () { go(1); });
    ring.setAttribute('tabindex', '0');
    ring.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(-1); e.preventDefault(); }
      if (e.key === 'ArrowRight') { go(1); e.preventDefault(); }
    });
    /* Arrastre: al soltar, encaja en el formato más cercano */
    var x0 = null, moved = 0;
    stage.addEventListener('pointerdown', function (e) {
      x0 = e.clientX; moved = 0; ring.classList.add('is-dragging');
    });
    window.addEventListener('pointermove', function (e) {
      if (x0 === null) return;
      moved = Math.abs(e.clientX - x0);
      drag = (e.clientX - x0) * .35;
      paint();
    });
    window.addEventListener('pointerup', function () {
      if (x0 === null) return;
      x0 = null;
      ring.classList.remove('is-dragging');
      base = Math.round((base + drag) / step) * step;
      drag = 0;
      paint();
    });
    /* Clic en una tarjeta lateral: la trae al frente */
    for (var c = 0; c < n; c++) {
      (function (i) {
        cards[i].addEventListener('click', function () {
          if (moved > 6) return;
          var target = -i * step;
          var cur = base + scroll;
          var diff = ((target - cur) % 360 + 540) % 360 - 180;
          base += Math.round(diff / step) * step;
          paint();
        });
      })(c);
    }
    if (!reduce) {
      var stopT;
      jobs.push(function (vh) {
        var r = ring.getBoundingClientRect();
        var t = clamp((vh - r.top) / (vh + r.height));
        scroll = (t - .5) * -1.5 * step;
        ring.classList.add('is-scrolling');
        clearTimeout(stopT);
        stopT = setTimeout(function () { ring.classList.remove('is-scrolling'); }, 120);
        paint();
      });
    }
    paint();
    var ready = function () { setTimeout(function () { ring.classList.add('is-ready'); }, 60); };
    if (document.readyState === 'complete') ready(); else window.addEventListener('load', ready);
  }

  /* ---------- 3. Pista de proceso ---------- */
  var lane = document.querySelector('[data-sx-track]');
  if (lane) {
    var laps = lane.querySelectorAll('.sx-lap');
    jobs.push(function (vh) {
      var r = lane.getBoundingClientRect();
      /* 0 cuando la pista entra al 80 % de la pantalla; 1 cuando su final llega al 45 % */
      var p = reduce ? 1 : clamp((vh * .8 - r.top) / (r.height + vh * .35));
      lane.style.setProperty('--p', p.toFixed(3));
      for (var k = 0; k < laps.length; k++) laps[k].classList.toggle('is-on', p >= k / (laps.length - 1) - .02);
    });
  }

  /* ---------- Bucle de scroll compartido ---------- */
  var ticking = false;
  var run = function () {
    ticking = false;
    var vh = window.innerHeight;
    for (var j = 0; j < jobs.length; j++) jobs[j](vh);
  };
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(run); }
  }, { passive: true });
  window.addEventListener('resize', run);
  run();
})();
