#******************************************************************************
# trapezoid.py
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


#DEFINE YOUR FUNCTION f HERE:
from math import sin, sqrt
def f(x):
    return sqrt(1+sin(x)**2)                                                                                    #Defining f(x) for this equation we are solving
    
#TEST CODE FOR THE FUNCTION f: (uncomment to test, comment out before submitting to Gradescope)
# print(f(0.2), '(this should equal 1.0195437719875284 if your function works)')
# print(f(-1.4), '(this should equal 1.4039626670016296 if your function works)')


#CODE FOR GETTING THE INPUT:
A = float(input('Enter A: '))                                                                                    #Lower bound of integral 
B = float(input('Enter B: '))                                                                                    #Upper bound of integral
N = int(input('Enter N: '))                                                                                      #'number of horizontal bar under the graph for precision' aka how many slices we are taking to find the area

################################################
#INSERT CODE FOR COMPUTING APPROXIMATION OF DEFINITE INTEGRAL USING TRAPEZOIDAL RULE BELOW:   
dx = (B-A) / N                                                                                                   #Definition of delta x; to be then substituted to def of trapezoid
first_last_terms = f(A) + f(B)                                                                                  #Since the first and last term of definition has a coefficient of 1. By associative property of addition, it doesn't matter which order we add, so I might as well add them first.
between = 0                                                                                                      #Count of terms b/w the terms between the first and last terms

for i in range (1, N):                                                                                           #From the first term to N (exclusive), the for loop should compute first term then by definition of trapezoid rule, adds and multiplies middle terms form (x2...xn-1) by 2 
    x = A + i * dx
    between += 2 * f(x)

integral = dx/2 * (first_last_terms + between)                                                                   #Final computation and definition of integral of f(x) using the trapezoid rule


################################################

#CODE FOR PRINTING THE APPROXIMATION TO 8 DECIMAL PLACES
# integral is the variable for the approximation 
print(f'{integral:.8f}')                                                                                         #Print the result up to 8 decimals