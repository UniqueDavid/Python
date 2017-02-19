#文档测试
def abs(n):
	'''
	Function to get absolute value of number

	Example:

	>>>abs(1)
	1
	>>>abs(-1)
	1
	>>>abs(0)
	0
	'''
	return n if n>=0 else(-n)
import doctest
doctest.testmod()