class Atm:
    #static/class variable
    counter =0
    def __init__(self):

        #instance variables
        self.__pin=''
        self.__balance=0
        self.sno = Atm.counter
        Atm.counter = Atm.counter+1
        # self.menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print('Pin changed')

    def menu(self):
        user_input = input('''
                    Hello, how would you like to proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit   ''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.__balance_check()
        else:
            print('Bye')
    
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin")
        if temp==self.__pin:
            amount = int(input("Enter your amount"))
            self.__balance = self.__balance+amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp==self.__pin:
            amount = int(input("Enter the amount"))
            if(amount<=self.__balance):
                self.__balance = self.__balance-amount
                print("Operation successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    def balance_check(self):
        temp = input("Enter pin")
        if temp==self.__pin:
            print(self.__balance)
        
        else:
            print("Invalid pin")




sbi = Atm()