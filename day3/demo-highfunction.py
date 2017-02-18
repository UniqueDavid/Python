#求解两个数的绝对值之和
def add(x,y,f):
	return f(x)+f(y)
f=abs;
print(add(-10,-20,f))