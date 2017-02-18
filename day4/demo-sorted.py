#对于序列进行排序
a=[2,1,5,3,6,4,-1]
print(sorted(a))
#sorted后面可以接一个自定义函数，实现自定义的排序
print(sorted(a,key=abs))
#对于字符串进行排序
b=['alida','Bob','David','Cylia']
print(sorted(b))
#可以增加条件忽略大小写
print(sorted(b,key=str.lower))
#元祖的排序
c=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#按照姓名
def by_name(t):
	return t[0][0]
#按照成绩
def by_score(t):
	return t[1]
#也可以引用包
from operator import itemgetter
print(sorted(c,key=itemgetter(0)))
print(sorted(c,key=by_name))
print(sorted(c,key=by_score))