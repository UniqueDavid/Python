#计算一个输入的list元素之积
from functools import reduce
def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,L)
print('3*5*7*9=',prod([3,5,7,9]))