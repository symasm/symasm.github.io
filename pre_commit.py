import os

os.system(r'copy ..\symasm.py .')

for root, dirs, files in os.walk(r'..\impl'):
    for name in files:
        if name.endswith('.py'):
            filestr = open(os.path.join(root, name), 'r', encoding = 'utf-8-sig').read()
            open(name if name != '__init__.py' else 'impl.py', 'w', encoding = 'utf-8', newline = "\n").write(filestr.replace('from .', 'from '))
