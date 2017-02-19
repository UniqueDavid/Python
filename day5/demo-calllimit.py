#访问限制，如果定义了一个类里面的属性希望不可以被访问，可以使用__修饰
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print("%s %s"%(self.__name,self.__score))
bart=Student('David',90)
print(bart.__score)