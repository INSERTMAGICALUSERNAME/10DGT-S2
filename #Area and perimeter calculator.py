#Area and perimeter calculator 
#Author: Johann Shobolt
#Date: 2024/10/25
#Version: 1

print('This program will calculate the area and perimeter of your shape')
def valid_num (question):
    error = "whoops, that is not a valid number"
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
#Make this loop, dont be lazy 
width = valid_num('enter your width\n')
print (f'the width of your shape is {width}')
height = valid_num('now enter the shapes height\n')
perimeter = (width * 2) + (height * 2) 
area = width * height 
print(f'The perimeter of your shape is {perimeter}\n')
print (f'The area of your shape is {area}')









'''loopy_mc_looper = ''
while loopy_mc_looper == '':
    width = float(input('Enter the width of your shape'))
    print (f'The Width of your shape is {width}')
    height = float(input('Enter the height of your shape'))
    print (f'The Height of your shape is {height}')'''
