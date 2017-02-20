#使用contextlib完成自定义的with使用
from contextlib import contextmanager
class Query(object):
	def __init__(self,name):
		self.name=name
	def query(self):
		print('Queryinfo about %s....'%self.name)
@contextmanager
def create_query(name):
	print('Begin..')
	q=Query(name)
	yield q
	print('End...')
with create_query('David') as q:
	q.query()