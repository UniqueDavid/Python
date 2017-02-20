#python的摘要算法(哈希算法，散列算法)
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#如果数据量过大，可以分开update
md5.update('你好啊'.encode('utf-8'))
md5.update('我们爱你！'.encode('utf-8'))
print(md5.hexdigest())
