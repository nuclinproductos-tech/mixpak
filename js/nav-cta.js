/* =====================================================================
   NAV + CTA · mejora progresiva (ver css/nav-cta.css)
   - Página actual detectada por URL (funciona en ES / EN / PT y con
     o sin ".html"), marcada con aria-current.
   - Marco de registro que se desliza entre items del menú.
   - Teclado en desplegables: ↓/↑ recorren, Esc devuelve el foco.
   - Drawer móvil: foco atrapado y devuelto, submenús con altura animada.
   - CTAs: flecha unificada (SVG) y magnetismo moderado en primarios.
   Sin dependencias. Todo opcional: sin JS la web funciona igual.
   ===================================================================== */
(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');

  root.classList.add('ux-nav');

  /* ── Utilidades ─────────────────────────────────────────────── */
  function normPath(p) {
    p = (p || '/').replace(/\/+$/, '');
    p = p.replace(/\/index(\.html)?$/, '');
    p = p.replace(/\.html$/, '');
    return p || '/';
  }

  function samePage(href) {
    if (!href) return false;
    try {
      var u = new URL(href, window.location.href);
      if (u.origin !== window.location.origin) return false;
      if (u.hash && normPath(u.pathname) === normPath(window.location.pathname) && u.hash !== '') {
        /* "index.html#contacto" no es "Inicio" */
        return false;
      }
      return normPath(u.pathname) === normPath(window.location.pathname);
    } catch (e) {
      return false;
    }
  }

  var ARROW_SVG =
    '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false" class="ux-arrow">' +
    '<path d="M4 10h11M11 5.5 15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.9" ' +
    'stroke-linecap="round" stroke-linejoin="round"/></svg>';

  /* ── 1. Página actual ───────────────────────────────────────── */
  var nav = doc.querySelector('.header-nav');
  var currentItem = null;

  if (nav) {
    Array.prototype.forEach.call(nav.children, function (li) {
      var link = li.querySelector(':scope > a');
      var trigger = li.querySelector(':scope > .nav-trigger');
      if (link && samePage(link.getAttribute('href'))) {
        link.setAttribute('aria-current', 'page');
        currentItem = link;
      }
      if (trigger) {
        var dd = doc.getElementById(trigger.getAttribute('data-dd'));
        if (!dd) return;
        dd.querySelectorAll('a').forEach(function (a) {
          if (samePage(a.getAttribute('href'))) {
            a.setAttribute('aria-current', 'page');
            trigger.setAttribute('data-current', 'true');
            currentItem = trigger;
          }
        });
      }
    });
  }

  /* Drawer: mismo criterio */
  doc.querySelectorAll('.mobile-nav > li').forEach(function (li) {
    var link = li.querySelector(':scope > a');
    if (link && samePage(link.getAttribute('href'))) {
      link.setAttribute('aria-current', 'page');
      li.classList.add('is-current');
    }
    li.querySelectorAll('.mob-submenu a').forEach(function (a) {
      if (samePage(a.getAttribute('href'))) {
        a.setAttribute('aria-current', 'page');
        li.classList.add('is-current');
      }
    });
  });

  /* ── 2. Marco de registro deslizante ────────────────────────── */
  if (nav) {
    var reg = doc.createElement('li');
    reg.className = 'nav-reg';
    reg.setAttribute('aria-hidden', 'true');
    reg.setAttribute('role', 'presentation');
    nav.appendChild(reg);

    var target = null;

    function itemOf(el) {
      return el && el.closest ? el.closest('.header-nav > li:not(.nav-reg)') : null;
    }

    function place(el, visible) {
      if (!el) {
        reg.style.setProperty('--o', '0');
        return;
      }
      var li = itemOf(el);
      var hit = li ? li.querySelector(':scope > a, :scope > .nav-trigger') : el;
      if (!hit) return;
      reg.style.setProperty('--x', (li ? li.offsetLeft : 0) + hit.offsetLeft + 'px');
      reg.style.setProperty('--w', hit.offsetWidth + 'px');
      reg.style.setProperty('--o', visible ? '1' : '0');
      reg.classList.toggle('is-away', !!currentItem && hit !== currentItem);
      target = hit;
    }

    function rest() {
      var open = nav.querySelector('.nav-trigger[aria-expanded="true"]');
      if (open) return place(open, true);
      if (currentItem) return place(currentItem, true);
      /* Sin página actual: el marco se desvanece donde está */
      reg.style.setProperty('--o', '0');
      reg.classList.remove('is-away');
    }

    nav.addEventListener('pointerover', function (e) {
      if (e.pointerType === 'touch') return;
      var li = itemOf(e.target);
      if (!li) return;
      var hit = li.querySelector(':scope > a, :scope > .nav-trigger');
      /* Primer hover sin página actual: aparece in situ, sin deslizar desde 0 */
      if (reg.style.getPropertyValue('--o') !== '1') {
        reg.classList.remove('is-ready');
        place(hit, false);
        void reg.offsetWidth;
        reg.classList.add('is-ready');
      }
      place(hit, true);
    });

    nav.addEventListener('pointerleave', function () {
      window.setTimeout(rest, 160);
    });

    nav.addEventListener('focusin', function (e) {
      if (e.target.closest('.nav-dropdown')) return;
      place(e.target, true);
    });

    nav.addEventListener('focusout', function (e) {
      if (!nav.contains(e.relatedTarget)) window.setTimeout(rest, 0);
    });

    /* Al cerrar un desplegable (atributo cambia en JS de la página) */
    nav.querySelectorAll('.nav-trigger').forEach(function (t) {
      new MutationObserver(function () {
        if (!nav.matches(':hover')) rest();
      }).observe(t, { attributes: true, attributeFilter: ['aria-expanded'] });
    });

    function init() {
      reg.classList.remove('is-ready');
      rest();
      void reg.offsetWidth;
      window.requestAnimationFrame(function () { reg.classList.add('is-ready'); });
    }

    init();
    if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(init);
    if ('ResizeObserver' in window) {
      var ro = new ResizeObserver(function () {
        reg.classList.remove('is-ready');
        if (target) place(target, reg.style.getPropertyValue('--o') === '1');
        window.requestAnimationFrame(function () { reg.classList.add('is-ready'); });
      });
      ro.observe(nav);
    }
  }

  /* ── 3. Teclado en desplegables ─────────────────────────────── */
  doc.querySelectorAll('.nav-trigger[data-dd]').forEach(function (trigger) {
    var dd = doc.getElementById(trigger.getAttribute('data-dd'));
    if (!dd) return;
    var links = function () { return Array.prototype.slice.call(dd.querySelectorAll('a')); };

    function open() {
      if (trigger.getAttribute('aria-expanded') !== 'true') trigger.click();
    }

    trigger.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        open();
        var l = links();
        if (l[0]) window.setTimeout(function () { l[0].focus(); }, 30);
      }
    });

    dd.addEventListener('keydown', function (e) {
      var l = links();
      var i = l.indexOf(doc.activeElement);
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        e.preventDefault();
        l[(i + 1) % l.length].focus();
      } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        e.preventDefault();
        if (i <= 0) trigger.focus();
        else l[i - 1].focus();
      } else if (e.key === 'Home') {
        e.preventDefault();
        l[0].focus();
      } else if (e.key === 'End') {
        e.preventDefault();
        l[l.length - 1].focus();
      } else if (e.key === 'Escape') {
        trigger.focus();
      }
    });

    /* Salir con Tab cierra el panel */
    trigger.parentElement.addEventListener('focusout', function (e) {
      if (trigger.parentElement.contains(e.relatedTarget)) return;
      if (trigger.getAttribute('aria-expanded') === 'true' && !trigger.parentElement.matches(':hover')) {
        trigger.setAttribute('aria-expanded', 'false');
        trigger.classList.remove('nav-active');
        dd.classList.remove('open');
      }
    });
  });

  /* ── 4. Drawer móvil ────────────────────────────────────────── */
  var drawer = doc.getElementById('mobile-drawer');
  var burger = doc.getElementById('hamburger');

  if (drawer) {
    var lastFocus = null;

    function focusables() {
      return Array.prototype.filter.call(
        drawer.querySelectorAll('a[href], button:not([disabled])'),
        function (el) { return el.offsetParent !== null || el === doc.activeElement; }
      );
    }

    new MutationObserver(function () {
      var isOpen = drawer.classList.contains('open');
      if (isOpen) {
        lastFocus = doc.activeElement;
        window.setTimeout(function () {
          var close = doc.getElementById('mobile-close');
          if (close) close.focus({ preventScroll: true });
        }, 60);
      } else if (drawer.contains(doc.activeElement) || doc.activeElement === doc.body) {
        var back = burger || lastFocus;
        if (back && back.offsetParent !== null) back.focus({ preventScroll: true });
      }
    }).observe(drawer, { attributes: true, attributeFilter: ['class'] });

    drawer.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !drawer.classList.contains('open')) return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0];
      var last = f[f.length - 1];
      if (e.shiftKey && doc.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && doc.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });

    /* Submenús: altura real medida (corre después del handler de la página) */
    function syncSubmenus() {
      drawer.querySelectorAll('.mob-submenu').forEach(function (s) {
        s.style.maxHeight = s.classList.contains('open') ? s.scrollHeight + 32 + 'px' : '0px';
      });
    }
    drawer.querySelectorAll('.mob-trigger').forEach(function (b) {
      b.addEventListener('click', function () { window.requestAnimationFrame(syncSubmenus); });
    });
    syncSubmenus();
  }

  /* ── 5. CTAs: flecha unificada ──────────────────────────────── */
  var PRIMARY = [
    '.header-cta', '.mob-cta', '.btn.btn--gold', '.fab-btn-primary', '.btn-page-cta',
    '.hero-cta-btn--quote', '.le-cta', '.des-what-cta', '.cp-custom-cta', '.env3-dual-cta',
    '.f-submit', '.btn.btn-primary:not([onclick])'
  ].join(',');
  var SECONDARY = '.btn.btn--white, .fab-btn-ghost, .hero-cta-btn--meet, .btn.btn-ghost';
  var TERTIARY = '.intro-link, .le-all, .des-scale-cta, .sector-footer-cta';

  function stripArrowText(el) {
    /* Quita "→" final de los nodos de texto; devuelve true si lo había */
    var found = false;
    for (var n = el.lastChild; n; n = n.previousSibling) {
      if (n.nodeType === 3) {
        if (/→\s*$/.test(n.nodeValue)) {
          n.nodeValue = n.nodeValue.replace(/\s*→\s*$/, '');
          found = true;
        }
        if (n.nodeValue.trim()) break;
      } else if (n.nodeType === 1) {
        break;
      }
    }
    return found;
  }

  function enhanceButton(el, withArrow) {
    var had = stripArrowText(el);
    var hasIcon = !!el.querySelector(':scope > svg:last-child');
    if ((had || withArrow) && !hasIcon) el.insertAdjacentHTML('beforeend', ARROW_SVG);
  }

  doc.querySelectorAll(PRIMARY).forEach(function (el) {
    if (el.closest('#cookie-bar, .cookie-btns')) return;
    enhanceButton(el, true);
    /* El formulario reescribe el texto del botón: se vuelve a normalizar */
    if (el.matches('.f-submit')) {
      new MutationObserver(function () {
        if (/→\s*$/.test(el.textContent)) enhanceButton(el, true);
      }).observe(el, { childList: true });
    }
  });

  doc.querySelectorAll(SECONDARY).forEach(function (el) { enhanceButton(el, false); });

  doc.querySelectorAll(TERTIARY).forEach(function (el) {
    if (stripArrowText(el) && !el.querySelector('.ux-arr')) {
      var s = doc.createElement('span');
      s.className = 'ux-arr';
      s.setAttribute('aria-hidden', 'true');
      s.textContent = '→';
      el.appendChild(s);
    }
  });

  /* ── 6. Magnetismo moderado (solo puntero fino, sin reduced-motion) ── */
  var MAGNETIC = '.header-cta, .hero-cta-btn--quote, .btn.btn--gold, .fab-btn-primary, .btn-page-cta';

  doc.querySelectorAll(MAGNETIC).forEach(function (el) {
    var raf = 0;
    el.addEventListener('pointermove', function (e) {
      if (!finePointer.matches || reduceMotion.matches) return;
      var r = el.getBoundingClientRect();
      var dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
      var dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(function () {
        el.style.setProperty('--mx', (dx * 4).toFixed(2) + 'px');
        el.style.setProperty('--my', (dy * 3).toFixed(2) + 'px');
      });
    });
    el.addEventListener('pointerleave', function () {
      cancelAnimationFrame(raf);
      el.style.removeProperty('--mx');
      el.style.removeProperty('--my');
    });
  });

  /* ── 7. Vídeos de fondo: solo pantallas ≥768px ──────────────────
     Los <video> llevan data-src y preload="none": en móvil, con
     movimiento reducido o con ahorro de datos se queda el póster
     (mismo encuadre) y no se descargan 4–7 MB. En escritorio se
     cargan al acercarse al viewport, conservando la velocidad de
     reproducción que fije cada página. */
  var wideMQ = window.matchMedia('(min-width: 768px)');
  var saveData = !!(navigator.connection && navigator.connection.saveData);

  function loadVideo(v) {
    if (v.dataset.uxLoaded) return;
    v.dataset.uxLoaded = '1';
    var rate = v.playbackRate || 1;
    v.querySelectorAll('source[data-src]').forEach(function (s) {
      s.src = s.getAttribute('data-src');
      s.removeAttribute('data-src');
    });
    if (v.hasAttribute('data-src')) {
      v.src = v.getAttribute('data-src');
      v.removeAttribute('data-src');
    }
    v.muted = true;
    v.load();
    v.addEventListener('loadeddata', function () {
      v.playbackRate = rate;
      var p = v.play();
      if (p && p.catch) p.catch(function () {});
    }, { once: true });
  }

  function setupVideos() {
    if (!wideMQ.matches || reduceMotion.matches || saveData) return;
    var vids = Array.prototype.filter.call(
      doc.querySelectorAll('video'),
      function (v) { return v.hasAttribute('data-src') || v.querySelector('source[data-src]'); }
    );
    if (!vids.length) return;
    if (!('IntersectionObserver' in window)) { vids.forEach(loadVideo); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { loadVideo(en.target); io.unobserve(en.target); }
      });
    }, { rootMargin: '300px 0px' });
    var vh = window.innerHeight || doc.documentElement.clientHeight;
    vids.forEach(function (v) {
      var r = v.getBoundingClientRect();
      /* El vídeo del hero ya está a la vista: carga directa, sin esperar al observer */
      if (r.top < vh + 300 && r.bottom > -300) loadVideo(v);
      else io.observe(v);
    });
  }

  setupVideos();
  if (wideMQ.addEventListener) wideMQ.addEventListener('change', setupVideos);
})();
