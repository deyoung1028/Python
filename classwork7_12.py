#class Table:
   # def __init__(self):
       # self.finish = ""
        #self.length = ""
        #self.type = ""
        #self.style = ""

#table = Table()
#table.finish = "Cherry"
#table.length = "50 in."
#table.type = "executive"
#table.style = "Oxford"

#Bank Account

class BankAcount:
    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
     self.balance += amount

    def withdrawl(self, amount):
         if self.balance >= amount:
            self.balance -= amount

    def transfer_funds(self, amount, destination):
        #withdraw from source account 
        self.withdrawl(amount)
        #deposit to destination account
        destination.deposit(amount)



account = BankAcount("1234")
account.deposit(100)
account.withdrawl(200)
print(f"Account balance: {account.balance}")

source_account = BankAcount("5678")
source_account.deposit(500)

destination_account = BankAcount("456")

source_account.transfer_funds(100, destination_account)

print(source_account.balance) #400
print(destination_account.balance) #100




