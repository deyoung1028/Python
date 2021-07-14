
name = input("Please enter your name: ")

file = open("guest.txt" , "w")
file.write(name)
file.close()