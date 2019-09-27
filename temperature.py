#!/usr/bin/env python3
fahrenheit= 0
print("input the temperature for transf")
fahrenheit=int(input())
celsius = (fahrenheit - 32) / 1.8
print("fahrenheit{:3d}  {:7.2f}celsius".format(fahrenheit,celsius))
#括号里的3d表示3三位宽度的整数，7.2代表一共七位（包括小数点两位小数，宽度不够用空格代替）
