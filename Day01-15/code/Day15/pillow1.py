"""
使用pillow操作图像

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""
from PIL import Image

img = Image.open('Day01-15\\code\\Day15\\res\\guido.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('Day01-15\\code\\Day15\\res\\guido.jpg')

img2 = Image.open('Day01-15\\code\\Day15\\res\\guido.jpg')
img3 = img2.crop((335, 435, 430, 615))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y , 180 * x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('Day01-15\\code\\Day15\\res\\guido2.jpg')
