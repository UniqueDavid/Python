#python继承
class Animals(object):
	def run(self):
		print("Animal is running!")
class Dog(Animals):
	def run(self):
		print('Dog is running!')
class Cat(Animals):
	pass
dog=Dog()
dog.run()
#判断变量是否为某个类型可以用isinstance()判断
print(isinstance(dog,Animals))
print(isinstance(dog,Cat))