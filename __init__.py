from flask import Flask
# rag_system.py 最顶部添加
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'



app = Flask('rag_system')

app.config.from_pyfile('settings.py')

from rag_system import views