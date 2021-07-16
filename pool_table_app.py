pool_tables_arr = []

from pool_table_class import PoolTable

for i in range(1, 13):
        pool_tables = PoolTable(i)
        pool_tables_arr.append(pool_tables)


def display_all_tables():
    for pool_table in pool_tables_arr:
        if pool_table.is_occupied == False:
          print(f"\n Pool Table {pool_table.table_number} ------ is occupied {pool_table.is_occupied}")
        if pool_table.is_occupied == True:
            print(f"\n Pool Table {pool_table.table_number} ------ is occupied {pool_table.is_occupied} ")

def save_to_file():
    with open("pool_tables.txt", "w") as file:
        for table in pool_tables_arr:
            file.write(f'Table number: {table.table_number} | {table.start_time} | {table.stop_time} | {table.total_time} | {table.total_cost} \n')
             

while True:
    print("\n")
    print("\n")
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
    print("3 - To Quit Application")

    choice = input("Enter choice:\t")

    if choice == "1": #Check out a pool table
        display_all_tables()
        choice = int(input("Please select a table:"))
        chosen_table = pool_tables_arr[choice -1]
        if pool_tables_arr[choice -1].is_occupied ==True:
           print(f"!!!Uh Oh! Table number {choice} is occupied,please select another table!!")
        chosen_table.checking_out()
        print(f"You checked out table {chosen_table.table_number} at {chosen_table.start_time}")

    if choice == "2": #check in a pool table
        display_all_tables()
        choice = int(input("Please enter the number of the table that you wish to return:"))
        return_table = pool_tables_arr[choice -1]
        return_table.checking_in()
        print(f"Table {return_table.table_number} is now checked in! Total Time Played = {return_table.total_time_minutes} minutes")
        print(f"Total Cost: $ {return_table.total_cost} dollars")
        save_to_file()


    if choice == "3":
        break


