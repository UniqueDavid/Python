#在内存中读写
#读写字符串
from io import StringIO
f=StringIO()
f.write('hello')
print(f.getvalue())
f1=StringIO('ni hao a!')
while True:
	s=f1.readline()
	if s=='':
		break
	print(s.strip())
#读写二进制
from io import BytesIO
f=BytesIO()
f.write('我是'.encode('utf-8'))
print(f.getvalue())