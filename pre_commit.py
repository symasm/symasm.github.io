import os

#os.system(r'copy ..\symasm.py .')
filestr = open('../symasm.py', 'r', encoding = 'utf-8-sig').read()
open('symasm.py', 'w', encoding = 'utf-8', newline = "\n").write(filestr.replace('from impl.', 'from impl_'))

for root, dirs, files in os.walk('../impl'):
    for name in files:
        if name.endswith('.py'):
            filestr = open(os.path.join(root, name), 'r', encoding = 'utf-8-sig').read()
            dest_file_name = os.path.normpath(os.path.join(root[3:], '..', name if name != '__init__.py' else os.path.basename(root) + '.py')).replace('\\', '_')
            from_prefix = dest_file_name[:-len(name)] if name != '__init__.py' else 'impl_' * (root != '../impl')
            #print(os.path.join(root, name), '->', dest_file_name, '"from ' + from_prefix + '"')
            open(dest_file_name, 'w', encoding = 'utf-8', newline = "\n").write(filestr.replace('from .', 'from ' + from_prefix))
