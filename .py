import os

os.system('git init')
os.system('git clone https://github.com/abishekvp/asmi.git')
os.chdir(os.path.expanduser('asmi'))
os.system('pip install -r req.txt')
os.chdir(os.path.expanduser('main'))
os.system('python -m manage runserver')
