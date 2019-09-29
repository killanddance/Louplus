#!/usr/bin/env python3
a,b=0,1
while b<100:
    print(b,end=" ")  #用end参数 替换PRINT默认的换行符
    a,b=b,b+a
print()   #打印一个默认的换行符


