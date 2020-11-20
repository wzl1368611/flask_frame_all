s8day126 Flask上下文管理

内容回顾：
	1. Linux命令(20个)
		cd
		vim
		mkdir
		ls
		touch
		cat 
		sed
		
	2. 面向对象：特殊方法
		obj['x'] = 123
		obj.x = 123 
		obj + 123
	3. functools
		def func(a1,a2,a3):
			return a1 + a2 + a3 
			
		v1 = func(1,2,3)


		new_func = functools.partial(func,111,2)
		new_func(3)
				
	4. 你认识的装饰器？应用场景？
		- 应用：
			- flask：路由、before_request
			- django: csrf、缓存、用户登录
	
	5. Flask 
		- 蓝图
		- session原理
		


今日内容：
	1. threading.local
	
	2. 上下文管理
	
	3. 数据库连接池
	
内容详细：
	1. threading.local
		a. threading.local 
			作用：为每个线程开辟一块空间进行数据存储。
		
			问题：自己通过字典创建一个类似于threading.local的东西。
				storage={
					4740:{val:0},
					4732:{val:1},
					4731:{val:3},
					4712:{},
					4732:{},
					5000:{val:}
				}
		b. 自定义Local对象
			作用：为每个线程(协程)开辟一块空间进行数据存储。
	
				try:
					from greenlet import getcurrent as get_ident
				except Exception as e:
					from threading import get_ident

				from threading import Thread
				import time

				class Local(object):

					def __init__(self):
						object.__setattr__(self,'storage',{})

					def __setattr__(self, k, v):
						ident = get_ident()
						if ident in self.storage:
							self.storage[ident][k] = v
						else:
							self.storage[ident] = {k: v}

					def __getattr__(self, k):
						ident = get_ident()
						return self.storage[ident][k]

				obj = Local()

				def task(arg):
					obj.val = arg
					obj.xxx = arg
					print(obj.val)

				for i in range(10):
					t = Thread(target=task,args=(i,))
					t.start()
	
	
	
	2. 在源码中分析上下文管理
		
		第一阶段：将ctx(request,session)放到“空调”上（Local对象）
				   
		第二阶段：视图函数导入：request/session 
		
		第三阶段：请求处理完毕
						- 获取session并保存到cookie
						- 将ctx删除
	
	
		问题：flask中一共有几个LocalStack和Local对象

		
作业：
	按组为单位，画Flask上下文管理 请求流程（类.方法）






















	
	
	
	
	
	
	
	
	