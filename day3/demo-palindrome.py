#过滤非回数，回数是指从左到右和从右到左读都是一样的
def is_pailndrome(n):
	s=str(n)
	s1=s[::-1]
	mid=len(s)//2
	if s[0:mid]==s1[0:mid]:
		return n
print(list(filter(is_pailndrome,range(1,1000000))))