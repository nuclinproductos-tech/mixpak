/*
 * Envía cada solicitud del formulario de contacto (#cform) también al CRM de HubSpot.
 * Se engancha a la llamada a Web3Forms que ya hace cada página, así que solo actúa
 * después de que la validación del formulario haya pasado, y el email de Web3Forms
 * se sigue enviando igual. Si HubSpot falla, el usuario no lo nota.
 */
(function () {
  var HS_URL = 'https://api-eu1.hsforms.com/submissions/v3/integration/submit/' +
    '149661832/9a93b00a-f697-4185-a597-c45a15234734';
  var origFetch = window.fetch;
  if (!origFetch) return;

  function val(form, id) {
    var el = form.querySelector('#' + id);
    if (!el) return '';
    if (el.tagName === 'SELECT') {
      var opt = el.options[el.selectedIndex];
      return opt && opt.value ? opt.text.trim() : '';
    }
    return (el.value || '').trim();
  }

  function sendToHubSpot(form) {
    var sector = val(form, 'fsec');
    var servicio = val(form, 'fserv');
    var mensaje = val(form, 'fmsg');
    var message = [
      sector && 'Sector: ' + sector,
      servicio && 'Servicio: ' + servicio,
      mensaje && '\n' + mensaje
    ].filter(Boolean).join('\n');

    var map = {
      firstname: val(form, 'fn'),
      lastname: val(form, 'fa'),
      company: val(form, 'fe'),
      jobtitle: val(form, 'fc'),
      email: val(form, 'fem'),
      phone: val(form, 'ft'),
      message: message
    };
    var fields = [];
    for (var k in map) if (map[k]) fields.push({ name: k, value: map[k] });

    var privacy = form.querySelector('#fpriv');
    var label = privacy && form.querySelector('label[for="fpriv"]');
    var body = {
      fields: fields,
      context: { pageUri: location.href, pageName: document.title }
    };
    if (privacy && privacy.checked) {
      body.legalConsentOptions = { consent: {
        consentToProcess: true,
        text: label ? label.textContent.replace(/\s+/g, ' ').trim() : 'Acepto la política de privacidad'
      } };
    }

    origFetch.call(window, HS_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      keepalive: true
    }).catch(function () {});
  }

  window.fetch = function (url, opts) {
    try {
      var form = document.getElementById('cform');
      if (form && typeof url === 'string' && url.indexOf('api.web3forms.com/submit') !== -1 &&
          !(form.querySelector('[name="botcheck"]') || {}).value) {
        sendToHubSpot(form);
      }
    } catch (e) {}
    return origFetch.apply(window, arguments);
  };
})();
