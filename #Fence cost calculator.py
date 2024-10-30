#Fence cost calculator 
#Author: Johann Shobolt
#Date: 2024/10/30
#Version: 3


print ()
print ()
print('This program will calculate the cost of a fence')
def valid_num (question):
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

loopy_mc_looper = ''
while loopy_mc_looper == '':
    width = valid_num('Enter your width:\n')
    print (f'The width of your shape is {width}')

    height = valid_num('Now enter the shapes height:\n')
    print (f'The Height of your shape is {height}\n')

    fence_cost = valid_num(f'What is the cost per metre of each fence?\n')
    print (f'The cost of each fence is {fence_cost}\n')

    perimeter = (width * 2) + (height * 2) 
    print(f'The perimeter of your shape is {perimeter} units\n')

    total_fence_cost = perimeter * fence_cost
    print (f'The cost total cost of the fence is ${total_fence_cost}')
    
    
    loopy_mc_looper = input("Do you want me to ask again? <enter> to keep going, anything else to stop").lower()
    if loopy_mc_looper == '':
        print ()
    else:
        print ('Thank You for using this calculator')

