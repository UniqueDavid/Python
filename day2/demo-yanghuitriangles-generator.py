def yanghuitriangle(max):
	n=1
	while n<max:
		g=(x for x in range(n))
		g.append(x for x in reversed(n))
		for n in g:
			print(n)
		n=n+1
yanghuitriangle(20)