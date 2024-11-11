#******************************************************************************
# population.py
#******************************************************************************
# Name: Sneha Roy
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): 9.2.7. Constants https://python.readthedocs.io/en/latest/library/math.html#constants
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#


from math import e                                                              #need Euler's number for Pert, hence needed to import math module

p1 = float(input("Enter the initial population: "))                             #Inputs for the initial Pert + final pert in float values b/c the inputs are numbers
t1 = float(input("Enter the first time period in years: "))
r1 = float(input("Enter the first growth rate as a percentage: "))
t2 = float(input("Enter the second time period in years: "))
r2 = float(input("Enter the second growth rate as a percentage: "))

r1_decimal = r1 / 100                                                            #converting to decimal since input is in %form 
r2_decimal = r2 / 100                                                            #converting to decimal since input is in %form 

total_time = t1 + t2                                                          

p1_population = p1 * e**(r1_decimal*t1)                                          #calculation for Pert at initial population
p2_population = p1_population * e**(r2_decimal* t2)                              #calculation for Pert as initial population compounds to final population

growth_rate_percentage = ((p2_population - p1)/p1) * 100                         #calculation for % of growth from intial population to final population                

print(f"The ending population is {p2_population:.6f}")                                                       #prints the output
print(f"The overall growth in the {total_time} year period is {growth_rate_percentage:.3f} percent")         #prints the output