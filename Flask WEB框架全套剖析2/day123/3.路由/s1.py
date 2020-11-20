from flask import Flask,render_template,redirect
app = Flask(__name__)

"""
1. 执行decorator=app.route('/index',methods=['GET','POST'])
2. @decorator
     - decorator(index)
"""
# 路由方式一（*）：
@app.route('/index',methods=['GET','POST'])
def index():
    return "Index"

# 路由方式二：
def order():
    return 'Order'

app.add_url_rule('/order',view_func=order)


if __name__ == '__main__':
    app.run()