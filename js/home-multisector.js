/* Home · Capacidad multisector: explorador de sectores (sin dependencias)
   Pasar el ratón o enfocar un sector cambia el escenario. Mientras nadie
   interactúa y la sección está a la vista, recorre los sectores solo. */
(function () {
  var root = document.querySelector('.msx');
  if (!root) return;
  var rows = root.querySelectorAll('.msx-row');
  var shots = root.querySelectorAll('.msx-shot');
  if (!rows.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var TOUR = 3600, cur = -1, timer = 0, visible = false, stopped = reduce;
  root.style.setProperty('--tour', TOUR + 'ms');

  var shotFor = function (k) {
    for (var i = 0; i < shots.length; i++) if (shots[i].getAttribute('data-k') === k) return shots[i];
    return shots[0];
  };

  function show(i) {
    if (i === cur) return;
    var next = i < 0 ? shots[0] : shotFor(rows[i].getAttribute('data-k'));
    for (var s = 0; s < shots.length; s++) {
      var on = shots[s] === next, was = shots[s].classList.contains('is-on');
      shots[s].classList.toggle('is-on', on);
      shots[s].classList.toggle('is-out', !on && was);
    }
    /* Las que salieron vuelven a esperar por la derecha sin animarse */
    setTimeout(function () {
      for (var s = 0; s < shots.length; s++) {
        if (!shots[s].classList.contains('is-out')) continue;
        shots[s].style.transition = 'none';
        shots[s].classList.remove('is-out');
        void shots[s].offsetWidth;
        shots[s].style.transition = '';
      }
    }, 800);
    for (var r = 0; r < rows.length; r++) rows[r].classList.toggle('is-on', r === i);
    cur = i;
  }

  function tick() {
    clearTimeout(timer);
    if (stopped || !visible) { root.classList.remove('is-touring'); return; }
    root.classList.remove('is-touring');
    show((cur + 1) % rows.length);
    void root.offsetWidth;
    root.classList.add('is-touring');
    timer = setTimeout(tick, TOUR);
  }

  function take(i) {
    stopped = true;
    clearTimeout(timer);
    root.classList.remove('is-touring');
    show(i);
  }

  for (var k = 0; k < rows.length; k++) {
    (function (i) {
      rows[i].addEventListener('pointerenter', function (e) { if (e.pointerType !== 'touch') take(i); });
      rows[i].addEventListener('focus', function () { take(i); });
    })(k);
  }

  if (!stopped && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) {
      var v = en[0].isIntersecting;
      if (v === visible) return;
      visible = v;
      if (visible) timer = setTimeout(tick, 1400); else { clearTimeout(timer); root.classList.remove('is-touring'); }
    }, { threshold: .45 }).observe(root.querySelector('[data-msx-stage]'));
  }
})();
