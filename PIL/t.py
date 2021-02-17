
# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('image/20200701174928.jpg')
# # 获得图像尺寸:
# w, h = im.size
# # im.format
# # im.mode
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')
##################################################################################
# 华丽的分割线
# 批量缩放图片尺寸并且图像不失真

from PIL import ImageGrab
from PIL import Image
from PIL import ImageFilter
import os
input_path = 'xxxxx'

output_path = 'xxxx'

scale = 0.5

def imageResize(input_path, output_path, scale):
    # 获取输入文件夹中的所有文件/夹，并改变工作空间
    files = os.listdir(input_path)
    os.chdir(input_path)
    # 判断输出文件夹是否存在，不存在则创建
    if(not os.path.exists(output_path)):
        os.makedirs(output_path)
    for file in files:
        # 判断是否为文件，文件夹不操作
        if(os.path.isfile(file)):
            img = Image.open(file)
            width = int(img.size[0]*scale)
            height = int(img.size[1]*scale)
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(os.path.join(output_path, "New_"+file))

imageResize(input_path, output_path, scale)