# -*- coding: utf-8 -*-

import os
import sys
import platform

# путь в проекте к модулю manage.py
sys.path.insert(0, '/home/c/cc52289/newsite_sql/public_html/WebBooks')
# путь в проекте к модулю settings.py
sys.path.insert(0, '/home/c/cc52289/newsite_sql/public_html/WebBooks/WebBooks')
# путь к виртуальному окружению
sys.path.insert(0, '/home/c/cc52289/newsite_sql/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "WebBooks.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
