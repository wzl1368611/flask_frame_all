"""
1. 请求刚刚达到
    ctx = RequestContext(...)
          - request
          - session=None
    ctx.push()
        ctx.session = SecureCookieSessionInterface.open_session

2. 视图函数

3. 请求结束
    SecureCookieSessionInterface.save_session()
"""
from flask import Flask,session
app = Flask(__name__)
app.secret_key = 'sadfasdfasdf'

@app.route('/x1')
def index():
    # 去ctx中获取session
    session['k1'] = 123
    session['k2'] = 123
    del session['k2']
    return "Index"


@app.route('/x2')
def order():
    print(session['k1'])
    return "Order"

if __name__ == '__main__':
    app.run()

    # 1. 请求一旦到来显
    app.__call__
    app.wsgi_app
    app.open_session
