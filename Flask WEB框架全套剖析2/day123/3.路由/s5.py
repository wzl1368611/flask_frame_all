from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/index',methods=['GET','POST'],redirect_to='/new')
def index():
    return "老功能"

@app.route('/new',methods=['GET','POST'])
def new():
    return '新功能'


if __name__ == '__main__':
    app.run()