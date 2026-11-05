/* Sectores · interacciones (sin dependencias)
   1. Productos: filtro por formato y foco dorado que sigue al cursor.
   2. Formatos: estantería solo con CSS (sin JS).
   3. Pista de proceso: el corredor avanza con el scroll y enciende cada fase. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v) { return Math.max(0, Math.min(1, v)); };
  var jobs = [];

  /* ---------- 1. Productos: filtro por formato y foco ---------- */
  var cardsBox = document.querySelector('.sx-cards');
  if (cardsBox) {
    var lang = (document.documentElement.lang || 'es').slice(0, 2);
    var L = {
      es: { by: 'Filtrar por formato', all: 'Todos' },
      en: { by: 'Filter by format', all: 'All' },
      pt: { by: 'Filtrar por formato', all: 'Todos' }
    }[lang] || { by: 'Filtrar por formato', all: 'Todos' };
    var grid = cardsBox.querySelector('.sx-cards-grid');
    var cardsP = cardsBox.querySelectorAll('.sx-panel');
    var tally = {}, order = [];
    for (var a = 0; a < cardsP.length; a++) {
      var fl = cardsP[a].querySelectorAll('.sx-formats li');
      for (var b = 0; b < fl.length; b++) {
        var name = fl[b].textContent.trim();
        if (!tally[name]) { tally[name] = 0; order.push(name); }
        tally[name]++;
      }
    }
    /* Solo los formatos que comparten dos o más familias: el filtro cruza, no repite */
    var shared = order.filter(function (k) { return tally[k] > 1; });
    if (shared.length > 1) {
      var bar = document.createElement('div');
      bar.className = 'sx-filter';
      bar.setAttribute('role', 'group');
      bar.setAttribute('aria-label', L.by);
      var html = '<span class="sx-filter-l" aria-hidden="true">' + L.by + '</span>' +
        '<button type="button" class="sx-chip" data-f="" aria-pressed="true">' + L.all + '</button>';
      shared.forEach(function (k) {
        html += '<button type="button" class="sx-chip" data-f="' + k.replace(/"/g, '&quot;') + '" aria-pressed="false">' + k + '<i>' + tally[k] + '</i></button>';
      });
      bar.innerHTML = html;
      grid.parentNode.insertBefore(bar, grid);
      var chips = bar.querySelectorAll('.sx-chip');
      bar.addEventListener('click', function (e) {
        var btn = e.target.closest('.sx-chip');
        if (!btn) return;
        var f = btn.getAttribute('data-f');
        for (var c = 0; c < chips.length; c++) chips[c].setAttribute('aria-pressed', chips[c] === btn ? 'true' : 'false');
        cardsBox.classList.toggle('is-filtered', !!f);
        for (var d = 0; d < cardsP.length; d++) {
          var hit = false, li = cardsP[d].querySelectorAll('.sx-formats li');
          for (var e2 = 0; e2 < li.length; e2++) {
            var on = !!f && li[e2].textContent.trim() === f;
            li[e2].classList.toggle('is-hit', on);
            if (on) hit = true;
          }
          cardsP[d].classList.toggle('is-match', hit);
        }
      });
    }
    if (window.matchMedia && window.matchMedia('(hover: hover)').matches) {
      grid.addEventListener('pointermove', function (e) {
        var card = e.target.closest('.sx-panel');
        if (!card) return;
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    }
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
