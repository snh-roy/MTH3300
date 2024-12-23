#******************************************************************************
# newton.py
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

# FIRST, WRITE CODE TO GET INPUT FOR THE COEFFICIENTS BELOW, starting with x^0 
# see the pdf specifications for the exact input prompts and formatting
x0 = float(input("Enter x^0 coefficient: "))
x1 = float(input("Enter x^1 coefficient: "))
x2 = float(input("Enter x^2 coefficient: "))
x3 = float(input("Enter x^3 coefficient: "))
x4 = float(input("Enter x^4 coefficient: "))
x5 = float(input("Enter x^5 coefficient: "))

#******************************************************************************
guess = float(input('Enter guess: ')) # the initial guess for Newton's method
    
# the number of iterations for Newton'n method
n_iterations = int(input('Enter number of iterations of Newton\'s method: '))
#******************************************************************************

# INSERT CODE FOR NEWTON'S METHOD BELOW

coefficient = [x0, x1, x2, x3, x4, x5]                                                              #handled in a list for one-call management 

def f(coefficient:list, x:float)-> float:                                                           #This will take the coefficients in the list and set up the polynomial to the power of its index. i.e. if x1 = 2, then 2 * x**1 = 2x. This is the f(x)
    fx= 0 
    for i in range(len(coefficient)):                       
        fx+= coefficient[i] * (x ** i)                                                              #computes f(x)
    return fx

def f_prime(coefficient:list, x:float) -> float:                                                    #This sets up the f'(x) polynomial       
    fx_prime = 0
    for i in range(1, len(coefficient)):    
        fx_prime += coefficient[i] * i * (x**(i-1))                                                 #computes f'(x), definition of d/dx + range starts from 1 to avoid negative power when i = 0
    return  fx_prime
    
xn = guess                                                                                          #assign the input of guess to xn as per guideline
for i in range(n_iterations):   
    fx = f(coefficient,xn)                                                                          #computed f(x) with the current guess value
    fx_prime = f_prime(coefficient,xn)                                                              #computed f'(x) with the current guess value
    xn = xn - (fx/ fx_prime)                                                                        #definition of Newton's Method + and final computation of all inputs

print(xn)
