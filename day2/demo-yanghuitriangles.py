def yanghuitriangles(max):
	L=[1]
	L1=[]
	n=0
	while n<=max:
		L=L1
		L1=[]
		n=n+1
		x=0
		while x<n:
			if x==0:
				L1.append(1)
				x=x+1
				continue
			elif x==n-1:
				L1.append(1)
				break
			else:
				L1.append(L[x]+L[x-1])
				x=x+1
				continue
		print(L1)
yanghuitriangles(8)

		


