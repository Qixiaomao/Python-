import urllib.parse
import urllib.request

def data():
    datas = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
    repo = urllib.request.urlopen('http://httpbin.org/post',data=datas)
    print(repo.read())
    

if __name__ == '__main__':
    data()