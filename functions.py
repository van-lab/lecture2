# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:55:51 2020

@author: home990
"""

def square(x):
  return x*x
def main():
  for i in range(10):
    print("{} square is {}".format(i, square(i)))

if __name__ == "__main__":
  main()
  
