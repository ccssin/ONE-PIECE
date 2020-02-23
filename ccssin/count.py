#for循环结构  for+元素+in+集合
for a in range(10):
    print(a)
        #这里的a不能带引号，否则会出现10个a
    #这道题的主要目的是为了生成一个从 0 到 x-1 的整数序列，比如我们打印 0 到 9 的数


    #还可以用 range(a,b) 取某个区间的数，比如要打印 1 到 10 ,你可以写：
for a in range(1,11):
        print(a)
        # 注意： range(a,b) 包头不包尾，尾数要 + 1 。