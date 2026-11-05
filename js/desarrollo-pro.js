/* Desarrollo · interacciones (sin dependencias)
   1. Marcos dinámicos: el marco activo crece (columnas y filas de la rejilla).
   2. Galería elástica: el panel activo se expande; en táctil, el primer toque
      abre el panel y el segundo sigue el enlace.
   3. Carrusel en arco: flechas, pasos, teclado y arrastre.
   4. Despliegue: --p (0 a 1) según la posición de la sección en pantalla. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var touch = window.matchMedia && window.matchMedia('(hover: none)').matches;
  /* Las transiciones se activan tras la carga para que no se disparen al aplicar la hoja */
  var ready = function () {
    var els = document.querySelectorAll('[data-dv-frames],[data-dv-elastic]');
    setTimeout(function () { for (var r = 0; r < els.length; r++) els[r].classList.add('is-ready'); }, 60);
  };
  if (document.readyState === 'complete') ready(); else window.addEventListener('load', ready);

  /* ---------- 1. Marcos dinámicos ---------- */
  var frames = document.querySelector('[data-dv-frames]');
  if (frames) {
    var fs = frames.querySelectorAll('.dv-frame');
    var setFrame = function (i) {
      for (var k = 0; k < fs.length; k++) fs[k].classList.toggle('is-active', k === i);
      var col = i % 3, row = Math.floor(i / 3);
      var c = ['1fr', '1fr', '1fr']; c[col] = '2.3fr';
      var r = ['1fr', '1fr']; r[row] = '1.55fr';
      frames.style.setProperty('--cols', c.join(' '));
      frames.style.setProperty('--rows', r.join(' '));
    };
    for (var i = 0; i < fs.length; i++) {
      (function (i) {
        fs[i].addEventListener('mouseenter', function () { setFrame(i); });
        fs[i].addEventListener('focus', function () { setFrame(i); });
        fs[i].addEventListener('click', function () { setFrame(i); });
      })(i);
    }
  }

  /* ---------- 2. Galería elástica ---------- */
  var gal = document.querySelector('[data-dv-elastic]');
  if (gal) {
    var ps = gal.querySelectorAll('.dv-panel');
    var setPanel = function (p) {
      for (var k = 0; k < ps.length; k++) ps[k].classList.toggle('is-active', ps[k] === p);
    };
    for (var j = 0; j < ps.length; j++) {
      ps[j].addEventListener('mouseenter', function () { setPanel(this); });
      ps[j].addEventListener('focus', function () { setPanel(this); });
      ps[j].addEventListener('click', function (e) {
        if ((touch || window.innerWidth <= 820) && !this.classList.contains('is-active')) {
          e.preventDefault();
          setPanel(this);
        }
      });
    }
  }

  /* ---------- 3. Carrusel en arco ---------- */
  var arc = document.querySelector('[data-dv-arc]');
  if (arc) {
    var cards = arc.querySelectorAll('.dv-arc-card');
    var tabs = arc.querySelectorAll('[data-go]');
    var prev = arc.querySelector('[data-dir="-1"]');
    var next = arc.querySelector('[data-dir="1"]');
    var stage = arc.querySelector('.dv-arc-stage');
    var cur = 0, n = cards.length;
    var go = function (i) {
      cur = Math.max(0, Math.min(n - 1, i));
      for (var k = 0; k < n; k++) {
        var o = k - cur, a = Math.abs(o);
        cards[k].style.setProperty('--o', o);
        cards[k].style.setProperty('--a', a);
        cards[k].classList.toggle('is-active', o === 0);
        cards[k].classList.toggle('is-far', a > 2);
        cards[k].setAttribute('aria-hidden', o === 0 ? 'false' : 'true');
      }
      for (var t = 0; t < tabs.length; t++) {
        if (t === cur) tabs[t].setAttribute('aria-current', 'step');
        else tabs[t].removeAttribute('aria-current');
      }
      prev.disabled = cur === 0;
      next.disabled = cur === n - 1;
    };
    prev.addEventListener('click', function () { go(cur - 1); });
    next.addEventListener('click', function () { go(cur + 1); });
    for (var t = 0; t < tabs.length; t++) {
      tabs[t].addEventListener('click', function () { go(+this.getAttribute('data-go')); });
    }
    for (var c = 0; c < cards.length; c++) {
      cards[c].addEventListener('click', function () {
        if (!dragged) go(+this.getAttribute('data-i'));
      });
    }
    arc.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(cur - 1); e.preventDefault(); }
      if (e.key === 'ArrowRight') { go(cur + 1); e.preventDefault(); }
    });
    var x0 = null, dragged = false;
    stage.addEventListener('pointerdown', function (e) {
      x0 = e.clientX; dragged = false; stage.classList.add('is-dragging');
    });
    window.addEventListener('pointerup', function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0;
      if (Math.abs(dx) > 40) { dragged = true; go(cur + (dx < 0 ? 1 : -1)); }
      x0 = null; stage.classList.remove('is-dragging');
      setTimeout(function () { dragged = false; }, 0);
    });
    go(0);
  }

  /* ---------- 4. Despliegue con el scroll ---------- */
  var scale = document.querySelector('.des-scale.dv');
  var unfurl = scale && scale.querySelector('[data-dv-unfurl]');
  if (unfurl) {
    var folds = unfurl.querySelectorAll('.dv-fold');
    var points = scale.querySelector('[data-dv-points]');
    var items = points ? points.querySelectorAll('li') : [];
    if (!reduce) {
      var ticking = false;
      var update = function () {
        ticking = false;
        var r = unfurl.getBoundingClientRect(), vh = window.innerHeight;
        /* 0 cuando el borde superior entra por abajo; 1 cuando el centro llega al 55 % */
        var p = (vh - r.top) / (vh * 0.45 + r.height * 0.5);
        p = Math.max(0, Math.min(1, p));
        p = 1 - Math.pow(1 - p, 2);
        scale.style.setProperty('--p', p.toFixed(3));
      };
      var onScroll = function () {
        if (!ticking) { ticking = true; requestAnimationFrame(update); }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll);
      update();
    }
    var on = function (i) {
      for (var k = 0; k < folds.length; k++) folds[k].classList.toggle('is-on', k === i);
      for (var m = 0; m < items.length; m++) items[m].classList.toggle('is-on', m === i);
      if (points) points.classList.toggle('has-on', i > -1);
    };
    var bind = function (list) {
      for (var q = 0; q < list.length; q++) {
        (function (q) {
          list[q].addEventListener('mouseenter', function () { on(q); });
          list[q].addEventListener('mouseleave', function () { on(-1); });
        })(q);
      }
    };
    bind(folds); bind(items);
  }
})();
