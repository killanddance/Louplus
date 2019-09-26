#!/usr/bin/env python3
amount = float(input("Enter amount:"))  #输入数额
inrate = float(input("Enter Interest rate:")) #输入利率
period = int(input("Enter period:")) #输入期限
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("year {} Rs. {:.5f}".format(year,value))
    amount = value
    year = year +1



