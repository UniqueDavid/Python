#map，从字面上看是通过一个定义好的函数把输入实例转换成输出实例
def f(x):
	return x*x
r=map(f,[1,2,3,4,5,6])
print(list(r))
#reduce,如果有x1/x2/x3/x4/x5等元素，它会先计算两个元素的结果然后重复与后面的元素进行计算，相当于累加、累乘等功能。
from functools import reduce
def fn(x,y):
	return x*y
result=reduce(fn,[1,2,3,4,5,6])
print(result)