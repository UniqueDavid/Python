height=input("请输入您的身高:")
weight=input("请输入您的体重:")
mHeight=float(height)
mWeight=float(weight)
bmi=mWeight/pow(mHeight,2)
if bmi>=32:
	print('严重肥胖!!!')
elif bmi>=28:
	print('体重肥胖!!')
elif bmi>=25:
	print('体重过重!')
elif bmi>=18.5:
	print('体重正常.')
else:
	print('体重过轻~')