# -*- coding: utf-8 -*-
import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/c/cc36217/newsite/public_html/avtoterminal_server')
#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/c/cc36217/newsite/public_html/avtoterminal_server/avtoterminal_server')
#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/c/cc36217/newsite/venv/lib/python3.10/site-packages'.format(platform.python_version()[0:3]))
#sys.path.insert(0, '/home/c/cx53558/newsite/myenv/lib/python3.6/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "avtoterminal_server.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
