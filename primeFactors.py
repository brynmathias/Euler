#!/usr/bin/env python
# encoding: utf-8
"""
primeFactors.py

Created by Bryn Mathias on 2011-09-09.
Copyright (c) 2011 Imperial College. All rights reserved.



The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?


"""

import sys
import os
import math
def isPrime(number):
  """Check if a number is prime -- bruit force and not very nice!!"""
  if number is 2: return True
  if number < 2: return False
  if number % 2 is 0: return False
  for i in range(3,int(math.sqrt(number))+1):
    if number % i == 0:
      return False
  # print "%d is Prime"%(number)
  return True




def main(num):
  """Return the prime factors of an input number"""
  outList = []
  Primes = []
  for i in range(0,int(math.sqrt(num)+1)):
    val = int(math.sqrt(num)+1) - i
    if isPrime(val):
      if num % val is 0:
        print "found one factor %d"%(val)
        return True
  pass






if __name__ == '__main__':
  main(600851475143)

