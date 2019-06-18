def two():
    print()
import urllib.request
import urllib.parse
data = bytes(urllib.parse.urlencode({'pw':'2019','un':'2020'}),enconding='utf8')
print(data)
url='http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)