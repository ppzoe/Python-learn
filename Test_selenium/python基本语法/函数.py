#函数的参数
"""
def add(a,b):
c = a+b
print (c)
add(1,2)
"""
"""
def add(a = 1,b = 2):
c = a+b
print (c)
add()
add(2,3)
add()
"""
#函数的返回值
"""
def add(a=1,b=2):
    c=a+b
    return a,b,c
print(add())
x,y,z= add()
print(x,y,z)
"""
#函数的嵌套
"""
def a1(a ,b):
    return a+b
def a2(c):
    return c
def calculate (x,y,z):
    result = a1(x,y)-a2(z)
    return result
print (calculate (1,2,3))
"""
"""
def calculate (x,y,z):
    def a1(a ,b):
        return a+b
    def a2(c):
        return c
    result = a1(x,y)-a2(z)
    return result
print (calculate (1,2,3))
"""
"""
def a1(a ,b):
    c = a+b
    def a2(x):
        x = x*x
        return x
    return a2(c)
print (a1(1,2))
"""