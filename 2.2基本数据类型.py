a = 100 #整型
print(type(a))
b = True
print(type(b))

c = 1.1
print(type(c))

d = 'wf'
print(type(d))

e = 1+2j
print(type(e))
#数据类型转换
ac = a + c
print("ab的数据类型",type(ac))
ac = a + int(c)
print("ab的数据类型",type(ac))