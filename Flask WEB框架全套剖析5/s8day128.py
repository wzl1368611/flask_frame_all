s8day128

内容回顾：
	1. flask和django区别？
		- 相同：
			- 基于wsgi
		- 不同：
			- 传值方式
			- 组件：
				- flask少
				- django多
	
	2. flask上下文管理是如何实现？
		- 前提：记得不太清除了，应该是xxx； 前两天恰好刚看的。
		- 流程：
			- 请求刚进来，RequestContext(request,session)、AppContext(app,g) -> LocalStack -> Local 
			- 视图处理，LocalProxy -> 偏函数 -> LocalStack -> Local 
			- 请求结束，sava_session -> LocalStack.pop()
	
	3. Local作用？
		- 用于保存
			- 请求上下文对象
			- app上下文对象
		- 并且可以做到“线程”间的数据隔离。
		
		线程：threading.local
		协程：greenlet.get_current as get_ident
		
		
	4. LocalStack作用？
		- 将Local中保存的数据维护成一个栈
			
		{
			1432: { stack:[ctx,ctx,ctx,] }
		}
	
	5. Flask内置功能
		- 配置
		- 路由
		- 视图
		- 模板 
		- session
		- 蓝图
		- 闪现
		- 装饰器
		- 中间件
		
	6. 第三方组件：
		- Flask：
			- flask-session，将原来保存在cookie中的session数据，放到redis/memcache/文件/数据库中。
		- 公共：
			- DBUtils，数据库连接池
			- wtforms，做表单验证+生成HTML标签

今日内容：
	1. 面向对象相关
		__mro__
		metaclass
		
	2. wtforms
	
	3. SQLALchemy/flask-sqlalchemy
	
	4. 其他
		- flask-script
		- flask-migrate
		- 多app应用
		- 离线脚本
	
内容详细：
	1. 面向对象相关
		1. __mro__，找到当前类寻找属性的顺序。
			class A(object):
				pass


			class B(A):
				pass


			class C(object):
				pass

			class D(B,C):
				pass

			print(D.__mro__)
			
		2. __dict__
			class Foo(object):
				CITY = 'bj'
				def __init__(self,name,age):
					self.name = name
					self.age = age
				def func(self):
					pass

			# print(Foo.CITY)
			# print(Foo.func)
			print(Foo.__dict__)

			obj1 = Foo('oldboy',54)
			print(obj1.__dict__)
		
		3. metaclass
			# 1. 创建类的两种方式
			class Foo(object):
				CITY = "bj"

				def func(self,x):
					return x + 1

			Foo = type('Foo',(object,),{'CITY':'bj','func':lambda self,x:x+1})
		
		
					
			# 2. 类由自定义type创建
			#    类由type创建，通过metaclass可以指定当前类由那一个type创建。
			"""
			class MyType(type):
				def __init__(self,*args,**kwargs):
					print('创建类之前')
					super(MyType,self).__init__(*args,**kwargs)
					print('创建类之后')

			class Foo(object,metaclass=MyType): # 当前类，由type类创建。
				CITY = "bj"
				def func(self, x):
					return x + 1
			"""
			# 3. 类的继承
			#    类的基类中指定了metaclass，那么当前类也是由metaclass指定的类来创建当前类。
			"""
			class MyType(type):
				def __init__(self,*args,**kwargs):
					print('创建类之前')
					super(MyType,self).__init__(*args,**kwargs)
					print('创建类之后')

			class Foo(object,metaclass=MyType): # 当前类，由type类创建。
				CITY = "bj"
				def func(self, x):
					return x + 1

			class Bar(Foo):
				pass
			"""


			# ################################## 变 ##################################
			"""
			class MyType(type):
				def __init__(self,*args,**kwargs):
					print('创建类之前')
					super(MyType,self).__init__(*args,**kwargs)
					print('创建类之后')

			Base = MyType('Base',(object,),{})
			# class Base(object,metaclass=MyType):
			#     pass

			class Foo(Base):
				CITY = "bj"
				def func(self, x):
					return x + 1
			"""
			# ################################## 变 ##################################
			"""
			class MyType(type):
				def __init__(self,*args,**kwargs):
					print('创建类之前')
					super(MyType,self).__init__(*args,**kwargs)
					print('创建类之后')

			def with_metaclass(arg):
				return MyType('Base',(arg,),{}) # class Base(object,metaclass=MyType): pass

			class Foo(with_metaclass(object)):
				CITY = "bj"
				def func(self, x):
					return x + 1
			"""

			# ######################################################## 实例化 ########################################################
			class MyType(type):
				def __init__(self,*args,**kwargs):
					super(MyType,self).__init__(*args,**kwargs)

			class Foo(object,metaclass=MyType): # 当前类，由type类创建。
				pass


			"""
			0. Mytype的__init__
			obj = Foo() 
			1. MyType的__call__
			2. Foo的__new__
			3. Foo的__init__
			"""
			
			总结：
				1. 默认类由type实例化创建。
				2. 某个类指定metaclass=MyType，那么当前类的所有派生类都由于MyType创建。
				3. 实例化对象
					- type.__init__ 
					
					- type.__call__
					- 类.__new__
					- 类.__init__
				
		
	2. wtforms实现流程
		
		实例化流程：
			class LoginForm(Form):
				name = StringField(正则=[验证规则1，验证规则1，],插件=Input框)
				pwd = StringField(正则=[验证规则1，验证规则1，],插件=Password框)
				
		
		作业：找验证流程
			
		
		相关面试题：
			a. Python基础部分，哪些比较重要？
				- 反射
					- cbv
					- django 配置文件
					- wtforms中
						class Form(with_metaclass(FormMeta, BaseForm)):
						
							Meta = DefaultMeta

							def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
							
								...
								"""
								self._fields = {
									'name': simple.StringField(实例化),
									'pwd': simple.PasswordField()，
								}
								"""
								for name, field in iteritems(self._fields):
									# Set all the fields to attributes so that they obscure the class
									# attributes with the same names.
									setattr(self, name, field)
								...
						obj = Form()
						obj.name 
				- 装饰器
					- flask路由 /装饰器
					- 认证
					- csrf
				
				- 生成器、迭代器
				
				
				- 面向对象
					- 继承、封装、多态
					- 特殊功能：
						- 双下划线的方法
							- __mro__ 
								class FormMeta(type):
								def __call__(cls, *args, **kwargs):
									...
									# Create a subclass of the 'class Meta' using all the ancestors.
									if cls._wtforms_meta is None:
										bases = []
										# LoginForm，Form，BaseForm，object
										for mro_class in cls.__mro__:
											if 'Meta' in mro_class.__dict__:
												bases.append(mro_class.Meta)

										cls._wtforms_meta = type('Meta', tuple(bases), {})
							- __dict__ 
								- dir 
								- dict 
							- __new__ ,实例化但是没有给当前对象
								- wtforms，字段实例化时返回：不是StringField，而是UnboundField
											    def __new__(cls, *args, **kwargs):
													if '_form' in kwargs and '_name' in kwargs:
														return super(Field, cls).__new__(cls)
													else:
														return UnboundField(cls, *args, **kwargs)
								- rest framework ,many=True 
							- __call__
								- flask请求的入口
								- 字段生成标签时：字段.__str__ => 字段.__call__ => 插件.__call__ 
							- __iter__ 
								pass
							
						- metaclass
							- 作用：用于指定使用哪个类来创建当前类
							- 场景：在类创建之前定制操作
									示例：wtforms中，对字段进行排序。
				
				
	3. SQLAchemy，ORM框架。
		问题：什么是ORM？
			  关系对象映射
				类   -> 表
				对象 -> 记录（一行数据）
				
			  当有了对应关系之后，不再需要编写SQL语句，取而代之的是操作：类、对象。
				ORM： models.User.objects.filter(id__gt=1,type__name='技术部')
				
				SQL: 
					  select 
						id,
						name,
						age,
						email
					  from user left join type on user.type_id = type.id 
						
		问题： ORM和原生SQL哪个好？
		
		问题： 概念
				db first，根据数据库的表生成类
							django 
								python manage.py inspectdb
				code first，根据类创建数据库表；
							django：
								python manage.py makemigrations
								python manage.py migrate 
		
		
		问题：ORM是怎么实现？
			  DDD中： unit of work 
		
		
		SQLALchemy，是一个基于python实现的ORM框架。
			1. 基于SQLALchemy写原生SQL
				- SQLAclchemy连接池
					import time
					import threading
					import sqlalchemy
					from sqlalchemy import create_engine
					from sqlalchemy.engine.base import Engine
					 
					engine = create_engine(
						"mysql+pymysql://root:123@127.0.0.1:3306/t1?charset=utf8",
						max_overflow=0,  # 超过连接池大小外最多创建的连接
						pool_size=5,  # 连接池大小
						pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
						pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
					)
					 
					 
					def task(arg):
						conn = engine.raw_connection()
						cursor = conn.cursor()
						cursor.execute(
							"select * from t1"
						)
						result = cursor.fetchall()
						cursor.close()
						conn.close()
					 
					 
					for i in range(20):
						t = threading.Thread(target=task, args=(i,))
						t.start()
				- DBUtils+pymysql 做连接池
			2. 基于SQLALchemy写ORM
				
				models.py 
					
					#!/usr/bin/env python
					# -*- coding:utf-8 -*-
					from sqlalchemy.ext.declarative import declarative_base
					from sqlalchemy import Column, Integer, String, UniqueConstraint, Index
					from sqlalchemy import create_engine

					Base = declarative_base()

					# 创建单表
					class Users(Base):
						__tablename__ = 'users'
						id = Column(Integer, primary_key=True,autoincrement=True)
						name = Column(String(32))
						extra = Column(String(16))
						
					
					# 数据库连接相关
					# engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
					# 创建表
					# Base.metadata.create_all(engine)
					# 删除表
					# Base.metadata.drop_all(engine)
						
				app.py 
					import models
					from sqlalchemy.orm import sessionmaker
					from sqlalchemy import create_engine

					engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
					XXXXXX = sessionmaker(bind=engine)
					session = XXXXXX()



					obj1 = models.Users(name="alex", extra='sb')
					obj2 = models.Users(name="alex", extra='db')
					session.add(obj1)
					session.add(obj2)


					session.commit()
								
		使用：
			安装： pip3 install sqlalchemy
			
			
			1. 表操作
					#!/usr/bin/env python
					# -*- coding:utf-8 -*-
					from sqlalchemy.ext.declarative import declarative_base
					from sqlalchemy import Column, Integer, String, UniqueConstraint, Index,DateTime,ForeignKey
					from sqlalchemy import create_engine
					import datetime
					Base = declarative_base()

					class Classes(Base):
						__tablename__ = 'classes'
						id = Column(Integer, primary_key=True,autoincrement=True)
						name = Column(String(32),nullable=False,unique=True)

					class Student(Base):
						__tablename__ = 'student'
						id = Column(Integer, primary_key=True, autoincrement=True)
						username = Column(String(32), nullable=False,index=True)
						password = Column(String(64), nullable=False)
						ctime = Column(DateTime,default=datetime.datetime.now)
						class_id = Column(Integer, ForeignKey("classes.id"))

					class Hobby(Base):
						__tablename__ = 'hobby'
						id = Column(Integer, primary_key=True)
						caption = Column(String(50), default='篮球')

					class Student2Hobby(Base):
						__tablename__ = 'student2hobby'
						id = Column(Integer, primary_key=True, autoincrement=True)
						student_id = Column(Integer, ForeignKey('student.id'))
						hobby_id = Column(Integer, ForeignKey('hobby.id'))

						__table_args__ = (
							UniqueConstraint('student_id', 'hobby_id', name='uix_student_id_hobby_id'),
							# Index('ix_id_name', 'name', 'extra'),
						)

					def init_db():
						# 数据库连接相关
						engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
						# 创建表
						Base.metadata.create_all(engine)
					def drop_db():
						engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
						# 删除表
						Base.metadata.drop_all(engine)

					if __name__ == '__main__':
						# drop_db()
						init_db()
			
			2. 数据进行操作
				
				第一步：
					增
					删
					改
					查
				
				第二步：
					复杂查询条件
					分组
					排序
					连表
					分页
					组合union /union all 
	
	
			PS: commit 
			
			参考博客：http://www.cnblogs.com/wupeiqi/articles/8259356.html
	
	
作业：
	1. wtforms实例化过程
	2. wtforms验证流程（钩子函数到底如何实现？）
	3. SQLALchemy表+基本操作
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	