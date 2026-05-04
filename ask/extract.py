import re

log_path = '/Users/anabelen/.gemini/antigravity/brain/18ce29e5-52bb-480d-bf32-c659fc8762f5/.system_generated/logs/overview.txt'
with open(log_path, 'r') as f:
    text = f.read()

# find all TargetContent and ReplacementContent
matches = re.finditer(r'"TargetContent":"([^"]*?)","ReplacementContent":"([^"]*?)"', text)
for m in matches:
    print("Found pair!")
