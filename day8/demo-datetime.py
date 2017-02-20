#获取当前时间
from datetime import datetime,timedelta
now=datetime.now()
print(now)
#指定时间
dt=datetime(2017,2,21,11,20)
print(dt)
#timestamp:相对于epoch time（1970年1月1日）的秒数
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
#把用户输入的字符串转换成日期
cday=datetime.strptime('2017-02-10 19:07:04','%Y-%m-%d %H:%M:%S')
print(cday)
#日期转成字符串
print(dt.strftime('%Y-%m-%d'))
#日期加减
print(dt+timedelta(hours=10))