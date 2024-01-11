import os

os.system('git init')
os.system('git clone https://github.com/abishekvp/django.git')
os.chdir(os.path.expanduser('django'))
os.system('pip install -r requirements.txt')
os.system('python -m manage runserver')
