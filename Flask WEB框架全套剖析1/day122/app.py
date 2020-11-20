from flask import Flask,render_template,request,redirect,session

app = Flask(__name__) # 一个Flask类的对象
app.secret_key = 'u2jksidjflsduwerjl'
app.debug = True
USER_DICT = {
    '1': {'name':'志军','age':18},
    '2': {'name':'大伟','age':48},
    '3': {'name':'梅凯','age':38},
}

@app.route('/login',methods=['GET',"POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user') # 获取POST传过来的值
    pwd = request.form.get('pwd') # 获取POST传过来的值
    if user == 'alex' and pwd == '123':
        # 用户信息放入session
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html',msg ='用户名或密码错误')
        # return render_template('login.html',**{'msg':'用户名或密码错误'})


@app.route('/index',endpoint='n1')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    return render_template('index.html',user_dict = USER_DICT)

@app.route('/detail')
def detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    uid = request.args.get('uid')
    info = USER_DICT.get(uid)

    return render_template('detail.html',info = info)


@app.route('/logout')
def logout():
    del session['user_info']
    return redirect('/login')


if __name__ == '__main__':
    app.run()