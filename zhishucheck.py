#质数检查
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