class Customer:

    def __init__(self,name):
        self.name=name

def greet(customer):
    print("Hello", customer.name)


cust = Customer('Nitish')
greet(cust)
print(cust.name)