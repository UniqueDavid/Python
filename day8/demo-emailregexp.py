#邮件验证的正则表达式
import re
re_email=re.compile(r'^([a-z]*[a-zA-Z0-9.]*)@([a-zA-Z0-9]*).([a-zA-Z]*)$')
print(re_email.match('someone@gmail.com'))