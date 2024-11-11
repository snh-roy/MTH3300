#******************************************************************************
# binary.py
#******************************************************************************
# Name: Sneha Roy
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import random

# The two lines below set the random seed for testing on Gradescope. Comment out these lines to test your code on Spyder.
#####################
seed = input() # comment out to test on Spyder, but leave for Gradescope submission
random.seed(seed) # comment out to test on Spyder, but leave for Gradescope submission
#####################

# YOUR CODE SHOULD START BELOW. THE LINES ABOVE NEED TO BE BEFORE YOUR CODE! #

eight_digit =int(input("Enter 8's digit: "))                            #Input of either 1 or 0
if eight_digit !=0 and eight_digit !=1: 
    eight_digit =int(input("Enter 8's digit: "))

four_digit = int(input("Enter 4's digit: "))                            #Input of either 1 or 0
if four_digit !=0 and four_digit !=1: 
    four_digit = int(input("Enter 4's digit: "))      

two_digit = int(input("Enter 2's digit: "))                              #Input of either 1 or 0
if two_digit !=0 and two_digit !=1: 
    two_digit = int(input("Enter 2's digit: "))                                                                 

one_digit = int(input("Enter 1's digit: "))                              #Input of either 1 or 0
if one_digit !=0 and one_digit !=1: 
    one_digit =int(input("Enter 1's digit: "))                                                                      

num = eight_digit * 8 + four_digit * 4 +two_digit * 2 + one_digit * 1                              #computes decimal equivalent of the binary                     
print (f"The binary number {eight_digit}{four_digit}{two_digit}{one_digit} is {num} in base ten")  #prints the input and decimal translation

x = random.randrange(0,16)                                                 #generates a random number from 0 to 15 (16 is exclusive) & assigns to random_number for comparison later

if num < x:                                                                #compares the random number with the decimal translation of the binary
    dec_vs_rand = True 
else: 
    dec_vs_rand = False

print (f"Less than the randomly generated number {x}? {dec_vs_rand}")      #prints output