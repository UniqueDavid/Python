#把字符串转成浮点数
from functools import reduce
def str2tofloat(s):
	def fn1(x,y):
		return x*10+y
	def fn2(x,y):
		return x*0.1+y
	def separate(s):
		mint=''
		mfloat='0'
		flag=True
		for x in s:
			if x=='.':
				flag=False
				continue
			if(flag):
				mint+=x
			else:
				mfloat+=x
		return mint,mfloat
	def char2num(s):
		return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	mint,mfloat=separate(s)
	return reduce(fn1,map(char2num,mint))+reduce(fn2,map(char2num,mfloat[::-1]))
print(str2tofloat('123.456'))