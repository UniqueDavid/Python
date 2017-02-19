#装饰器就是不希望改变一个函数内部定义的情况下为其添加一个功能
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
#这里相当于now=log(now)
@log
def now():
	print("2017-02-18")
now()