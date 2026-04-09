import re
import glob

html_files = [
    'index.html',
    'desarrollo-producto.html',
    'envasado-avanzado.html',
    'diseno-packaging.html',
    'fabricacion-propia.html',
    'calidad-regulatorio.html',
    'idi-continuo.html'
]

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reemplazar height: 64px; en CSS
        old_str = "height: 64px; /* Mucho mayor */"
        new_str = "height: 192px;\n  max-width: 100%;\n  object-fit: contain;"
        
        # In case the exact comment is slightly different
        content = re.sub(r'height:\s*64px;\s*/\* Mucho mayor \*/', new_str, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Updated logo size in {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

