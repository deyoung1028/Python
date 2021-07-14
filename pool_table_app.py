pool_tables_arr = []

from pool_table_class import PoolTable

for i in range(1, 13):
        pool_tables = PoolTable(i)
        pool_tables_arr.append(pool_tables)

def display_open_tables():
    for pool_table in pool_tables_arr:
        print(f"\n Pool Table {pool_table.table_number} ------ is occupied {pool_table.is_occupied}")

def display_checked_out_tables():
    for pool_table in pool_tables_arr:
        if pool_table.is_occupied == True:
            print(f"\n Pool Table {pool_table.table_number}")


while True:

    print("\t\t\t\t\tWELCOME!!!!!")
    print("\n")
    print("_____________________________________Pool Table Manager______________________________________")
    print("\n")
    print("\t\t\tPlease select from one of the options below:")
    print("\n")
    print("1 - Check Out a Pool Table")
    print("\n")
    print("2 - Check in a Pool Table")
    print("\n")
    print("3 - Print Pool Table Usage")
    print("\n")
    print("4 - Print Pool Table Receipt")
    print("\n")
    print("5 - To Quit Application")

    choice = input("Enter choice:\t")

    if choice == "1":
        display_open_tables()
        choice = int(input("Please select a table:"))
        chosen_table = pool_tables_arr[choice -1]
        chosen_table.checking_out()

     #if choice == "2":




    #if choice == "3": 

    #if choice == "4": 

    if choice == "5":
        break

    
