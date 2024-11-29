#Bits calculator
#Author: Johann Shobolt
#Date: 2024/11/22
#Version: 5


def valid_num (question): # Function to output a valid number
    error = "that is not a valid response ಠ~ಠ\n"
    while True:
        try:
            response = int(input(question))
            if 0 < response: 
                break
            else:
                print (f'{error}\n')
        except ValueError:
            print (error)
    return response

print ('This program will calculate the amount of bits needed to represent data, either a text type, image or integer\n')

loopy_mc_looper = ''#this is the loop variable
while loopy_mc_looper == '':
    print ('______________________\n') #line breaks make output easier to read

    selection = valid_num('Enter a number that corresponds to the data type that you want \n1:Text \n2:Image \n3:Integer\n')#asking what they want calculated
    print ('______________________\n')
    if selection == 1:
        text_bit = len(input('Enter your sentence (only use ascii symbols and no numbers)\n'))* 8 #getting the input, counting it and then multiplying by eight

        print (f'the amount of bits needed to represent your sentence is:\n{text_bit}\n')#out put
        print ('______________________\n')

    #find pixels up find pixels across, multply them, then times by 24
    elif selection == 2:
        width = valid_num('Enter the amount of pixels on the width of the image:\n')  # getting width and height   
        height = valid_num('Now enter the images height:\n') 
        image_bits = (width * height) * 24 # multipling width and height and then by 24 to get bits
        print (f'The amount of bits needed to represent your image is {image_bits}\n') #outputting bits
        print ('______________________\n') #line breaks make output easier to read
    
    elif selection == 3:
        integer_bit  = len(str(bin(valid_num("Enter the integer:\n" ))[2:])) # converting input to binary, turning into a string, and then counting the digits
        print (f'the amount of bits needed is {integer_bit}') # output 
    
    else:(print(f'Mate, you had one job, it was a choice between 1 2 or 3, and you chose {selection}?\n')) # fail response
    
    loopy_mc_looper = input("Do you want me to ask again? <enter> to keep going, anything else to stop").lower()#finsihing the loop
    if loopy_mc_looper == '':
        print ()
    else:
        print ('Thank You for using this calculator')#exit message
    

    



   
    
