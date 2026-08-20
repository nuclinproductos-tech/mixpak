(function () {
  var KEY = 'mps_cookie_consent';
  if (localStorage.getItem(KEY)) return;

  var STRINGS = {
    es: {
      aria: 'Aviso de cookies',
      title: 'Este sitio utiliza cookies',
      text: 'Usamos cookies propias y de terceros (Google Fonts) para el correcto funcionamiento del sitio y análisis de navegación. Puede aceptarlas o rechazar las no esenciales.',
      accept: 'Aceptar todas',
      reject: 'Solo necesarias'
    },
    en: {
      aria: 'Cookie notice',
      title: 'This site uses cookies',
      text: 'We use first-party and third-party cookies (Google Fonts) for the correct operation of the site and browsing analysis. You can accept them or reject the non-essential ones.',
      accept: 'Accept all',
      reject: 'Necessary only'
    },
    pt: {
      aria: 'Aviso de cookies',
      title: 'Este sítio utiliza cookies',
      text: 'Utilizamos cookies próprias e de terceiros (Google Fonts) para o correto funcionamento do sítio e análise de navegação. Pode aceitá-las ou rejeitar as não essenciais.',
      accept: 'Aceitar todas',
      reject: 'Apenas necessárias'
    }
  };
  var lang = (document.documentElement.lang || 'es').slice(0, 2).toLowerCase();
  var t = STRINGS[lang] || STRINGS.es;

  var banner = document.createElement('div');
  banner.id = 'cookie-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-modal', 'false');
  banner.setAttribute('aria-label', t.aria);
  banner.innerHTML = [
    '<div class="cb-inner">',
    '  <div class="cb-text">',
    '    <strong>' + t.title + '</strong>',
    '    <p>' + t.text + '</p>',
    '  </div>',
    '  <div class="cb-actions">',
    '    <button class="cb-btn cb-accept" id="cb-accept">' + t.accept + '</button>',
    '    <button class="cb-btn cb-reject" id="cb-reject">' + t.reject + '</button>',
    '  </div>',
    '</div>'
  ].join('');

  var style = document.createElement('style');
  style.textContent = [
    '#cookie-banner{',
      'position:fixed;bottom:0;left:0;right:0;z-index:9999;',
      'background:#fff;border-top:2px solid #C8A84B;',
      'box-shadow:0 -4px 24px rgba(0,0,0,.12);',
      'padding:16px 24px;',
      'animation:cbSlideUp .35s ease both;',
    '}',
    '@keyframes cbSlideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}',
    '.cb-inner{',
      'max-width:1200px;margin:0 auto;',
      'display:flex;align-items:center;justify-content:space-between;',
      'gap:24px;flex-wrap:wrap;',
    '}',
    '.cb-text{flex:1;min-width:260px;}',
    '.cb-text strong{',
      'display:block;font-family:\'Nunito Sans\',sans-serif;',
      'font-size:1rem;color:#000066;margin-bottom:4px;',
    '}',
    '.cb-text p{',
      'font-size:.82rem;color:#6B7280;line-height:1.5;margin:0;',
    '}',
    '.cb-actions{display:flex;gap:10px;flex-shrink:0;flex-wrap:wrap;}',
    '.cb-btn{',
      'font-family:\'Inter\',sans-serif;font-size:.85rem;font-weight:700;',
      'padding:10px 22px;border-radius:999px;cursor:pointer;',
      'transition:all .2s ease;border:2px solid transparent;white-space:nowrap;',
    '}',
    '.cb-accept{background:#C8A84B;color:#000066;border-color:#C8A84B;}',
    '.cb-accept:hover{background:#A8893A;border-color:#A8893A;}',
    '.cb-reject{background:transparent;color:#000066;border-color:#000066;}',
    '.cb-reject:hover{background:#000066;color:#fff;}',
    '@media(max-width:640px){',
      '.cb-inner{flex-direction:column;align-items:flex-start;}',
      '.cb-actions{width:100%;}',
      '.cb-btn{flex:1;text-align:center;}',
    '}'
  ].join('');

  document.head.appendChild(style);
  document.body.appendChild(banner);

  function dismiss(value) {
    localStorage.setItem(KEY, value);
    banner.style.animation = 'cbSlideUp .3s ease reverse both';
    setTimeout(function () { banner.remove(); }, 320);
  }

  document.getElementById('cb-accept').addEventListener('click', function () { dismiss('accepted'); });
  document.getElementById('cb-reject').addEventListener('click', function () { dismiss('rejected'); });
})();
