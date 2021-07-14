#name = input("Please enter your name: ")

#option 1 

#file = open("guest.txt" , "w")
#file.write(name)
#file.close()

#Option 2

#while True:
    #with open("programming-likes.txt", "a") as file:
        #file.write(input("Tell me, why do you enjoy programming?"))
        #file.write("n")


while True:
    
    with open("favorite-dish.txt", "a") as file:
        favorite_dish = input("What is your favorite dish?  ")
        file.write(favorite_dish)
        file.write("\n")


    choice = input("enter q to quit of any key to continue:")

    if choice == "q":
        break

with open("favorite-dish.txt") as file:
    content = file.read()
    print(content)


