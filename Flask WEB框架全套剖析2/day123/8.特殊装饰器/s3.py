from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'asdfasdfasdf'
@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    return "视图函数x1"

@app.route('/index',methods=['GET','POST'])
def index():
    print('视图函数x2')
    return "视图函数x2"

if __name__ == '__main__':
    app.run()