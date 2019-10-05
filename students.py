#!/usr/bin/env python3
n = int(input("ENter the number of students:"))
data = {} #用来存储数据的字典变量
Subjects = ('physics','maths','history') #所有科目
for i in range(0,n):
    name = input('enter the name of the student:{}'.format(i+1))#获得学生名称

    marks = []
    for x in Subjects:
        marks.append(int(input('enter marks of{}:'.format(x)))) #获得每一科的分数
    data[name] = marks
    print("marks is {}.........{}".format(marks,type(marks)))
    print("data=={}......{}".format(data,type(data)))
for x,y in data.items():
    print("x======&*^*^&*^=====",x)
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed!!")
    else:
        print(x,"passed!!!")
