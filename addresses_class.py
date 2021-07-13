class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)
        

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

user = User("John", "Doe")
address = Address("1200 Richmond", "Atlanta", "GA", "30517")

user.add_address(address)
user.add_address(Address("1234 Main", "Atlanta", "GA", "30517"))

for address in user.addresses:
    print(address.street)
    print(address.city)
    print(address.state)
    print(address.zip_code)


class Post:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author
        self.comments = []
    