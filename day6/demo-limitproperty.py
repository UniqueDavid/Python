#限制类里面的属性，比如说规定只有那几个属性
#注意：这仅仅对于当前的类实例有用，对于继承的子类不起作用
class Student(object):
	#使用tuple来定义允许绑定的属性名称
	__slots__=('name','age')
s=Student()
s.name='David'
s.age=25
s.score=96
