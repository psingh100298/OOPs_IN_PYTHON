class Customer:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
    if(customer.gender=='Male'):
        print("Hello", customer.name,'Sir')
    else:
        print("Hello", customer.name,'Mam')


n = input("Hi, Please enter your name")
g = input("Please enter your gender(Male/Female)")
cust = Customer(n,g)
greet(cust)
print(cust.name)