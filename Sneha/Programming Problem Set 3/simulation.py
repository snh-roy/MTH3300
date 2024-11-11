#******************************************************************************
# simulation.py
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

num_of_plays = 10 ** 6                                                                                #1 million simulations

earnings_over_all_plays = 0                                                                           #Initialize total earnings across all games to 0
num_successes = 0                                                                                     #Initialize counter for number of winnings to 0
x = int(input()) # in one play, to keep the amount earned, we must get > x dollars
##################### DO NOT MODIFY ANY CODE ABOVE #######################################
##################### YOUR CODE SHOULD BE BELOW THIS LINE ################################

for _ in range(num_of_plays):                                                                           #Loop through the game 1 million, _ is used as we don't know what th of 1M we are in    
    game_total = 0                                                                                      #Current game set to 0 

    for _ in range(4):                          #Loop through 4 dice rolls per game  
        num_of_roll = random.randint(1,6)       #Random dice roll between 1 and 6

        if num_of_roll <= 3:          #If roll is 1, 2 or 3, add $1 to the current game
            game_total += 1
        elif num_of_roll == 4:        #If roll is 4, add $5 to the current game
            game_total += 5
        elif num_of_roll == 5:        #If roll is 5, add $10 to the current game
            game_total += 10
        elif num_of_roll == 6:        #If roll is 6, add $50 to the current game
            game_total += 50
        
    if game_total > x:                #If current game earnings exceed target value, increment win counter
        num_successes += 1
        earnings_over_all_plays += game_total        #Add current game earnings to total earnings if above is true
    else:    
        earnings_over_all_plays -= 100               #Subtract $100 as a penelty for  inputing a value greater than the game total


##################### YOUR CODE SHOULD BE ABOVE THIS LINE ################################
##################### DO NOT MODIFY ANY CODE BELOW #######################################
print(f'{num_successes/num_of_plays:.1f}') # estimate of the probability of winning > x in a play of the game
print(f'{earnings_over_all_plays/num_of_plays:.0f}') # estimate of the expected value of the amount won in a single play