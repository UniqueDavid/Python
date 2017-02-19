#返回一个函数而不是一个值
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
f=lazy_sum(1,3,5,7,9)
print(f())