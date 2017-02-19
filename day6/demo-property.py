#使用@property进行可以设置一个getter函数，即返回一个值
#使用score.setter可以设置相关的值，这里面第一个参数为self，第二个为value
class Student(object):
	@property
	def name(self):
		return self.__name
	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score must be an integer!')
		if value <0 or value>100:
			raise ValueError('Score must between 0~100!')
		self.__score=value
s=Student()
s.score=60
print(s.score)
