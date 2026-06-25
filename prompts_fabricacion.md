# Imágenes Sección "Qué Fabricamos" — Mix Pak System
## Archivo de referencia y prompts para regeneración

---

## Estado actual (v2 — junio 2025)

Las imágenes han sido actualizadas con fotografías reales del inventario del sitio,
eliminando las anteriores con branding ficticio (marcas inventadas como "Aurelia", "NutriVita", "Aurora Wellness").

### Asignación de imágenes

| Categoría | Archivo actual | Razón del cambio |
|---|---|---|
| Polvos y mezclas | `envases/productos/prod_polvos_1775736308903.png` | Doypack negro + bote con polvo funcional, fondo gris neutro, sin branding |
| Líquidos y soluciones | `envases/productos/prod_shots_1775736380453.png` | Viales de vidrio ámbar con tapa aluminio, fondo cemento neutro, aspecto farmacéutico |
| Geles, cremas y semisólidos | `IMG/sectores/sector_cosmetica.png` | Gama de envases cosméticos (tubos, tarros, dispensadores), fondo blanco limpio |
| Cápsulas y comprimidos | `envases/productos/prod_capsulas_1775736322273.png` | Bote ámbar + cápsulas y comprimidos de distintos colores, fondo blanco |
| Snacks y sólidos | `envases/productos/prod_barritas_1775736366649.png` | Barrita de cereales real en flow pack blanco neutro abierto, fondo gris |
| Monodosis y especiales | `envases/all_stickpacks.png` | Variedad de stickpacks y sachets en blanco, fondo blanco, todos los formatos |

---

## Criterio de estilo para nuevas imágenes

El estilo visual de la web de Mix Pak System sigue estas pautas:

- **Fondo**: Neutro (gris claro, blanco, cemento grisáceo). Sin fondos de color vivo.
- **Iluminación**: Natural, suave, de estudio. Sin sombras duras.
- **Composición**: Limpia, centrada, con espacio suficiente alrededor del producto.
- **Branding**: Sin logos ni marcas ficticias visibles. Envases "your brand" o en blanco son aceptables.
- **Estilo**: Industrial realista. No aspiracional cosmético ni editorial de revista de moda.
- **Materiales**: Fotografía de producto — no renders 3D evidentes, no mockups vacíos.

---

## Prompts para regeneración (cuota disponible a partir de ~29/06/2025)

### 1. Polvos y mezclas
```
Product photography: a matte black doypack pouch and a black cylindrical canister 
with a measuring scoop filled with white protein powder, spilling slightly. 
Light grey concrete background. Studio lighting, soft shadows. 
No text, no brand logos. Clean, premium supplement brand aesthetic. 
Square format 1:1. Sharp focus on the powder texture.
```

### 2. Líquidos y soluciones
```
Product photography: six amber glass vials with aluminum screw caps arranged 
in a triangular formation. Clear golden liquid inside each vial. 
Light warm grey concrete surface. Soft natural studio lighting from above-left. 
No labels, no text, no branding. Pharmaceutical aesthetic. 
Square format 1:1. Sharp focus, slight depth of field.
```

### 3. Geles, cremas y semisólidos
```
Product photography: three unlabeled white cosmetic tubes and one clear glass jar 
with a white cream texture visible inside, arranged on a light marble surface. 
White background. Minimalist composition. Soft shadows from side lighting. 
No text, no brand logos. Clean industrial-cosmetic aesthetic. 
Square format 1:1.
```

### 4. Cápsulas y comprimidos
```
Product photography: a clear amber glass supplement bottle without cap, lying on 
its side with various capsules (white, blue, yellow) and round white tablets 
spilling out onto a clean white surface. Light beige-grey background. 
No labels or text. Natural studio lighting. Pharmaceutical product photography. 
Square format 1:1.
```

### 5. Snacks y sólidos
```
Product photography: a granola and chocolate chip energy bar, partially unwrapped 
from a plain white flow-pack wrapper, resting on a light grey concrete slab. 
Scattered oats and seeds around it. Warm natural light from above. 
No text, no brand logos. Clean food photography aesthetic. 
Square format 1:1. Close-up, textured.
```

### 6. Monodosis y especiales
```
Product photography: a flat lay of 8 different single-dose packaging formats 
on a clean white surface: 2 sachets, 2 stick packs, 2 single-dose pouches, 
1 small ampoule, 1 blister strip. All packaging in white or transparent. 
Top-down view. Studio lighting. No text, no branding. 
Landscape format 4:3.
```

---

## Notas técnicas

- Tamaño recomendado: 800×800px mínimo, idealmente 1200×1200px
- Formato: WebP (convertir con `cwebp -q 85 input.png -o output.webp`)
- Ubicación: `envases/productos/` para imágenes de producto
- Guardar el original en alta resolución antes de exportar a WebP
- El panel visual usa `aspect-ratio: 4/3` y `object-fit: cover`
- El panel de Monodosis tiene clase adicional `.visual--contain` para mostrar la imagen completa

---

*Última actualización: 25/06/2025 — Mix Pak System*
