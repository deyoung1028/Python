#Grocery App with delete option and exceptions

stores_arr = [] #global array

class Shoppinglist:
     def __init__(self, store, address):
        self.store = store
        self.address  = address
        self.items = []

     def add_item(self, item):
        self.items.append(item)


class Groceryitem:
     def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

while True:
    print("-----------Grocery Shopping List-----------")
    print("1 - Add Store")
    print("2 - Add item")
    print("3 - View all lists")
    print("4 - Delete a store")
    print("5 - Delete an item")
    print("6 - to quit")

    try:
        choice = int(input("Enter Choice:"))
    


        if choice == 1 :
            store_name = input("Add a store:")
            store_address = input("Add address:")
            store = Shoppinglist(store_name, store_address)
            stores_arr.append(store)
        

        elif choice == 2:
            for index in range(0, len(stores_arr)):
                print(f"{index + 1}--{stores_arr[index].store}")
            
                
            store_location = int(input("Which store?:"))
            item_name = input("add item:")
            item_quantity = int(input("How many?"))
            item_price = float(input("Enter the item price:"))
            item = Groceryitem(item_name, item_quantity, item_price)
            shopping_list = stores_arr[store_location -1]
            shopping_list.items.append(item)
            
        

        elif choice == 3:
            for store in stores_arr:
                print(f"{store.store} - {store.address}")
                for index in range(0, len(store.items)):
                    title = store.items[index].title
                    print(title)

        elif choice == 4:
            for index in range(0, len(stores_arr)):
              print(f"{index + 1} - {stores_arr[index].store}")
            del_store = int(input("Enter store number that you would like to delete:"))
            del stores_arr[del_store - 1]  

        elif choice == 5:
            for index in range(0, len(stores_arr)):
                print(f"{index + 1} -- {stores_arr[index].store}")
            store = stores_arr[index]
            choice3 = int(input("enter store choice:"))
            store = stores_arr[choice3 - 1]
            for index in range(0, len(store.items)):
                print(f"{index} {store.items[index].title} ")
            itemToDeleteIndex = int(input("Enter item to delete:"))
            del store.items[itemToDeleteIndex]
            print("Item deleted")


        elif choice == 6:
            break

    except ValueError:
        print("Invalid input. Please enter a number, not a letter!!!")

    