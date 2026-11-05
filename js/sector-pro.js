/* Sectores · interacciones (sin dependencias)
   1. Productos: rejilla solo con CSS (sin JS).
   2. Formatos: estantería solo con CSS (sin JS).
   3. Pista de proceso: el corredor avanza con el scroll y enciende cada fase. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v) { return Math.max(0, Math.min(1, v)); };
  var jobs = [];

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
