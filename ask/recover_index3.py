import re

log_path = '/Users/anabelen/.gemini/antigravity/brain/18ce29e5-52bb-480d-bf32-c659fc8762f5/.system_generated/logs/overview.txt'
with open(log_path, 'r') as f:
    text = f.read()

with open('index.html', 'r') as f:
    html = f.read()

def unescape_custom(s):
    # remove the bounding quotes
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    # replace literal \n with actual newlines? No, if the log contains ACTUAL newlines inside quotes, s already has actual newlines!
    # Wait, if s has escaped \" we should replace them with "
    s = s.replace('\\"', '"')
    # and \\n with \n
    s = s.replace('\\n', '\n')
    return s

def extract_replacements():
    # regex to find replace_file_content calls
    # but the regex needs to handle unescaped newlines!
    # "TargetContent":"...", "ReplacementContent":"..."
    matches = re.finditer(r'"TargetContent":\s*"(.*?)(?<!\\)",\s*"ReplacementContent":\s*"(.*?)(?<!\\)"', text, re.DOTALL)
    return matches

for i, m in enumerate(extract_replacements()):
    target = unescape_custom(m.group(1))
    replacement = unescape_custom(m.group(2))
    if target in html:
        html = html.replace(target, replacement)
        print(f"Applied replacement {i}")
    else:
        print(f"Warning: replacement {i} target not found!")

with open('index_recovered3.html', 'w') as f:
    f.write(html)
print("Recovery completed.")
