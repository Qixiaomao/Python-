# 编写方案解决json中文得问题
import json

json_data = [{
    "name":"王伟",
    "gender":"男",
    "birthday":"1992-10-18"
}]

with open('data.json','w',encoding='utf-8') as file:
    file.write(json.dumps(json_data,indent=2,ensure_ascii=False))
    print("Write Successful!\n")