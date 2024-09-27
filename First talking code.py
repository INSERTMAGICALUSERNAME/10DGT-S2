# TODO: Create a program that asks a user a question and reutrns a response based on the answer
# main loop. Keeps running until a condition is met 

Loopy_mc_looper = ""
while Loopy_mc_looper == "":
    Like_Roblox = input("Do you like Roblox?").lower()
    if Like_Roblox == "yes" or Like_Roblox == "y":
        print("You are dumb")
    elif Like_Roblox == "no" or Like_Roblox == "n":
        print("Congrats, you have a brain")
    
    Like_Minecraft = input(" do you like minecraft?").lower()
    if Like_Minecraft == "yes" or Like_Minecraft == "y":
        print("Yay")
    elif Like_Minecraft == "no" or Like_Minecraft == "n":
        print("(´・ω・`)")
    
    Go_again = input("Do you want me to ask again? (Y/N)").lower()
    if Go_again == "no" or Go_again == "n":
        Loopy_mc_looper = Go_again
    elif Go_again == "yes" or Go_again == "y":
        print ("ok then")
    
    else:
        print("Use a normal answer please ಠ~ಠ")
        
        