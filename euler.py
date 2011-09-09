#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Bryn Mathias on 2011-01-03.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
y = 0
for x in range(0,1001):
  if x > 999: continue
  print x
  if x%3 == 0 or x%5 == 0:
    y += x
    print y
print y


#question 2
