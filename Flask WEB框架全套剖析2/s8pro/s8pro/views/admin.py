from flask import Blueprint

ad = Blueprint('ad',__name__,url_prefix='/admin')

@ad.before_request
def bf():
    print('before_request')


@ad.route('/home')
def home():
    return 'home'

@ad.route('/xxxx')
def xxxx():
    return 'xxxx'
