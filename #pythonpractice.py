# Python练习
a = 100
a = 101
b = a

print(b)

import math   # 输出将是 100

def sin(x):
    x = float(x)
    n = 1
    num_n = pow(-1, n + 1) * (x ** (2 * n - 1)) / math.factorial(2 * n - 1)
    for n in range(1, 50):
        num_n += pow(-1, n + 1) * (x ** (2 * n - 1)) / math.factorial(2 * n - 1)
        while num_n < 0.00001:
            break
        print(n)
    return num_n


x = float(input("请输入一个角度值（单位：弧度）："))
print("结果为：", sin(x))


x = int(input("请输入一个整数："))
if x == 2:
    print("it is")  
while x % 2 == 0 and x > 2:
    print("not")


i = pow(x, 0.5)
for n in range(2, int(i) + 1):
    if x % n == 0:
        print("it is not")
    else:print("it is")