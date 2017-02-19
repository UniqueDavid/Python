#json文件生成
import json
d=dict(name='Bob',age=20,score=100)
f=json.dumps(d)
print(json.loads(f))