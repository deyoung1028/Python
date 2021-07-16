#json
# int, float, bool, dictionary, array
#array of int, array of dictionary, array of bool, etc.

import json
from os import name

# write json

#with open("car.json", "w") as file
    #car = {"make":"Honda", "model": "Accord", "noOfCylinders":2}
    #json.dump(object you want to write, file object)
   # json.dump(car,file)

users = []
while True: #loop

    with open("users.json", "w") as file: #setup for writing a json file
        json.dump(users,file) #  command to write a json file

        name = input("Please enter your name:")
        age = int(input("please enter age:"))
        user = {"name": name, "age": age} # dictionary format for array

        users.append(user) #adds a new user to the array 

    choice = input("Q to quit")
    if choice =="q": 
        break   


#read JSON

with open("users.json") as file: #setup for reading a json file
    person = json.load(file) # command to create a json that you can read

for user in users: #loop to display users and user ages
    print(user["name"])
    print(user["age"])

