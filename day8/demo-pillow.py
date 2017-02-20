#PIL适用于处理图像的工具
from PIL import Image
im=Image.open('test.jpg')
w,h=im.size
print('原始尺寸：(%s,%s)'%(w,h))
#缩放图片
im.thumbnail((w//2,h//2))
#把缩放的图片保存
im.save('thumbnail.jpg','jpeg')