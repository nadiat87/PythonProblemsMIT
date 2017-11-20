# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:42:44 2017

@author: Nadia
"""
#==============================================================================
# ##################################
# ######     ASSIGNMENT 0     ######
# ##################################
#==============================================================================
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.
#
# An example of an interaction with your program is shown below:
# Enter number x: 2
# Enter number y: 3
# X**y = 8
# log(x) = 1
#==============================================================================


#""" 
#input: a,b real numbers. a must be > 0
#returns: a^b and log2(a) 
#"""
import numpy    

try:
    a = float(input("Tell me one number: "))
    b = float(input("Tell me another number: "))
    print('x**y = ',round(a**b,2))
#    assert a > 0, 'warning: first number must be greater than zero!'
    print('log2(x) = ',round(numpy.log2(a),2))
except:
    print("Could not perform operations")
        
        