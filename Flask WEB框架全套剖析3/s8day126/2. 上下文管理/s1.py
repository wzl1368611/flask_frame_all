from flask import Flask,request,session,g,current_app

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request) # LocalProxy.__str__
    request.method # LocalProxy.__getattr__(key='method') # ctx中request, 再去request中获取method
    request.args   # LocalProxy.__getattr__(key='args')   # ctx中request, 再去request中获取args


    session['k1'] = 123  # LocalProxy.__setitem__(key=k1,value=123) # ctx中session, 再去session中改k1设置值
    session['k1'] # LocalProxy.__getitem__(key='k1') # ctx中session, 再去session中获取k1对应的值

    return 'wupeiqi'

if __name__ == '__main__':
    app.__call__
    app.wsgi_app
    app.run()

"""
用户请求一旦到来：
    1. app.__call__

"""