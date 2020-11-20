from flask import Flask,render_template,redirect
app = Flask(__name__)
import functools

def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print('before')
        return func(*args,**kwargs)
    return inner



@app.route('/xxxx',methods=['GET','POST'])
@wapper
def index():
    return "Index"


@app.route('/order',methods=['GET','POST'])
@wapper
def order():
    return "order"

if __name__ == '__main__':
    app.run()