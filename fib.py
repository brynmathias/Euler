#!/usr/bin/env python
# encoding: utf-8
"""
fib.py

Created by Bryn Mathias on 2011-09-09.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

a = 1
b = 2
x = 0
z = 0
for x in range(0,100000):
  if a + b < 4000000:
    print a+b
    if (a+b)%2 == 0:
      z += a+b
    if a < b:
      a = a + b
    else:
      b = b + a

print "Sum of all equal fibonanchi numbers below 4000000 is", z+2