from flask import Flask
# from utils import cheese  # 下面附上utils模块的实现

app = Flask(__name__)  # 一个Flask类的对象


@app.route('/index')
def index():
    # cheese()
    return 'Hello World'


if __name__ == '__main__':
    app.run()  # run_simple(host,port,app)
