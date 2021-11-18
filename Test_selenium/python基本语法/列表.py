a = [1,2,"d",(1,"dd")]
a.append("x")
print (a)
a.insert(2,"c")
print (a)
a.remove("d")
print (a)
a[-2] = 3
print (a)
c = [1,2,"d",(1,"dd")]
d = [4,["a",3],"ddd"]
a.extend(d)
print (c)
d = d + c
print (d)