from flask import Blueprint,render_template,request,session,redirect
home = Blueprint('home',__name__)


@home.route('/index')
def index():

    # user_info = session.get('user_info')
    # print(user_info)

    # session['user_info'] = {'k1':1,'k2':2}
    user_info = session.get('user_info') # {'k1':1,'k2':2}
    print('原来的值',user_info)
    session['user_info']['k1'] = 99999
    user_info = session.get('user_info')  # {'k1':1,'k2':2}
    print('修改之后的值',user_info)

    return "index"


@home.route('/test')
def test():
    user_info = session.get('user_info')
    print(user_info)
    return "test"