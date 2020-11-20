from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.before_request
def xxxxxxxxxx1():
    print('前1')
    return "不要再来烦我了"

@app.before_request
def xxxxxxxxxx2():
    print('前2')

@app.after_request
def oooooooo1(response):
    print('后1')
    return response

@app.after_request
def oooooooo2(response):
    print('后2')
    return response



@app.route('/x1',methods=['GET','POST'])
def x1():
    print('视图函数x1')
    return "视图函数x1"

@app.route('/x2',methods=['GET','POST'])
def x2():
    print('视图函数x2')
    return "视图函数x2"

if __name__ == '__main__':
    app.__call__
    app.run()