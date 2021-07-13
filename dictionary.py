#Take inputs for firstname and lastname and then create a dictionary with your first and last name. 
#Finally, print out the contents of the dictionary on the screen in the following format.

users=[]

while True:
    first = input("Enter first name:")
    last = input("Enter last name:")

    user = {"first" : first, "last": last}
    users.append(user)

    choice = input("Enter q to quit or any key to continue:")
    if choice == "q":
        break
print(users)

