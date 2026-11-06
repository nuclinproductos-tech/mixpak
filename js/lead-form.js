/* =====================================================================
   Formulario de contacto (#cform) · mejoras compartidas
   - La descripción del proyecto adapta su ayuda al estado elegido, para
     pedir justo la información que permite valorar ese tipo de proyecto.
   No toca validación, envío, HubSpot ni analítica (viven en cada página
   y en hubspot-crm.js).
   ===================================================================== */
(function () {
  'use strict';

  var form = document.getElementById('cform');
  if (!form) return;

  var lang = (document.documentElement.lang || 'es').slice(0, 2).toLowerCase();

  var HINTS = {
    es: {
      'en-produccion': 'Producto actual, volumen anual aproximado y qué quieres mejorar: coste, capacidad, calidad o plazos.',
      'ampliacion-gama': 'Gama actual, nuevas referencias previstas y volumen estimado por referencia.',
      'nuevo-lanzamiento': 'Tipo de producto, formato deseado, mercado de venta y fecha objetivo de lanzamiento.',
      'exploratoria': 'Cuéntanos la idea y en qué punto estás. Te orientamos sobre fórmula, formato y viabilidad.'
    },
    en: {
      'en-produccion': 'Current product, approximate annual volume and what you want to improve: cost, capacity, quality or lead times.',
      'ampliacion-gama': 'Current range, planned new SKUs and estimated volume per SKU.',
      'nuevo-lanzamiento': 'Product type, preferred format, target market and planned launch date.',
      'exploratoria': 'Tell us the idea and where you are. We will advise on formula, format and feasibility.'
    },
    pt: {
      'en-produccion': 'Produto atual, volume anual aproximado e o que pretende melhorar: custo, capacidade, qualidade ou prazos.',
      'ampliacion-gama': 'Gama atual, novas referências previstas e volume estimado por referência.',
      'nuevo-lanzamiento': 'Tipo de produto, formato pretendido, mercado e data prevista de lançamento.',
      'exploratoria': 'Conte-nos a ideia e em que fase está. Orientamos sobre fórmula, formato e viabilidade.'
    }
  };

  var estado = form.querySelector('#fest');
  var msg = form.querySelector('#fmsg');
  var hints = HINTS[lang] || HINTS.es;

  if (estado && msg) {
    var basePlaceholder = msg.getAttribute('placeholder') || '';
    estado.addEventListener('change', function () {
      msg.setAttribute('placeholder', hints[estado.value] || basePlaceholder);
    });
  }

  /* Teclados móviles adecuados por campo */
  function attrs(id, map) {
    var el = form.querySelector('#' + id);
    if (!el) return;
    Object.keys(map).forEach(function (k) { if (!el.hasAttribute(k)) el.setAttribute(k, map[k]); });
  }
  attrs('fn', { autocapitalize: 'words', enterkeyhint: 'next' });
  attrs('fe', { autocapitalize: 'words', enterkeyhint: 'next' });
  attrs('fc', { autocapitalize: 'sentences', enterkeyhint: 'next' });
  attrs('fem', { autocapitalize: 'off', spellcheck: 'false', inputmode: 'email', enterkeyhint: 'next' });
  attrs('ft', { inputmode: 'tel', enterkeyhint: 'next' });

  /* Errores accesibles: cada campo apunta a su mensaje */
  form.querySelectorAll('[required]').forEach(function (f) {
    var err = form.querySelector('#err-' + f.id);
    if (err) {
      err.setAttribute('role', 'alert');
      var d = f.getAttribute('aria-describedby');
      if (!d || d.indexOf(err.id) === -1) f.setAttribute('aria-describedby', ((d || '') + ' ' + err.id).trim());
    }
  });

  /* Tras la validación de la página (que corre antes en el mismo submit):
     marca aria-invalid y lleva el foco al primer campo con error, sin
     competir con el scroll suave que ya hace la página. */
  form.addEventListener('submit', function () {
    window.setTimeout(function () {
      var first = null;
      form.querySelectorAll('[required]').forEach(function (f) {
        var err = form.querySelector('#err-' + f.id);
        var bad = (err && err.classList.contains('visible')) || /EF4444|239, 68, 68|b91c1c/i.test(f.style.borderColor || '');
        if (bad) f.setAttribute('aria-invalid', 'true'); else f.removeAttribute('aria-invalid');
        if (bad && !first) first = f;
      });
      if (first) first.focus({ preventScroll: true });
    }, 0);
  });

  form.addEventListener('input', function (e) {
    if (e.target.hasAttribute && e.target.hasAttribute('aria-invalid')) e.target.removeAttribute('aria-invalid');
  });
  form.addEventListener('change', function (e) {
    if (e.target.hasAttribute && e.target.hasAttribute('aria-invalid')) e.target.removeAttribute('aria-invalid');
  });
})();
