/* Fabricación · interacciones (sin dependencias)
   1. Línea en profundidad: la fase que cruza el centro de la pantalla
      pasa al frente; las siguientes esperan detrás, las anteriores salen.
   2. Galería elástica de matrices: hover, foco, clic y teclado. */
(function () {
  /* ---------- 1. Línea en profundidad ---------- */
  var line = document.querySelector('.fx-line');
  if (line) {
    var steps = line.querySelectorAll('.fx-step');
    var shots = line.querySelectorAll('.fx-shot');
    var counter = line.querySelector('.fx-counter b');
    var stage = line.querySelector('.fx-stage');
    var n = steps.length, cur = -1;
    var set = function (a) {
      if (a === cur) return;
      cur = a;
      for (var k = 0; k < n; k++) {
        var d = k - a;
        steps[k].classList.toggle('is-active', d === 0);
        if (shots[k]) {
          shots[k].style.setProperty('--d', Math.max(d, 0));
          shots[k].classList.toggle('is-past', d < 0);
          shots[k].classList.toggle('is-far', d > 3);
        }
      }
      if (counter) counter.textContent = (a < 9 ? '0' : '') + (a + 1);
      if (stage) stage.style.setProperty('--fx-progress', ((a + 1) / n * 100) + '%');
    };
    set(0);
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) set(+e.target.getAttribute('data-i'));
        });
      }, { rootMargin: '-48% 0px -48% 0px' });
      for (var s = 0; s < n; s++) io.observe(steps[s]);
    }
  }

  /* ---------- 2. Galería elástica ---------- */
  var gal = document.querySelector('[data-fx-elastic]');
  if (gal) {
    var ps = gal.querySelectorAll('.fx-panel');
    var open = function (p) {
      for (var k = 0; k < ps.length; k++) {
        var on = ps[k] === p;
        ps[k].classList.toggle('is-active', on);
        ps[k].setAttribute('aria-expanded', on ? 'true' : 'false');
      }
    };
    var hover = window.matchMedia && window.matchMedia('(hover: hover)').matches;
    for (var j = 0; j < ps.length; j++) {
      if (hover) ps[j].addEventListener('mouseenter', function () { if (window.innerWidth > 820) open(this); });
      ps[j].addEventListener('focus', function () { open(this); });
      ps[j].addEventListener('click', function () { open(this); });
      ps[j].addEventListener('keydown', function (e) {
        var idx = Array.prototype.indexOf.call(ps, this);
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); ps[Math.min(ps.length - 1, idx + 1)].focus(); }
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); ps[Math.max(0, idx - 1)].focus(); }
      });
    }
    var ready = function () { setTimeout(function () { gal.classList.add('is-ready'); }, 60); };
    if (document.readyState === 'complete') ready(); else window.addEventListener('load', ready);
  }
})();
