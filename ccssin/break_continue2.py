a=0
while a<=10:
    a=a+1
    if a ==5:
      continue
    print(a)

#continue 和break 后面都没有符号，不知道为啥，可能是跳出和阻挡特殊把，，不知道以后会不会有
#这里continue的意思是 如果a==5（a和5相等时）不执行a=5，跳过去执行后面的，而前一个应用，break的意思就是直接执行到5的时候，跳出，输出，不执行后面的东西