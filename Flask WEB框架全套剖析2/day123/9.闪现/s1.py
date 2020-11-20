from flask import Flask,session,flash,get_flashed_messages
app = Flask(__name__)
app.secret_key = 'asdfasdfasdf'

@app.route('/x1',methods=['GET','POST'])
def login():
    flash('我要上向龙1',category='x1')
    flash('我要上向龙2',category='x2')
    return "视图函数x1"

@app.route('/x2',methods=['GET','POST'])
def index():
    data = get_flashed_messages(category_filter=['x1'])
    print(data)
    return "视图函数x2"

if __name__ == '__main__':
    app.run()