# monte_carlo.py
# CS 220 Lab 1 - Monte Carlo
# Lauren Dickman
# Thursday, October 31, 2019

import sys
import random
import math

### 
# function:  print_intro 
# purpose:   prints a message to the user, introducing the program
### 
def print_intro():
    print("Welcome to the amazing pi estimator! I'm going to use a Monte Carlo simulation to estimate pi.") 
    print("By throwing random darts at a dartboard, I can determine pi pretty accurately!")

### 
# function:  get_num_darts 
# return:    number of darts to throw (an int) for the simulation  
### 
def get_num_darts():
	num_darts = int(input("Please enter a positive integer (number of darts/trials): " ))
	return num_darts

### 
# function:    is_positive
# parameter:   num_darts, an integer
# return:      True if num_darts is positive; otherwise, False
# side effect: if num_darts is not positive, print an error message to the user
###
def is_positive(num_darts):
    if num_darts > 0:
        return True
    else:
        print("Oops, you need to enter a positive number.")
        return False

### 
# function:  throw_darts
# parameter: num_darts, the number of darts to throw
# return:    a list of tuples representing the random darts (length is 
#               num_darts)
###
def throw_darts(num_darts):
    L = []
    for count in range(num_darts):
        throws = get_random_tuple(-1, 1)
        L.append(throws)
    return L

###
# function:   get_random_tuple
# parameters: a and b are floats with a < b
# return:     a random tuple of the form (x, y) where a <= x <= b and 
#                a <= y <= b
###
def get_random_tuple(a, b): 
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    return (x,y)

###
# function:   get_ratio
# parameters: L, a list of tuples (x, y) representing darts
# return:     a float number, the ratio:
#                r = (number of darts inside circle) / (number of darts thrown)
###
def get_ratio(L):
    num = len(L)
    r = (count_hits(L) / num)
    return r
###
# function:   count_hits
# parameters: L, a list of tuples (x, y) representing darts
# return:     an int, the number of darts in L which fall inside the circle
# note:       (x, y) is inside the circle whenever the distance from (x, y) 
#                to (0, 0) is less than 1
###
def count_hits(L):
    acc = 0
    for i in L:
        ans = math.sqrt((i[0]-0)**2 + (i[1]-0)**2)
        if ans < 1:
            acc = acc + 1
    return acc
    
###
# function:   get_percent_error
# parameter:  estimate, a float
# parameter:  correct, a float
# return:     the percent error (positive or negative float number) in using 
#                `estimate` as an estimate for `correct`.
# example:    get_percent_error(9.999, 10) is -0.1 (9.999 is 1/10 of a percent 
#                less than 10)
###
def get_percent_error(estimate, correct):
    ans = (estimate - correct)/correct*100
    return ans

### 
# function:   print_report 
# parameter:  n, a positive integer, the number of trials 
# parameter:  est, estimate for pi from the simulation (a float) 
# prints:     number of trials, the estimate for pi, and the percent error 
#                of that estimate, rounded to the nearest hundredth      
###
def print_report(num_darts, estimate, percent):
    print("Number of Trials:", num_darts)
    print("math.pi:", math.pi)
    print("Estimate for pi:", estimate)
    print("Percent error:", round(percent, 2),'%', sep='')
   
###
# function:   main
# purpose:    runs the simulation by calling helper functions
# note:       if the user enters a non-positive number of darts, calls 
#                sys.exit() to end the program
###
def main(): 
	print_intro()
	num_darts = get_num_darts()
	positive = is_positive(num_darts)
	if positive == True:
		throw = throw_darts(num_darts)
		estimate = (get_ratio(throw)*4)
		correct = math.pi
		percent = get_percent_error(estimate, correct)
		print("****RESULTS****")
		print_report(num_darts, estimate, percent)

main()