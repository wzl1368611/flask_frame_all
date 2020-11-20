s8day130 

内容回顾：
	
	a. 为什么要学python?
		- 亲朋/学长 建议
		- 了解：
			- 简单易学
			- 生态圈比较强大
			- 发展趋势：人工智能、数据分析
	
	b. 谈谈你对Python和其他语言的区别？
		- 解释型
			- python/php
		- 编译型
			- c/java/c#
		
		- Python弱类型
		
		
	c. 数据类型：
		- 字符串
		- 字典
		- 元组
		- 列表
		- 集合
		- collections
	d. 函数
		- 函数参数传递的是什么？
		- def func(a,b=[]):pass
		- lambda 表达式
		- 列表生成式   []
		- 生成器表达式 (for i in range(1))
		- 题： 
			val = [lambda :i+1 for i in range(10)]
			val[0]
			data = val[0]()
			print(data)
		- 常见内置函数：
			- map
			- reduce
			- filter
			- zip
			- instance
			- type
			- 
		- 生成器、迭代器、装饰器、可迭代对象
			- 迭代器，内部实现__next__方法，帮助我们向后一个一个取值。
			- 生成器，一个函数内部存在yield关键字；v = 函数()。
					  应用场景：
							- range/xrange
								- py2: range(100000000),立即创建;xrange(100000000)生成器；
								- py3: range(100000000)生成器；
							- redis获取值
								conn = Redis(...)
								
								def hscan_iter(self, name, match=None, count=None):
									"""
									Make an iterator using the HSCAN command so that the client doesn't
									need to remember the cursor position.

									``match`` allows for filtering the keys by pattern

									``count`` allows for hint the minimum number of returns
									"""
									cursor = '0'
									while cursor != 0:
										# 去redis中获取数据：12
										# cursor，下一次取的位置
										# data：本地获取的12条数数据
										cursor, data = self.hscan(name, cursor=cursor,
																  match=match, count=count)
										for item in data.items():
											yield item
							- stark组件
								xx.html:
									{% for item in data %}
										<p>{{item.k1}} {{item.name}}</p>
									{%endfor%}


								views.py
									def index(request):
										data = [
											{'k1':1,'name':'alex'},
											{'k1':2,'name':'老男孩'},
											{'k1':3,'name':'小男孩'},
										]
										
										new_data = []
										for item in data:
											item['email'] = "xxx@qq.com"
											new_data.append(item)

										return render(request,'xx.html',{'data':new_data})
										
								# ##################################################################
								xx.html:
									{% for item in data %}
										<p>{{item.k1}} {{item.name}}</p>
									{%endfor%}


								views.py
									def gen_data(data):
										for item in data:
											item['email'] = "xxx@qq.com"
											yield item 

									def index(request):
										data = [
											{'k1':1,'name':'alex'},
											{'k1':2,'name':'老男孩'},
											{'k1':3,'name':'小男孩'},
										]
										
										new_data = gen_data(data)
										
										return render(request,'xx.html',{'data':new_data})
							
			- 可迭代对象，一个类内部实现__iter__方法且返回一个迭代器。
					class Foo(object):
						def __iter__(self):
							return iter([11,22,33])
					obj = Foo()
					
					应用场景： 
						- wtforms中对form对象进行循环时候，显示form中包含的所有字段。
							class LoginForm(Form):
								name = simple.StringField(
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

							
							form = LoginForm()
							for item in form:
								print(item)
								
						- 列表、字典、元组
						
						总结：如果想要让一个对象可以被for循环，那么就需要在当前类中定义__iter__

			- 装饰器，在不改变原函数代码的基础上，在执行前后进行定制操作。
				- 手写
				- 应用场景： 
					- flask路由系统
					- flask before_request
					- csrf
					- django内置认证
					- django的缓存
				
今日内容：
	1. flask-script
	
	2. flask-sqlalchemy
	
	3. flask-migrate
	
	4. 自定义组件
	
	5. 其他：
		- 多app应用
		- 离线脚本
		- 信号：blinker
		
		
		
内容详细：
	1. flask-script
		- python manage.py runserver
		- python manage.py 自定义命令
		
	2. flask-sqlalchemy 
		作用：将SQLAlchemy相关的所有功能都封装到db=flask_sqlalchemy.SQLAlchemy()对象中
				- 创建表
					class User(db.Model):
						pass
		
				- 操作表
					db.session 
		
		
		扩展：离线脚本编写
			from s8day130_pro import db
			from s8day130_pro import create_app
			from s8day130_pro import models

			app = create_app()
			with app.app_context():
				# db.drop_all()
				# db.create_all()
				data = db.session.query(models.Users).all()
				print(data)
		
		
		步骤：
			1. 在 __init__.py中创建db对象
				from flask_sqlalchemy import SQLAlchemy

				# 包含了SQLAlchemy相关的所有操作
				db = SQLAlchemy()
				
			2. 在 __init__.py中create_app函数中让将app传入到db中
				
				def create_app():
					app = Flask(__name__)
					app.config.from_object('settings.DevelopmentConfig')

					from .views.account import ac
					app.register_blueprint(ac)
					
					# 看这里看这里
					db.init_app(app)
					
					return app
			
			3. 写配置文件，将连接字符串定义在配置文件中
				    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/s8day130db?charset=utf8"
					SQLALCHEMY_POOL_SIZE = 5
					SQLALCHEMY_POOL_TIMEOUT = 30
					SQLALCHEMY_POOL_RECYCLE = -1
			
			4. 定义 s8day130_pro/models.py
				
					#!/usr/bin/env python
					# -*- coding:utf-8 -*-
					from sqlalchemy.ext.declarative import declarative_base
					from sqlalchemy import Column, Integer, String, UniqueConstraint, Index,DateTime,ForeignKey
					from s8day130_pro import db

					class Users(db.Model):
						__tablename__ = 'users'
						id = Column(Integer, primary_key=True,autoincrement=True)
						name = Column(String(32),nullable=False,unique=True)
							
			5. 创建数据库表，编写离线脚本：drop_create_table.py 
					from s8day130_pro import db
					from s8day130_pro import create_app
					from s8day130_pro import models

					app = create_app()
					with app.app_context():
						db.drop_all()
						db.create_all()
						#data = db.session.query(models.Users).all()
						#print(data)
			
			6. 在视图函数中使用SQLAlchemy操作数据库
					from s8day130_pro import models
					from s8day130_pro import db
					ac = blueprints.Blueprint('ac',__name__)

					@ac.route('/login',methods=['GET','POST'])
					def login():
						data = db.session.query(models.Users).all()
						print(data)
						db.session.remove()
						return 'Login'
								
			
		SQLAlchemy两种创建session的方式：
			方式一：
				import models
				from threading import Thread
				from sqlalchemy.orm import sessionmaker
				from sqlalchemy import create_engine

				engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8",pool_size=2,max_overflow=0)
				XXXXXX = sessionmaker(bind=engine)

				def task():
					from sqlalchemy.orm.session import Session
					session = XXXXXX()

					data = session.query(models.Classes).all()
					print(data)

					session.close()

				for i in range(10):
					t = Thread(target=task)
					t.start()
			
			方式二（推荐）：
				import models
				from threading import Thread
				from sqlalchemy.orm import sessionmaker
				from sqlalchemy import create_engine
				from sqlalchemy.orm import scoped_session

				engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8",pool_size=2,max_overflow=0)
				XXXXXX = sessionmaker(bind=engine)

				session = scoped_session(XXXXXX)
				
				
				def task():

					# 1. 原来的session对象 = 执行session.registry()
					# 2. 原来session对象.query
					data = session.query(models.Classes).all()
					print(data)
					session.remove()

					

				for i in range(10):
					t = Thread(target=task)
					t.start()

							
		flask-session默认也是使用的第二种方式：scoped_session
			
			
			
			
			
		
		
		