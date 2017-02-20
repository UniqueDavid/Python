#使用PIL完成图像的模糊处理
from PIL import Image,ImageFilter
im=Image.open('test.jpg')
#应用模糊滤镜
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')