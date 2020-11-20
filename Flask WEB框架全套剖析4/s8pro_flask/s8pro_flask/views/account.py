from flask import Blueprint,render_template,request,session,redirect
from ..utils.sql import SQLHelper
account = Blueprint('account',__name__)

from wtforms import Form
from wtforms.fields import simple,core,html5
from wtforms import validators
from wtforms import widgets

class LoginForm(Form):
    user = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            # validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    pwd = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            # validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            # validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #                   message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

@account.route('/login',methods=['GET',"POST"])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html',form=form)

    form = LoginForm(formdata=request.form)
    if not form.validate():
        return render_template('login.html', form=form)

    obj = SQLHelper.fetch_one("select id,name from users where name=%(user)s and pwd=%(pwd)s", form.data)
    if obj:
        session.permanent = True
        session['user_info'] = {'id':obj['id'], 'name':obj['name']}
        return redirect('/index')
    else:
        return render_template('login.html',msg='用户名或密码错误',form=form)




class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    city = core.SelectField(
        label='城市',
        choices=SQLHelper.fetch_all('select id,name from city',{},None),
        # choices=(
        #     (1, '篮球'),
        #     (2, '足球'),
        # ),
        coerce=int
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.city.choices = SQLHelper.fetch_all('select id,name from city',{},None)


    def validate_name(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值
        # print(field.data) # 当前name传过来的值
        # print(self.data) # 当前传过来的所有的值：name,gender.....

        obj = SQLHelper.fetch_one('select id from users where name=%s',[field.data,])
        if obj:
            raise validators.ValidationError("用户名已经存在") # 继续后续验证
            # raise validators.StopValidation("用户名已经存在") # 不再继续后续验证


@account.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html',form=form)
    form = RegisterForm(formdata=request.form)
    if form.validate():
        print(form.data)
    else:
        print(form.errors)
    return "sdfasdfasdf"