from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 包含了SQLAlchemy相关的所有操作
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')

    from .views.account import ac
    app.register_blueprint(ac)

    db.init_app(app)
    return app