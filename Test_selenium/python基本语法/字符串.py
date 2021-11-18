#字符串的转换
"""
a = 1
print (type(a))
b = str(a)
print (type(b))
"""
"""
a = {"dd":1}
print (type(a))
b = str(a)
print (type(b))
print (b)
"""
#字符串的合并
"""
a = 1
a=str(a)
b = "xxx"
c = a+b
print (c)
"""
#字符串的截取
"""
a = "xyz123"
print (a[1])
print (a[2:4])
print (a[-3:-1])
"""
#split（字符/字符串，分割次数）
"""
a = "a=abc,b=123,cddd,(1,2)"
print (a.split(","))
print (type(a.split(",")))
print (a.split(",")[2])

a = "a=abc,b=123,cddd,(1,2)"
print (a.split(",",3))

a="a=abc,b=123,cddd,(1,2)"
print(a.split(",")[0].split("=")[1])
"""
#字符串的替换 replace
"""
a="a=abc,b=123,cddd,(1,2)"
print(a.replace(",","and"))

a="a=abc,b=123,cddd,(1,2)"
print(a.replace(",","and",2))
"""
a = "a=abc,b=123,cddd,(1,2)"
print (a.replace(",","and",2))
print (a)
b = a.replace(",","and",2)
print (b)