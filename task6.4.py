import re
content = input()
def corrector(text):
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    return text
print(corrector(content))