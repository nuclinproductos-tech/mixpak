/*
 * Envía cada solicitud del formulario de contacto (#cform) también al CRM de HubSpot.
 * Se engancha a la llamada a Web3Forms que ya hace cada página, así que solo actúa
 * después de que la validación del formulario haya pasado, y el email de Web3Forms
 * se sigue enviando igual. Si HubSpot falla, el usuario no lo nota.
 */
(function () {
  var HS_URL = 'https://api-eu1.hsforms.com/submissions/v3/integration/submit/' +
    '149661832/f47d14e7-2f8b-4a49-85dd-4a87fc7ef703';
  var origFetch = window.fetch;
  if (!origFetch) return;

  // Los <option value> cambian según idioma y página; se traducen a los valores
  // de las propiedades mp_sector / mp_servicio de HubSpot. Un valor desconocido
  // no se envía (HubSpot rechazaría todo el envío), pero sigue apareciendo en el mensaje.
  var SECTOR = {
    'nutricion-deportiva': 'nutricion_deportiva',
    'complementos-alimenticios': 'complementos_alimenticios',
    'supplements-alimenticios': 'complementos_alimenticios',
    'cosmetica': 'cosmetica',
    'alimentacion': 'alimentacion',
    'nutricion-clinica': 'nutricion_clinica',
    'higiene': 'higiene',
    'hygiene': 'higiene',
    'pet-care': 'cuidado_animal',
    'veterinaria': 'cuidado_animal',
    'otro': 'otro'
  };
  var SERVICIO = {
    'desarrollo': 'formulacion_desarrollo',
    'formulacion-desarrollo': 'formulacion_desarrollo',
    'formulacion-development': 'formulacion_desarrollo',
    'fabricacion': 'fabricacion',
    'copacking': 'copacking',
    'copacking-envasado': 'copacking',
    'copacking-packing': 'copacking',
    'integral': 'integral'
  };
  var IDIOMAS = { es: 'es', en: 'en', pt: 'pt' };

  function val(form, id) {
    var el = form.querySelector('#' + id);
    return el ? (el.value || '').trim() : '';
  }

  function optionText(form, id) {
    var el = form.querySelector('#' + id);
    var opt = el && el.options && el.options[el.selectedIndex];
    return opt && opt.value ? opt.text.trim() : '';
  }

  function sendToHubSpot(form) {
    var sector = optionText(form, 'fsec');
    var servicio = optionText(form, 'fserv');
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
      mp_sector: SECTOR[val(form, 'fsec')],
      mp_servicio: SERVICIO[val(form, 'fserv')],
      message: message,
      mp_idioma: IDIOMAS[(document.documentElement.lang || 'es').slice(0, 2).toLowerCase()],
      mp_origen: 'web',
      hs_lead_status: 'NEW'
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
