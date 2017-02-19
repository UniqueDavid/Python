#打开文件操作
#f=open('demo.py','w',encoding='utf-8')
#f.write('Hi')
#f.close()
with open('demo.py','w',encoding='utf-8') as f:
	f.write('Hi !My name is 杨政！')