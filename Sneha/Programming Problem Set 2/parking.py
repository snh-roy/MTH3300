#******************************************************************************
# parking.py
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
car1 = int(input("Car 1 preferred spot: "))                         #input of either 1,2, or 3 
car2 = int(input("Car 2 preferred spot: "))

spot = car1                                                         #car 1 will have the privilege to park first anywhere
print(f"Car 1 parks in spot {car1}")

if car2 < spot:                                                     #if car 2 value is less than car 1, then it gets to car on a avilable spot it prefers
    print(f"Car 2 parks in spot {car2}")

elif car2 > spot:                                                   #if car 2 value is greater than car 1, then it gets to car on a avilable spot it prefers
    print(f"Car 2 parks in spot {car2}") 

elif car2 == car1:                                                  #if car 2 prefers the same spot as car 1, 
    if car1 < 3:                                                    
        print(f"Car 2 parks in spot {car1 + 1}")                    #then car 2 can park in the next available spot
    else:                                                           #if car 1 parks in spot 3, then car 2 cannot park since there are no more spots
        print("Car 2 cannot park")