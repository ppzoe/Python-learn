# r=requests.方法(url.headers,data,...)
# r.headers     获取返回的头信息
# r.text        获取返回的主体
# r.cookies     获取返回的cookie
# r.status_code 获取返回的状态码
import requests
test_url="http://www.163.com"

response=requests.get(test_url)
print (response.status_code)
print (response.headers)
print (response.text)