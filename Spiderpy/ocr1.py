import tesserocr
from PIL import Image

pathFile = r'D:\Mylearn\pythonLearn\pythonProject\04_python爬虫\code.jpg'
image = Image.open(pathFile)
result = print(tesserocr.image_to_text(image))