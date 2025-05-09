from flask import Flask

app = Flask('rag_system')

app.config.from_pyfile('settings.py')

from rag_system import views