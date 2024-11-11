#******************************************************************************
# quadratic.py
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

# math is imported and the code to get the three coefficents is provided to start off
import math

# Prompt the user for coefficients a, b, and c
a = float(input("Enter x^2 coefficient: "))
b = float(input("Enter x^1 coefficient: "))
c = float(input("Enter x^0 coefficient: "))

if a == 0:                                                                           #quadratic formulas are always non-zero coeficient for x^2 values
    print("The equation is not quadratic")

else:
    discriminant = b**2 - 4*a*c                                                      #discriminant formula: b^2 - 4ac

    if discriminant > 0:                                                              #when discriminant is positive, there are two distinct real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)                                     #+ sqrt
        x2 = (-b - math.sqrt(discriminant)) / (2*a)                                     #- sqrt

        if x1 < x2:                                                                  #smalller solution displayed first 
            print(f"TWO REAL SOLUTIONS: x = {x1:.4f} and x = {x2:.4f}")
        else: 
            print(f"TWO REAL SOLUTIONS: x = {x2:.4f} and x = {x1:.4f}")

    elif discriminant == 0:                                                          #if the discriminant is 0, then there's only one solution
        x = -b / (2*a)                                                               #x-coordinate of the vertex of a quadratic equation
        print(f"ONE SOLUTION: x = {x:.4f}")                                             

    else:                                                                              #when discriminant is negative, solutions will be imaginary
        real_num = -b / (2*a)
        imaginary = math.sqrt(-discriminant) / (2*a)
        print(f"COMPLEX SOLUTIONS: x = {real_num:.4f} - {abs(imaginary):.4f}i and x = {real_num:.4f} + {abs(imaginary):.4f}i")  #prints complex positve solutions upto 4 digits
