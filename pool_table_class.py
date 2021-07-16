from datetime import datetime 

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None
        self.stop_time = None
        self.total_time = None 
        self.total_cost_per_hour = 30.0
        self.total_cost = 0.0

    def checking_out(self):
        self.is_occupied = True
        self.start_time = datetime.now()
        self.total_cost = 0.0
        

    def checking_in(self):
        self.is_occupied = False
        self.stop_time = datetime.now()
        self.total_time = self.stop_time - self.start_time
        self.total_time_minutes = self.total_time.total_seconds() / 60
        self.total_cost = (self.total_cost_per_hour / 60) * self.total_time_minutes

        
        
    
        
       



