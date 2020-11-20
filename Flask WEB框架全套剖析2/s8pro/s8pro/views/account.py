from flask import Blueprint,render_template
import redis

ac = Blueprint('ac',__name__)

@ac.route('/login')
def login():
    conn = redis.Redis()
    return render_template('login.html')


@ac.route('/logout')
def logout():
    return '大人'
