#将二进制转换成字符串
import base64
print(base64.b64encode(b'binaru\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#为了防止url中的+和/发生冲突，使用urlsafe_进行解码和编码
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))