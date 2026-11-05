# Archivos para subir a la web (FileZilla/Plesk)

Rama `form-formato-cursor`, 05-11-2026. Ruta en el servidor = misma ruta que en el repo. Comprobado con curl contra mixpaksystem.com.

## 1. Páginas y archivos modificados (sobrescribir)

- contacto.html
- copacking.html
- desarrollo.html
- empresa.html
- en/copacking.html
- en/desarrollo.html
- en/empresa.html
- en/fabricacion.html
- en/index.html
- en/sectores/alimentacion.html
- en/sectores/complementos-alimenticios.html
- en/sectores/cosmetica.html
- en/sectores/cuidado-animal.html
- en/sectores/higiene.html
- en/sectores/nutricion-deportiva.html
- fabricacion.html
- index.html
- js/formatos-tunnel.js
- js/hubspot-crm.js
- pt/copacking.html
- pt/desarrollo.html
- pt/empresa.html
- pt/fabricacion.html
- pt/index.html
- pt/sectores/alimentacion.html
- pt/sectores/complementos-alimenticios.html
- pt/sectores/cosmetica.html
- pt/sectores/cuidado-animal.html
- pt/sectores/higiene.html
- pt/sectores/nutricion-deportiva.html
- sectores/alimentacion.html
- sectores/complementos-alimenticios.html
- sectores/cosmetica.html
- sectores/cuidado-animal.html
- sectores/higiene.html
- sectores/nutricion-deportiva.html
- sitemap.xml

## 2. Archivos que FALTAN en el servidor (nuevos; sin ellos fallan el túnel de formatos, la línea del tiempo, HubSpot, las FAQs y el cursor)

- css/cursor.css
- css/cta-band.css
- css/desarrollo-pro.css
- js/desarrollo-pro.js
- css/fabricacion-pro.css
- js/fabricacion-pro.js
- css/seo-faq.css
- css/formatos-tunnel.css
- css/empresa-timeline.css
- js/formatos-tunnel.js  (ya está en la lista 1)
- js/empresa-timeline.js
- js/hubspot-crm.js  (ya está en la lista 1)
- assets/envases/web/  (carpeta completa, incluida la subcarpeta sueltos/)

## NO subir

- docs/, preview-linea-envasado/, .claude/, .git/

## Después de subir

1. Enviar una solicitud de prueba desde https://mixpaksystem.com/#contacto y comprobar que llegan el email (web3forms) y el contacto (HubSpot).
2. Search Console: volver a enviar sitemap.xml.
