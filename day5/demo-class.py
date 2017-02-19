#python的类和实例
#类是抽象的模板，实例是具体的对象
class Student(object):
	pass
bart=Student()
#给类赋一个值
bart.name='Bart Simpson'
print(bart.name)
#可以把一些必要的属性定义在类里面
class Teacher(object):
	#这里的第一参数永远是self，表示创建的实例本身
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	#可以对于内部的属性进行封装
	def print_info(self):
		print("name:%s salary:%s"%(self.name,self.salary))
adam=Teacher('Adam Jhson',8500)
print(adam.salary)
adam.print_info()