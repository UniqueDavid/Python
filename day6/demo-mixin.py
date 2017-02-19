#python的多重继承
class Teacher(object):
	def showCarrer():
		print('I am a Teacher!')
class Doctor(object):
	def showarrer():
		print('I am a Doctor!')
class XiaoMing(Teacher,Doctor):
	pass
s=XiaoMing()
print(s.showarrer)