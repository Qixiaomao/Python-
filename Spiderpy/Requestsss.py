import requests

urls = 'http://httpbin.org/get'

data = {
    'name':'germey',
    'age':22
}

r = requests.get(url=urls,params=data)
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))