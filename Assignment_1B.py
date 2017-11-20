# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:07:54 2017

@author: Nai
"""
#==============================================================================
# ##################################
# ######     ASSIGNMENT 1     ######
# ##################################
#==============================================================================
# Part B: Saving, with a raise 
#==============================================================================
# In Part A, we unrealistically assumed that your salary didn’t change.
# But you are an MIT graduate, and clearly you are going to be worth more
# to your company over time! So we are going to build on your
# solution to Part A by factoring in a raise every six months.
# 
# In Part B, copy your solution to Part A. 
# Modify your program to include the following:
# 
#   1.Have the user input a semi-annual salary raise semi_annual_raise 
#     (as a decimal percentage)
#   2.After the 6 th month, increase your salary by that percentage. 
#     Do the same after the 12th month, the 18 month, and so on.
# 
# Write a program to calculate how many months it will take you save up
# enough money for a down payment. LIke before, assume that your
# investments earn a return of r = 0.04 (or 4%) and the required down payment
# percentage is 0.25 (or 25%). 
# Have the user enter the following variables:
#       1.The starting annual salary (annual_salary) 
#       2.The portion of salary to be saved (portion_saved) 
#       3.The cost of your dream home (total_cost)
#       4.The semiannual salary raise (semi_annual_raise)
#         
#     Please make your program print results in the format shown in 
#     the test cases below. 
#     
#   Test Case 1 
#     >>> 
#     Enter your annual salary: 120000 
#     Enter the percent of your salary to save, as a decimal: .05 
#     Enter the cost of your dream home: 500000 
#     Enter the semiannual raise, as a decimal: .03
#     Number of months: 142 
#     >>> 
#
#   Test Case 2 
#     >>> 
#     Enter your annual salary: 80000 
#     Enter the percent of your salary to save, as a decimal: .1 
#     Enter the cost of your dream home: 800000 
#     Enter the semiannual raise, as a decimal: .03
#     Number of months: 159 
#     >>>
#
#   Test Case 3 
#     >>> 
#     Enter your annual salary: 75000 
#     Enter the percent of your salary to save, as a decimal: .05 
#     Enter the cost of your dream home: 1500000 
#     Enter the semiannual raise, as a decimal: .05
#     Number of months: 261 
#     >>>
#==============================================================================

# Input variables
annual_salary = float(input(' Enter your starting annual salary: '))
portion_saved = float(input(' Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input(' Enter the cost of your dream home: '))
semi_annual_raise = float(input(' Enter the semiannual raise, as a decimal: '))

# Initial calculations
r = 0.04 # investments annual rate
portion_down_payment = 0.25* total_cost # downpayment required for house
current_savings = 0 # initial savings
months = 0

# Calculate how many months of savings are needed for downpayment
while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12 + portion_saved*annual_salary/12)
    months += 1
    if (months%6 == 0):
        annual_salary *= (1+semi_annual_raise)
print('Number of months: ',months)
