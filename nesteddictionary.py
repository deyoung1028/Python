#Create a dictionary with your first name, last name and list of addresses (2 addresses is fine) - nested dictionary

user = {"first_name":"Jennie" , "last_name":"DeYoung"}

address1 = {"street":"123 Main", "city":"Atlanta", "state":"GA"}
address2 = {"street":"456 Paradise", "city":"Fiji", "state":"NZ"}

user["addresses"] = [address1, address2]

print(user)