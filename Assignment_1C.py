# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:30:51 2017

@author: Nai
"""
#==============================================================================
# ##################################
# ######     ASSIGNMENT 1     ######
# ##################################
#==============================================================================
# Part C: Finding the right amount to save away 
#==============================================================================
# In Part B, you had a chance to explore how both the percentage of your salary
# that you save each month and your annual raise affect how long it takes you 
# to save for a down payment. This is nice, but suppose you want to set a
# particular goal, e.g. to be able to afford the down payment in three years.
# How much should you save each month to achieve this? In this problem, you are
# going to write a program to answer that question. To simplify things, assume:
# 
#   1.Your semiannual raise is .07 (7%)
#   2.Your investments have an annual return of 0.04 (4%)
#   3.The down payment is 0.25 (25%) of the cost of the house
#   4.The cost of the house that you are saving for is $1M.
# 
# You are now going to try to find the best rate of savings to achieve a down
# payment on a $1M house in 36 months. Since hitting this exactly is a 
# challenge, we simply want your savings to be within $100 of the required
# down payment.
# 
# In ps1c.py , write a program to calculate the best savings rate, as a 
# function of your starting salary.You should use bisection search to help you 
# do this efficiently. You should keep track of the number of steps it takes
# your bisections search to finish. You should be able to reuse some of the
# code you wrote for part B in this problem.
#         
#    Please make your program print results in the format shown in 
#     the test cases below. 
#     
#   Test Case 1 
#     >>> 
#     Enter the starting salary: 150000
#     Best savings rate: 0.4411
#     Steps in bisection search: 12
#     >>> 
#
#   Test Case 2 
#     >>> 
#     Enter the starting salary: 300000
#     Best savings rate: 0.2206
#     Steps in bisection search: 9
#     >>>
#
#   Test Case 3 
#     >>> 
#     Enter the starting salary: 10000 
#     It is not possible to pay the down payment in three years.
#     >>>
#==============================================================================

# Input variables
annual_salary = float(input(' Enter the starting salary: '))

# Initial parameters
r = 0.04 # investments annual rate
semi_annual_raise = 0.07
tol = 100
max_months = 36
total_cost = 1000000
portion_down_payment = 0.25* total_cost # downpayment required for house
current_savings = 0 # initial savings

# function to calculate savings at the end of the max period
def calc_savings(s,annual_salary,r,semi_annual_raise):
    current_savings = 0 # initial savings
    for months in range(max_months):
        current_savings += (current_savings*r/12 + (s/100/100)*annual_salary/12)
        months += 1
        if (months%6 == 0):
            annual_salary *= (1+semi_annual_raise)
    return current_savings

# initial parameters for bisection search
low = 0
high = 10000
num_guesses = 0
guess = int((low + high)/2.0) 

# Calculate savings to reach downpayment in 36 months
while abs(current_savings - portion_down_payment) >= tol and guess<10000:
    current_savings = calc_savings(guess,annual_salary,r,semi_annual_raise)
    tmp = guess    
    if current_savings > portion_down_payment:
        high = guess
    else:
        low = guess
    guess = int((low + high)/2.0)
    num_guesses += 1
    if abs(guess-tmp)<1:
        break
#    print('current savings',current_savings,'guess',guess/10000)
if abs(current_savings - portion_down_payment) < tol:
    print(' Best savings rate: ', float(round(guess/10000,5)))
    print(' Steps in bisection search: ', num_guesses)
else:
    print(' It is not possible to pay the down payment in three years.')
    
#for months in range(max_months):
#    current_savings += (current_savings*r/12 + (guess/100/100)*annual_salary/12)
#    months += 1
#    if (months%6 == 0):
#        annual_salary *= (1+semi_annual_raise)
#    print('current savings',current_savings,'guess',guess/10000)