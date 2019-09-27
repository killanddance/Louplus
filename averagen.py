#!/usr/bin/env python3
N=10
sum=0
count=0
print("please input ten number:")
while count < N:
    number = float(input())
    sum = sum + number
    count+=1
    print("current Number is{}".format(count))
print ("the sum of numberI is{}.".format(sum))
print("the averagen is {:.5f}".format(sum/10))

