from flask import Flask
from .views import account
from .views import admin
from .views import user


app = Flask(__name__)


app.register_blueprint(account.ac)
app.register_blueprint(admin.ad)
app.register_blueprint(user.us)