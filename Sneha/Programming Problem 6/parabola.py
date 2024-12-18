#******************************************************************************
# parabola.py
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

class Parabola:

    def __init__(self, h, k, a):     #Atributes
        self._xvert = h              #some float value h representing x vetex
        self._yvert = k              #some float value k representing y vetex
        self._leadingcoef = a        #some float value a representing the leading coefficient
    
    def yintercept(self):            
        y_intercept = self._leadingcoef * ((0-self._xvert)**2)+self._yvert   #vertex formula to find the vertex where x is 0
        return y_intercept
    
    def display(self):                #displays the values of the leading coefficient, x-vertex, y-vertex
        print(self._xvert, self._yvert, self._leadingcoef)

    def isConcaveDown(self):           #determines if the function is concaving down only if the the leading coefficient is negative
        if self._leadingcoef < 0:
            return True
        else:
            return False


################################################################################
# PUT YOUR CLASS DEFINITION ABOVE!
################################################################################

def main():
    my_parabolas = []
    while True:
        myinput = input()
        if myinput == 'x':
            break
        inputlist = myinput.split()
        p = Parabola(float(inputlist[0]), float(inputlist[1]), float(inputlist[2]))
        my_parabolas.append(p)

    ####################################################
    # Write code which displays info for the parabolas in
    # my_parabolas that are concave down, also printing
    # the y-intercept for each.
    ####################################################

    for i in my_parabolas:            #once the info is stored in the listm loop through it
        if i.isConcaveDown():         #calls the function to check if it concaves down, aka a is negative
            i.display()               #displays the leading coefficient and the x and y vertices
            print(i.yintercept())     #prints the y-intercept



main()    


