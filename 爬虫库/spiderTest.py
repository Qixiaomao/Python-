#学习urllib.request模块
import urllib.request
#urllib库函数有request,error,parse,robotparser

repo = urllib.request.urlopen("https://www.baidu.com")
#print(repo.read().decode("utf-8"))
print(repo.status)
print(repo.getheaders())
print(repo.getheader('Server'))

