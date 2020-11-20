from flask import Flask,render_template,redirect,request,jsonify,make_response,Markup
app = Flask(__name__)

@app.template_global()
def sbbbbbbb(a1, a2):
    """
    每个模板中可以调用的函数
    :param a1:
    :param a2:
    :return:
    """
    return a1 + a2


def gen_input(value):
    # return "<input value='%s'/>" %value
    return Markup("<input value='%s'/>" %value)

@app.route('/x1',methods=['GET','POST'])
def index():
    context = {
        'k1':123,
        'k2': [11,22,33],
        'k3':{'name':'oldboy','age':84},
        'k4': lambda x: x+1,
        'k5': gen_input, # 当前模板才能调用的函数
    }

    return render_template('index.html',**context)


@app.route('/x2',methods=['GET','POST'])
def order():
    context = {
        'k1':123,
        'k2': [11,22,33],
    }

    return render_template('order.html',**context)




if __name__ == '__main__':
    app.run()