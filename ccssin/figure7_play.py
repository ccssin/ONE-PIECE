#逢7就跳过Python 开发环境
#int 类型   #变量   #运算符  #while循环  #条件判断   #a=int('7,14,21,28,35,42,49,56,63,70,77,84,91,98')#if a ==int: 这里的int没用上，不知道怎么用
a=0
while a<100:
    a+=1
    if a % 7 == 0 or a % 10 == 7 or a//10 == 7 :
        continue
    else:
        print(a)


