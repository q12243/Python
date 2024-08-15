#算数运算符
a = 2
b = 5
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b,type(a / b))#数据类型的转换
print('a ** b =', a ** b)
print('a // b =', a // b)
print('a % b =', a % b)  # 2/5 = 0 ......2

#  比较运算符
print('a > b  =', a > b)
print('a < b  =', a < b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)
print('a == b =', a == b)
print('a != b =', a != b)
#数据类型不一样，数值一样也成立，列如 2 == 2.0
#浮点数有效位数有限如果a=2.0000000000000000001 b=2，这两者在存储范围内相等，实际不相等，浮点数最多能存6位小数


# 赋值运算符
a = 1
a = a + 1
print(a)
a += 1  # a = a + 1等效
print(a)
a -= 1  # a = a - 1等效
print(a)
a *= 2  # a = a * 2等效
print(a)
a /= 3  # a = a / 3等效
print(a)

# 逻辑运算符 acd or not
a = 1
b = 2
print(a==1 and b == 2)
print(a==1 or b==2)
print(not b==2)
#True  1     Flase 0
print(1 and 0)
print(1 or 0)
print(not 0)

#成员运算符 in   not in
string = "hello alice"
char = "e"   #o a也可以，子字符串出现也算
print(char in string)

