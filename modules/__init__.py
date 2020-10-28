from flask import Flask
import pymongo
from modules.db import Database

app = Flask(__name__)

from modules.user.routes import module
from modules.org.routes import module

app.register_blueprint(user.routes.module, url_prefix = '/user')
app.register_blueprint(org.routes.module, url_prefix = '/org')
