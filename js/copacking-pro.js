/* Copacking · interacciones (sin dependencias)
   1. Catálogo: contador de formatos, reordenación animada (FLIP) e inclinación.
   2. Troquel: la línea de corte se dibuja y la foto se revela con el scroll.
   3. Bicompartimento: las dos mitades se acercan y se sellan con el scroll.
   4. Proceso: la cinta avanza en horizontal mientras la sección queda fijada. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hover = window.matchMedia && window.matchMedia('(hover: hover)').matches;
  var clamp = function (v) { return Math.max(0, Math.min(1, v)); };
  var ease = function (p) { return 1 - Math.pow(1 - p, 3); };
  var jobs = [];

  /* ---------- 1. Catálogo ---------- */
  var cat = document.querySelector('.cpx-cat');
  if (cat) {
    var items = cat.querySelectorAll('.env3-item[data-kind]');
    var count = cat.querySelector('.cpx-count b');
    var filters = cat.querySelectorAll('.env3-filter');
    var rects = null;
    for (var f = 0; f < filters.length; f++) {
      /* Fase de captura: se miden las posiciones antes de que el filtro original oculte tarjetas */
      filters[f].addEventListener('click', function () {
        if (reduce) return;
        rects = [];
        for (var k = 0; k < items.length; k++) {
          rects.push(items[k].classList.contains('is-hidden') ? null : items[k].getBoundingClientRect());
        }
      }, true);
      filters[f].addEventListener('click', function () {
        var shown = 0;
        for (var k = 0; k < items.length; k++) {
          var it = items[k];
          if (it.classList.contains('is-hidden')) continue;
          shown++;
          if (!rects) continue;
          var was = rects[k];
          if (!was) {
            it.classList.remove('is-entering');
            void it.offsetWidth;
            it.classList.add('is-entering');
            continue;
          }
          var now = it.getBoundingClientRect();
          var dx = was.left - now.left, dy = was.top - now.top;
          if (!dx && !dy) continue;
          it.animate([{ transform: 'translate(' + dx + 'px,' + dy + 'px)' }, { transform: 'none' }],
            { duration: 520, easing: 'cubic-bezier(.22,1,.36,1)' });
        }
        rects = null;
        if (count) count.textContent = shown;
      });
    }
    if (hover && !reduce) {
      for (var t = 0; t < items.length; t++) {
        items[t].addEventListener('pointermove', function (e) {
          var r = this.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
          this.style.setProperty('--rx', (x * 7).toFixed(2) + 'deg');
          this.style.setProperty('--ry', (y * -7).toFixed(2) + 'deg');
        });
        items[t].addEventListener('pointerleave', function () {
          this.style.removeProperty('--rx');
          this.style.removeProperty('--ry');
        });
      }
    }
  }

  /* ---------- 2. Troquel ---------- */
  var die = document.querySelector('[data-cpx-die]');
  if (die && !reduce) {
    jobs.push(function (vh) {
      var r = die.getBoundingClientRect();
      /* 0 cuando asoma por abajo; 1 cuando su centro llega al 55 % de la pantalla */
      var p = clamp((vh - r.top) / (vh * .45 + r.height * .5));
      die.style.setProperty('--p', ease(p).toFixed(3));
    });
    if (hover) {
      var photo = die.querySelector('.cpx-die-photo');
      die.addEventListener('pointermove', function (e) {
        var r = die.getBoundingClientRect();
        photo.style.setProperty('--mx', (((e.clientX - r.left) / r.width - .5) * -16).toFixed(1) + 'px');
        photo.style.setProperty('--my', (((e.clientY - r.top) / r.height - .5) * -12).toFixed(1) + 'px');
      });
      die.addEventListener('pointerleave', function () {
        photo.style.removeProperty('--mx');
        photo.style.removeProperty('--my');
      });
    }
  }

  /* ---------- 3. Bicompartimento ---------- */
  var seal = document.querySelector('[data-cpx-seal]');
  if (seal && !reduce) {
    jobs.push(function (vh) {
      if (window.innerWidth <= 960) { seal.style.setProperty('--s', 1); return; }
      var r = seal.getBoundingClientRect();
      var s = clamp((vh - r.top) / (vh * .35 + r.height * .45));
      seal.style.setProperty('--s', ease(s).toFixed(3));
    });
  }

  /* ---------- 4. Proceso: cinta horizontal ---------- */
  var conv = document.querySelector('[data-cpx-conveyor]');
  if (conv) {
    var pin = conv.querySelector('.cpx-pin');
    var track = conv.querySelector('.cpx-track');
    var stations = conv.querySelectorAll('.cpx-station');
    var ticks = conv.querySelectorAll('.cpx-tick');
    var dist = 0, cur = -1;
    var mark = function (a) {
      if (a === cur) return;
      cur = a;
      for (var k = 0; k < stations.length; k++) {
        stations[k].classList.toggle('is-on', k === a);
        if (ticks[k] && !dist) ticks[k].classList.toggle('is-on', k <= a);
      }
    };
    var measure = function () {
      if (window.innerWidth <= 820 || reduce) {
        dist = 0;
        conv.style.removeProperty('--h');
        track.style.removeProperty('--x');
        return;
      }
      dist = Math.max(0, track.scrollWidth - window.innerWidth);
      conv.style.setProperty('--h', (pin.offsetHeight + dist) + 'px');
    };
    jobs.push(function (vh) {
      if (!dist) {
        /* Sin fijado: la estación activa es la más cercana al centro de la pantalla */
        var best = 0, bd = Infinity;
        for (var k = 0; k < stations.length; k++) {
          var r = stations[k].getBoundingClientRect();
          var d = Math.abs(r.top + r.height / 2 - vh / 2) + Math.abs(r.left + r.width / 2 - window.innerWidth / 2);
          if (d < bd) { bd = d; best = k; }
        }
        mark(best);
        return;
      }
      var p = clamp(-conv.getBoundingClientRect().top / dist);
      track.style.setProperty('--x', (-p * dist).toFixed(1) + 'px');
      conv.style.setProperty('--cx-p', p.toFixed(3));
      mark(Math.min(stations.length - 1, Math.round(p * (stations.length - 1))));
      /* Los hitos se encienden cuando la cinta dorada los alcanza */
      for (var q = 0; q < ticks.length; q++) ticks[q].classList.toggle('is-on', p >= q / (ticks.length - 1) - .02);
    });
    measure();
    window.addEventListener('load', measure);
    window.addEventListener('resize', measure);
    track.addEventListener('scroll', function () { run(); }, { passive: true });
  }

  /* ---------- Bucle de scroll compartido ---------- */
  var ticking = false;
  var run = function () {
    ticking = false;
    var vh = window.innerHeight;
    for (var j = 0; j < jobs.length; j++) jobs[j](vh);
  };
  var onScroll = function () {
    if (!ticking) { ticking = true; requestAnimationFrame(run); }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  run();
})();
