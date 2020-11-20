s8day123 

内容回顾：
	1. 装饰器
		问题：什么是装饰器？
		问题：手写装饰器
		问题：装饰器都在哪里用过？
		
		import functools

		def wapper(func):
			@functools.wraps(func)
			def inner(*args,**kwargs):
				return func(*args,**kwargs)
			return inner
		"""
		1. 执行wapper函数，并将被装饰的函数当做参数。 wapper(index)
		2. 将第一步的返回值，重新赋值给  新index =  wapper(老index)
		"""
		@wapper
		def index(a1):
			return a1 + 1000

		@wapper
		def order(a1):
			return a1 + 1000


		print(index.__name__)
		print(order.__name__)
	
	2. 谈谈你对面向对象的认识？
		- 封装：
			- 将同一类方法分为一类：方法封装到类中
			- 将方法中共同的参数封装到对象中：把共用值封装到对象中。
			
			情况：
				a. BaseReponse			
					def index(a1,a2,a3,a4,a5,a6,a7):
						pass
						
					# 用户类实现
					class Foo(object):
						def __init__(self,a1,a2,a3,a4,a5,a6,a7):
							self.a1 = a1
							self.a2 = a2
							self.a3 = a3
							self.a4 = a4
							self.a5 = a5
							self.a6 = a6
							self.a7 = a7
							
					def index(obj):
						pass
				b. 给了一些值，将数据加工: django 自定义分页
					
					class Foo(object):
						def __init__(self,a1,a2,a3,a4,a5,a6,a7):
							self.a1 = a1
							self.a2 = a2
							self.a3 = a3
							self.a4 = a4
							self.a5 = a5
							self.a6 = a6
							self.a7 = a7
							
						def 金条(self):
							return self.a1 + self.a2
							
						def 手表(self):
							return self.a1 + self.a7
					
		

今日内容：
	1. 配置文件
	2. 路由 *
	3. 视图函数
	4. 请求和响应 *
	5. 模板
	6. session * 
	
	8. 蓝图 blueprint *
	10. 中间件
	7. 闪现 
	
	
内容详细：
	1. 配置文件
	
	2. 路由
		a. 添加路由的两种方式：
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
		b. endpoint(默认函数名)
		c. 传参数
			@app.route('/index/<int:nid>',methods=['GET','POST'])
			def index(nid):
				print(nid,type(nid))
				
				url_for('index',nid=888)
				
				return "Index"
		d. 自定义正则参数
	
				from flask import Flask,render_template,redirect,url_for
				from werkzeug.routing import BaseConverter
				app = Flask(__name__)


				class RegexConverter(BaseConverter):
					"""
					自定义URL匹配正则表达式
					"""
					def __init__(self, map, regex):
						super(RegexConverter, self).__init__(map)
						self.regex = regex

					def to_python(self, value):
						"""
						路由匹配时，匹配成功后传递给视图函数中参数的值
						:param value:
						:return:
						"""
						return int(value)

					def to_url(self, value):
						"""
						使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
						:param value:
						:return:
						"""
						val = super(RegexConverter, self).to_url(value)
						return val

				app.url_map.converters['xxx'] = RegexConverter

				@app.route('/index/<xxx("\d+"):nid>',methods=['GET','POST'])
				def index(nid):
					print(nid,type(nid))
					v = url_for('index',nid=999) # /index/999
					print(v)
					return "Index"

				if __name__ == '__main__':
					app.run()
	
		e. 其他参数
			- 重定向
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
			
				PS: 前端重定向
					- meta
					- js 
					
		重点：
			- url
			- methods 
			- endpoint
			- @app.route('/index/<int:nid1>/<int:nid2>/')
			- url_for 
	
		
	3. 
		- cbv
		- fbv
		
	4. 
		request
		response = make_response(....)
		# 响应头
		# cookie
		return response 
		
	5. 模板
	
	6. session 
		
	7. 常见装饰器
		- before_first_request
		- before_request
		- after_request
		- errorhandler(404)
		
	8. 闪现
	
	9. 中间件
	
	10. 蓝图 
	
	
	11. 补充：
		- 项目依赖 pip3 install pipreqs
			- 生成依赖文件：pipreqs ./ 
			- 安装依赖文件：pip3 install -r requirements.txt 
		- 什么是函数？什么是方法？
		
			from types import MethodType,FunctionType

			class Foo(object):
				def fetch(self):
					pass

			print(isinstance(Foo.fetch,MethodType))
			print(isinstance(Foo.fetch,FunctionType)) # True

			obj = Foo()
			print(isinstance(obj.fetch,MethodType)) # True
			print(isinstance(obj.fetch,FunctionType))
		
		
	
	
	
	
	
	
	
	