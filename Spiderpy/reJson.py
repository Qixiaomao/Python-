# 保存为json方式
import json

# loads()将str类型转换为json对象
json_str = '''
[{
        "name":"Bob",
        "gender":"male",
        "birthday":"1992-10-18"
    },
    {
        "name":"Selina",
        "gender":"female",
        "birthday":"1995-10-18"
    }]
'''
json_data = [{'name': 'Bob', 'gender': 'male', 'birthday': '1992-10-18'}, 
 {'name': 'Selina', 'gender': 'female', 'birthday': '1995-10-18'}]

# print(type(json_str))
# data = json.loads(json_str)
# print(data)
# print(type(data))
# print(data[0].get('name'))
with open('data_json.json','w') as file:
    file.write(json.dumps(json_data))
    print("Write successful!\n")