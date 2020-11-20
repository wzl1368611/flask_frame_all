from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder='templates')
app.debug = True

"""
LoginForm._unbound_fields = None
LoginForm._wtforms_meta = None
LoginForm.xxx = 123
LoginForm.name = UnboundField(simple.StringField, *args, **kwargs,creation_counter=1)
LoginForm.pwd = UnboundField(simple.PasswordField, *args, **kwargs,creation_counter=2)
"""
class LoginForm(Form):
    xxx = 123
    _name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        """
        FormMeta.__call__
            LoginForm._unbound_fields = [
                ('name',UnboundField(simple.StringField, *args, **kwargs,creation_counter=1),),
                ('pwd',UnboundField(simple.PasswordField, *args, **kwargs,creation_counter=2),),
            ]
            LoginForm._wtforms_meta = class Meta(DefaultMeta):
                                         pass
            LoginForm.xxx = 123
            LoginForm.name = UnboundField(simple.StringField, *args, **kwargs,creation_counter=1)
            LoginForm.pwd = UnboundField(simple.PasswordField, *args, **kwargs,creation_counter=2)
        LoginForm.__new__
            pass
        LoginForm.__init__
            LoginForm对象._fields = {
                    'name': simple.StringField(),
                    'pwd': simple.PasswordField()，
                }
            LoginForm对象.name = simple.StringField()
            LoginForm对象.pwd = simple.PasswordField()
        """
        form = LoginForm()
        # form = LoginForm(data={'name':'alex'})
        # print(form.name)
        # 执行simple.StringField().__str__
        # 执行simple.StringField().__call__
        # 调用meta.render_field(self, kwargs)
            # - simple.StringField()对象.widgets()
            # TextInput.__call__
        # for item in form:
        #     print(item) # 执行每个字段对象的.__str__
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()