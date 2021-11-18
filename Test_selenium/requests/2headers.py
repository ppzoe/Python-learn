import requests
test_url="http:www.163.com"
h={"User-Agent":"Android/H60-L01/4.4.2/"}
response = requests.get(test_url,headers=h)

# import requests
# test_url = "http://www.163.com"
# h = {"User-Agent":"Android/H60-L01/4.4.2/"}
# response = requests.get(test_url,headers = h)
# print (response.status_code）
# print (response.headers）
# print (response.text) 