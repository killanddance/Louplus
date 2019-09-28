#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera=int(input("input number of camera:"))
price = int(input("input price of the camera:"))
bonus = bonus_rate * numberofcamera
commission=price * commission_rate * numberofcamera
print("Bonus={:d}".format(bonus))
print("commission={:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bonus +commission))
