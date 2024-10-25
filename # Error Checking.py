# Error Checking and functions
# Author: Johann Shotbolt 
# Date 2024/10/25
# Version: 1


#Code that tests that a valid number is entered
'''done = False # this is a boolean variable set to false 
while not done: # this is a loop that runs until a valid number is entered 
    
    num_1 = int(input ("Please enter your value"))
    done = True 
print (f'The number you entered is {num_1}')'''

# Code that tests that a valid number is entered (V2)
# Create a function to call everytime i ask for a number.
# a function is a chunk of code that does something, and can be used over and over. To use a function, I call it by writing out it's name.
'''def test_valid_int(question):
    done = False 
    while not done:
        print (question) #  the 'question' is a place holder
        try: # this tries for a valid interger
            num = int(input())
            done = True

        except ValueError:
            print ('mate,that aint a valid number bro')

    return (num) # this gives back the value of num so that it can be used outside of the function
# Main program
num_1 = test_valid_int("Please enter your first number")
print (f'you entered {num_1-1}')

num_2 = test_valid_int ("Please enter your second number\n")
print (f'You entered {num_2-6}')

#My calculator 
sum = num_1 + num_2
subtract = num_1 - num_2  
multiply = num_1 * num_2 
print ('nah, just kidding\n')
print (f'You entered {num_1} and {num_2}')
answer = input('Do you want +,-,*')
    if answer == "+":
        print (f'The total of {num_1} and {num_2} is {sum}')
    elif answer == "-":
        print (f'The difference of {num_1},{num_2} and {num_3} is {subtract}')
    elif answer == "*":
        print (f'The product of {num_1},{num_2} and {num_3} is {multiply}')
    else:
        print ('answer with a symbol')'''

# version 3, refining code, making more pythonic
# ask the user to pick a number in a range
def valid_num (question, low, high):
    error = f"whoops, that is not an interger between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                break
            
            else:
                print (error)
                print ()
        except ValueError:
            print(error)
    return response
num_1 = valid_num("Enter a number between 1 and 15:", 1, 15)
print (f'you entered {num_1}\n')
num_2 = valid_num("Now enter a number between 50 and 100:",50,100)
print (f'You entered {num_2}\n')
num_3 = valid_num("Now enter a number between 1 and 100:",1,100)
print (f'You entered {num_3}\n')
#Multiply the results
multiply = num_1 * num_2 * num_3
print (f'the sum of {num_3}, {num_2} and {num_1} is {multiply}')





 
    