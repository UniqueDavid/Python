#python的正则表达式
import re
result=re.match(r'^\d{3}-\d{3,8}$','010-12345')
print(result)
#使用正则表达式做切分
print(re.split(r'\s+','a b  c'))
#使用分组功能可以很快的提取出相应的东西,group[0]是原始字符，1,2分别是分组的结果
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
#贪婪匹配，尽可能匹配多的
print(re.match(r'^(\d+)(0*)$','102300').groups())
#加个问号就是非贪婪匹配了
print(re.match(r'^(\d+?)(0*)$','102300').groups())