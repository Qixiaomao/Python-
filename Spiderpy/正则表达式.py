import re

content = '''Hello 123 4567 
World_This is a Regx Demo'''
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content) 这是一种匹配方式
# result = re.match('^Hello.*Demo$',content) .* 匹配所有除了换行符的数据
# '^He.*?Demo$' 非贪婪模式
# '^He.*?Demo$'
# result = re.match('.*?(\d+).*?(\d+)',content) # 修饰符 
# print(result)
# print(result.group(1)+result.group(2))

# 使用search()
# findall() 所有的匹配的内容
# sub()去掉需要匹配的字符
# complie()将匹配的规则封装为一个对象可以反复使用匹配的规则
content1 = '2023-12-31 12:00'
content2 = '2024-2-26 16:35'
content3 = '2024-2-26 16:36'

# 将以上具体的时间都去掉，我们只要日期
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)

print(result1,result2,result3)



