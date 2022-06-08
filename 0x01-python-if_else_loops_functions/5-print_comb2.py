#!/usr/bin/python3
# Author - Hassan Nurudeen
"""print numbers from 0 to 99, it should all be in two digits"""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
