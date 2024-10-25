#Area and perimeter calculator 
#Author: Johann Shobolt
#Date: 2024/10/25
#Version: 2


print ()
print ()
print('This program will calculate the area and perimeter of your shape')
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
    perimeter = (width * 2) + (height * 2) 
    area = width * height 
    print(f'The perimeter of your shape is {perimeter}\n')
    print (f'The area of your shape is {area}\n')

    Go_again = input("Do you want me to ask again? (Y/N)").lower()
    if Go_again == "no" or Go_again == "n":
        loopy_mc_looper = Go_again
    elif Go_again == "yes" or Go_again == "y":
        print ("ok then\n")
    
    else:
        print("Use a normal answer please ಠ~ಠ\n")











