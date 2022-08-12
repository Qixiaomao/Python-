# 导入模块
from bs4 import BeautifulSoup
import lxml

# 引入文本
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test3</title>
</head>
<body>
    <form action="welcome.php" method="get">
     名字：<input type="text" name="fname">
     年龄：<input type="text" name="age">
     <input type="submit" value="提交">

    </form>
</body>
</html>

'''

# 解析文本
h = BeautifulSoup(html,'lxml')
t = h.find('form')
print(t)


# 打印文本
# print(h)
# 提取标签属性，名，所有的属性，文本
# tag
print('标签名',t.name)
print('属性：',t.attrs)
print('文本',t.text)