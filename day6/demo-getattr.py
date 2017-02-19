#获取属性方法
class  Student(object):
	def __init__(self):
		self.name='David'
	#如果没有找到属性，才会调用这个方法
	def __getattr__(self,attr):
		if attr=='score':
			return 99
s=Student()
print(s.score)
