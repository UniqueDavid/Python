#枚举类型
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','oct','Nov','Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)