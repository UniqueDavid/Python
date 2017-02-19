#fib计算
class Fib(object):
	#定义一个获取下标的方法
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
	def __init__(self):
		self.a,self.b=0,1#初始化两个计数器
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration()
		return self.a
print(Fib()[9])