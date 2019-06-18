def one():
    print()
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'嘿嘿'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)