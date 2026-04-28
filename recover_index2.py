import json
import ast

log_path = '/Users/anabelen/.gemini/antigravity/brain/18ce29e5-52bb-480d-bf32-c659fc8762f5/.system_generated/logs/overview.txt'
with open(log_path, 'r') as f:
    lines = f.readlines()

with open('index.html', 'r') as f:
    html = f.read()

def unescape(v):
    if isinstance(v, str) and v.startswith('"') and v.endswith('"'):
        try:
            return ast.literal_eval(v)
        except Exception as e:
            return v
    return v

def apply_replacement(html, target, replacement):
    target = unescape(target)
    replacement = unescape(replacement)
    
    if target in html:
        return html.replace(target, replacement)
    else:
        print("Warning: target not found!")
        print("Target:", repr(target)[:100])
        return html

for i, line in enumerate(lines):
    if i >= 147:
        break
    if 'PLANNER_RESPONSE' in line and 'tool_calls' in line:
        try:
            # We can't use json.loads directly because of unescaped control chars in the whole line?
            # Actually, if the JSON is strictly invalid, json.loads(line) will fail.
            data = json.loads(line, strict=False)
            for tool in data.get('tool_calls', []):
                args = tool.get('args', {})
                tf = unescape(args.get('TargetFile', ''))
                if 'index.html' not in tf:
                    continue
                if tool['name'] == 'replace_file_content':
                    target = args.get('TargetContent', '')
                    replacement = args.get('ReplacementContent', '')
                    html = apply_replacement(html, target, replacement)
                elif tool['name'] == 'multi_replace_file_content':
                    chunks = args.get('ReplacementChunks', [])
                    if isinstance(chunks, str):
                        try:
                            chunks = json.loads(chunks, strict=False)
                        except:
                            pass
                    if isinstance(chunks, list):
                        for chunk in chunks:
                            target = chunk.get('TargetContent', '')
                            replacement = chunk.get('ReplacementContent', '')
                            html = apply_replacement(html, target, replacement)
        except Exception as e:
            pass

with open('index_recovered2.html', 'w') as f:
    f.write(html)
print("Recovery completed.")
