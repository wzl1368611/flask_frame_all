from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)

@app.route('/index',methods=['GET','POST'],endpoint='n1')
def index():
    v1 = url_for('n1')
    v2 = url_for('login')
    v3 = url_for('logout')
    print(v1,v2,v3)
    return "Index"

@app.route('/login',methods=['GET','POST'])
def login():
    return "login"

@app.route('/logout',methods=['GET','POST'])
def logout():
    return "logout"

if __name__ == '__main__':
    app.run()