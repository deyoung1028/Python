#from datetime import datetime 

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None
        self.stop_time = None
        

    def checking_out(self):
        self.is_occupied = True
        

    def checking_in(self):
        self.is_occupied = False
        print(f"Table {self.table_number} is available!")
        
       



