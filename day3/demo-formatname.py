#规范输入的姓名
def nametouppercase(s):
	str=''
	flag=True
	for x in s:
		if(flag):
			str+=x.upper()
			flag=False
		else:
			str+=x.lower()
	return str
print(list(map(nametouppercase,['lise','KlJK','DavidD'])))