#使用文件操作和目录
import os
#获取操作系统名称
print(os.name)
#获取环境变量
print(os.environ)
#列出所有文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])