#使用itertools进行对象的迭代
import itertools
#创建一个自然数队列
natuals=itertools.count(1)
#for n in natuals:
#	print(n)
#使用cycle把一个元素无限重复
cs=itertools.cycle('ABCDEFG')
#for c in cs:
#	print(c)
#使用repeat可以限定次数
ns=itertools.repeat('ABCDEF',4)
for n in ns:
	print(n)
#使用takewhile进行条件判断
it=itertools.takewhile(lambda x:x<=10,natuals)
print(list(it))
#使用chain把对象连接在一起
for c in itertools.chain('I am','good boy!'):
	print(c)