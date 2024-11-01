#Fence cost calculator 
#Author: Johann Shobolt
#Date: 2024/10/31
#Version: 4


print ()
print ()
print('This program will calculate the cost of a fence')
def valid_num (question): # Function to output a valid number
    error = "that is not a valid number ಠ~ಠ\n"
    while True:
        try:
            response = float(input(question))
            if 0 < response: 
                break
            else:
                print (error)
                print ()
        except ValueError:
            print (error)
    return response

loopy_mc_looper = ''#this is a loop variable
while loopy_mc_looper == '':
    width = valid_num('Enter your width:\n')#asking for width
    print (f'The width of your area is {width}')

    length = valid_num('Enter the shapes length:\n')#asking for height
    print (f'The length of your area is {length}\n')

    fence_cost = valid_num(f'What is the cost per metre of each fence?\n')#asking what the cost p/m of fence is
    print (f'The cost of each fence is {fence_cost}\n')

    print ('______________________\n') #line breaks make output easier to read

    perimeter = (width * 2) + (length * 2) #calculating perimeter of the fence line
    print(f'The perimeter of your shape is {perimeter} units\n')

    print ('______________________\n') #line breaks make output easier to read


    total_fence_cost = perimeter * fence_cost #calculating cost
    print (f'The cost total cost of the fence is ${total_fence_cost}\n')

    print ('______________________\n') #line breaks make output easier to read

    
    # Ask again loop
    loopy_mc_looper = input("Do you want me to ask again? <enter> to keep going, anything else to stop\n").lower()
    if loopy_mc_looper == '':
        print ()
    else:
        print ('Thank You for using this calculator')

