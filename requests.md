# requests库

* GET : r = requests.get('https://api.github.com/events')
* POST : r = requests.post('https://httpbin.org/post', data = {'key':'value'})
* delete : r = requests.delete('https://httpbin.org/delete')
* head : r = requests.head('https://httpbin.org/get')
* options : r = requests.options('https://httpbin.org/get')
* PUT: r = requests.put('https://httpbin.org/put', data = {'key':'value'})


## 携带参数

```python:

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)

```

## 模拟浏览器

```python

>>> url = 'https://api.github.com/some/endpoint'

>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

## 获取文本内容

```python

import requests

req = requests.get("http://www.baidu.com")


r = req.text
print(r.encode('utf-8'))

```

## 获取字节响应内容

```python

>>> r.content

b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

## 获取响应码

```python
>>> r = requests.get('https://httpbin.org/get')

>>> r.status_code

200
```

## 获取响应头

```python
>>> r.headers
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Fri, 07 Apr 2023 08:35:11 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:28:12 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
```

## 获取响应Json
```python
>>> r = requests.get('https://api.github.com/events')

>>> r.json()

[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

## 获取socket流内容

```python
>>> r = requests.get('https://api.github.com/events', stream=True)

>>> r.raw

<urllib3.response.HTTPResponse object at 0x101194810>

>>> r.raw.read(10)

'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

## 上传文件

```python
>>> url = 'https://httpbin.org/post'

>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)

>>> r.text

{  ...  "files": {    "file": "<censored...binary...data>"  },  ...}v

```

## 请求的时候用 json 作为参数
```python
>>> url = 'https://api.github.com/some/endpoint'

>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)

```

##  Post请求 当你想要一个键里面添加多个值的时候

```python
>>> payload_tuples = [('key1', 'value1'), ('key1', 'value2')]

>>> r1 = requests.post('https://httpbin.org/post', data=payload_tuples)

>>> payload_dict = {'key1': ['value1', 'value2']}

>>> r2 = requests.post('https://httpbin.org/post', data=payload_dict)

>>> print(r1.text)

{  ...  "form": {    "key1": [      "value1",      "value2"    ]  },  ...}

>>> r1.text == r2.text

True
```

## 获取cookies

```python
>>> url = 'http://example.com/some/cookie/setting/url'

>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']

'example_cookie_value'

```

## 设置超时

```python
>>> requests.get('https://github.com/', timeout=0.001)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```

## 发送cookies

```python
>>> url = 'https://httpbin.org/cookies'

>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)

>>> r.text

'{"cookies": {"cookies_are": "working"}}'

```
