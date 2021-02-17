# 批量修改图片尺寸,缺点图片会失真
from PIL import Image
import os.path

import glob
# glob模块用来查找文件目录和文件
 
def Resize(file, outdir, width, height):
    imgFile = Image.open(file)
    try:
        newImage = imgFile.resize((width, height), Image.BILINEAR)   
        newImage.save(os.path.join(outdir, os.path.basename(file)))
    except Exception as e:
        print(e)
 
 
for file in glob.glob("xxxxx/*.jpg"):  # 图片所在的目录
    Resize(file, "xxxxx", 800, 800)    # 新图片存放的目录
