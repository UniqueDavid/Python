#python内置集合collections
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
#定义一个坐标
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p)
#定义一个圆
Circle=namedtuple('Circle',['x','y','r'])
c=Circle(0,0,1)
print(c)
#使用deque完成高效的增加和删除操作,它是双向链表
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.pop()
print(q)

#使用defaultdict避免抛出keyerror
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key2'])

#可以使用OrderedDict对于无序的dict进行排序
d=dict([('a',1),('b',2),('c',3)])
od=dict([('a',1),('c',3),('b',2)])
print(d)
print(od)

#使用counter作为计数器,统计各个字符出爱心纳的次数
c=Counter()
for ch in 'programming':
	c[ch]=c[ch]+1
print(c)