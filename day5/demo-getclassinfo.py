#获取对象信息
class Student(object):
	pass
def show():
		print("Hi!!")
print(type(123))
print(type('123'))
print(type(Student()))
#比较两个变量是否为同一个类型
print(type(123)==type(456))
print(type(123)==type(Student()))
#判断一个对象是否为函数
import types
print(type(show)==types.FunctionType)
print(type(lambda x:x*x)==types.LambdaType)
#获取一个对象的所有属性
print(dir('ABC'))
#判断下是否具有某个属性
print(hasattr('ABC','__name__'))