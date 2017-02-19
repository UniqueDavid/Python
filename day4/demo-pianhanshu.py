#偏函数的使用
import functools
int2=functools.partial(int,base=2)
print(int2('100000'))
