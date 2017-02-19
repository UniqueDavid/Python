#python序列化
import pickle
d=dict(name='Bob',age=20,score=100)
print(pickle.dumps(d))
with open('test.txt','wb') as f:
	pickle.dump(d,f)
f=open('test.txt','rb')
d=pickle.load(f)
f.close()
print(d)