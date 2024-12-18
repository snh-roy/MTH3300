def exercise_1():

    def fn(my_num, my_list):
        my_num +=1 
        my_list[0] += 1
        return my_num*2
        return my_num 

    a_number= 10
    a_list =[4,8,2,3]
    x = fn(a_number,a_list)
    print(a_number)
    print(a_list)
    print(x)




def exercise_2():
    """Write code that receives a file name as input from the user. If the file exists, the code should open
the file and print out the first word, then print out
every other word in the file on a single line, separated by single spaces. For example, if the files contents were
hi i am your written homework
use me to study for the final
then, your code should print:
hi am written use to for final
If the file does not exist in the current directly, your code should display an error message to the user saying
the file does not exist and keep asking for a file name until the user enters a valid filename.
"""
    invalidFile = True 
    while invalidFile:
        filename = input(str("Enter a file name:"))
        try:
            file = open(filename, "r")
            invalidFile = False 
        except FileNotFoundError:
            print("file does not exist")
    
    sentences = file.read()
    filelist = sentences.split()
    for i in range (len(filelist)):
        if i % 2 == 0:
            print(filelist[i],end= "")

# x = 1
# def func():
#     global x
#     print(x)
#     x = 2
# func()

def exercise_3():
    """Using loops, declare and set a two-dimensional list
table to have values given by the following table:
2 4 6 8
3 6 9 12
4 8 12 16   """
    table = [[],[],[]]
    for r in range(2, 5):
        for c in range(1,5):
            table[r-2].append(r*c)
    print(table)
        

def exercise_4():
    """numlist = [[5, 1, 2, 4], [1, 3, 1, 0, 6], [8, 1]] 
    Write a function modify_list so that after the function call
modify_list(numlist), each row consists of one entry equal to the average of the entries in that row.
For example, with the given numlist, after calling modify_list(numlist),
numlist should be changed to
[[3.0], [2.2], [4.5]] """
    avg = [[],[], []]
    def modify_list(numlist):
        for row in range(len(numlist)):
            total = 0 
            for num in numlist[row]: 
                total+= num
            average = total / len(numlist[row])
            avg[row].append(average)
    numlist = [[5, 1, 2, 4], [1, 3, 1, 0, 6], [8, 1]]
    modify_list(numlist) #call the function before printing
    print(avg)


def exercise_5():
    def fun(n):
        if n==0:
            return 1 
        return 2 * fun(n-1)

    print(fun(5))

def exercise_6():
    def recur(x:int):
        if x <= 2:
            return 8
        return x +recur(x-2)
    print(recur(5))



def exercise_7():
    """Write a recursive function countEs that takes one string parameter and returns the number of e's in
the string."""
    def countEs(s:str):
        count=0
        if s == "":
            return 0 
        elif s[0] == "e":
            count = 1 
        return count + countEs(s[1:])
    
    s= "sneha eat eggs"
    print(countEs(s))


def exercise_8():
    """Write a recursive function recur that has as its input parameter a single nonnegative integer n
and returns the value 7*n + 3 without using any multiplications"""
    
    def recur(n:int):
        if n == 0:
            return 3   #3, 10, 17, 24
        return 7 +recur(n-1)
    print(recur(3))


def exercise_9():
    def fn(x, y):
        x[1] = 8
        y = 60
        print("!")
        x = [2, 3]
        return y
        print (y, end="")

    y = [0, 0]
    a = 10
    z = fn(y, a)
    print(y[0], y[1], a, z)


def exercise_10():
    peter = [[4, 0, 10, 1], [1, 0, 20, 1], [1, 0, 30, 1]]
    tom=[]
    for i in range(len(peter[0])):  
        total = 0
        for row in peter:
            total += row[i]
        tom.append(total)
    print(tom)

def exercise_11():
    user_entry = []
    total = 0 
    while True:
        n = int(input("Enter an number:"))
        user_entry.append(n)
        if (n%2 ==0 and n > 11): 
            for num in user_entry:
                total += num  
            print(total)
            print (user_entry[-1])

        elif (n%2 ==1 and n>20):
            print(0)
            break        

def exercise_12():
    """Write a RECURSIVE function called xdrop. This function should receive a list of strings as argument, and it
should return a new list, which is the same as the input, except that it should remove every occurrence of the string
"x"."""
    def xdrop(s:str):
        if s == []:
            return []
        
        if s[0] == "x":
            return xdrop(s[1:])
        return [s[0]]+xdrop(s[1:]) #Note: the syntax s[0]+xdrop(s[1:]) is a data type error b/c s[0]
                                    # is str and xdrop(s[1:] is list. Cannot str+list so put s[0] inside a list like this [s[0]]
    
    s = ["abc", "x", "def", "ghi", "x", "snexa"]
    print(xdrop(s))

def exercise_13():
    def allit(strings):
        count = 0  
        first_letter = strings[0][0]
        for word in strings: 
                if word[0] == first_letter: 
                    count += 1
                   
        return count

    strings = ["apple", "bear", "angle", "alligator", "banana", "alpha","anna"]
    print(allit(strings))


def exercise_14():
    class scheudle:
        def __init__(self,total):
            self.total_seats = total
            self.seats_taken = 0 
            self.res = {}


def exercise_15():
    def reverseList(x):
        reversed_list = []
        for i in range(len(x) - 1, -1, -1):  # Start from the last index
            reversed_list.append(x[i])  # Add each element to the new list
        return reversed_list

    x= [1,2,3,4,5,6]
    print(reverseList(x))


def exercise_16():
    fruits = ['Pear', 'Lime', 'Banana']
    prices = [1.25, 0.85, 1.50]
    fp={}
    for i in range (len(fruits)):
        fp[fruits[i]] = prices[i]
    print(fp)


def exercise_17():
    d = {"sneha": 1, "zejd": 2, "fahid": 3}
    for key, value in d.items():
        print(key, value, end=' ')

def exercise_18():
    pqr = ["hiya", "igloo", "jump", "kangaroo", "lion"]
    for word in range (len(pqr)):
        # if len(word)>0:
        print(word[3])

def exercise_19():
    start = 11 
    while start <= 401:
        sum = 0
        for i in range(40):
            sum += start ** 2
            start +=10
        break

    print(sum)

def exercise_20():
    """same problem as q19 but using for loop"""
    sum = 0
    for i in range(11,402,10):
        sum += i ** 2
    print(sum)

def exercise_21():
    """prof's solution for the previous q"""
    rs = 0 
    for n in range(1,41):
        rs += (10*n+1)**2
    print(rs)


def exercise_22():
    wordy = ["talk", "attention","bobobobo"]
    count = 0
    for word in wordy:
        for letter in word:
            if letter == "t":
                count+= 1
    print(count)

def exercise_23():
    def is_part(first, second):
        for i in range(len(first)):
            if first[i] * second[i] == 4:
                return True
        return False
    x = [4,2,-1]
    y= [1,2,-5]
    print(is_part(x,y))

def exercise_24():
    table = [[1,5,2,10], [3,15,4,20]]
    for i in range(4):
        for j in range(2):
            print(table[j][i], end = '  ')
    print('')

def exercise_25():
    def sum_of_digits(n):
        if n == 0:
            return 0
        return n % 10 + sum_of_digits(n // 10)
    print(sum_of_digits(100))

def exercise_26():
    s = ["sneha"]
    for l in range(len(s)-1,-1,-1):
        reversed = s[l][::-1] #s[l] accesses "sneha" and reverses using [::-1] slicing
        print (reversed)
##########################################
def solve(ex_number:int):
    if ex_number == 1:
        exercise_1()
    if ex_number == 2:
        exercise_2()
    if ex_number == 3:
        exercise_3()
    if ex_number == 4:
        exercise_4()
    if ex_number == 5:
        exercise_5()
    if ex_number == 6:
        exercise_6()
    if ex_number == 7:
        exercise_7()
    if ex_number == 8:
        exercise_8()
    if ex_number == 9:
        exercise_9()
    if ex_number == 10:
        exercise_10()
    if ex_number == 11:
        exercise_11()
    if ex_number == 12:
        exercise_12()
    if ex_number == 13:
        exercise_13()
    if ex_number == 14:
        exercise_14()  
    if ex_number == 15:
        exercise_15()
    if ex_number == 16:
        exercise_16()
    if ex_number == 17:
        exercise_17()
    if ex_number == 18:
        exercise_18()
    if ex_number == 19:
        exercise_19()
    if ex_number == 20:
        exercise_20()
    if ex_number == 21:
        exercise_21()
    if ex_number == 22:
        exercise_22()
    if ex_number == 23:
        exercise_23()
    if ex_number == 24:
        exercise_24()
    if ex_number ==25:
        exercise_25()

    if ex_number ==26:
        exercise_26()
solve(26)


    # avg = []
    # def modify_list(numlist):
    #     for row in numlist:
    #         total = 0 
    #         for num in row:
    #             total+= num
    #         average = total / len(row)
    #         avg.append([average]) #values of average is wrapped inside a list which is then appended in the avg list

       # count = 0  # Initialize the count of matching strings
        # for word in strings:  # Outer loop to pick a string
        #     # for other in strings:  # Inner loop to compare it with every string
        #         if word[0] == strings[0][0]: 
        #             count += 1
                   
        # return count