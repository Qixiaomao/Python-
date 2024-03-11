import urllib.request
import urllib.parse

repo = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(repo.read())