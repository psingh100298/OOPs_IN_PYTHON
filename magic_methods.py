class Student:
    def __init__(self,name):
        self.name=name

movies = ['Matrix','Finding Nemo']

class Garage:
    def __init__(self):
        self.cars = []

    #Magic method or dunder method
    def __len__(self):
        return len(self.cars)
    
    #magic method for getting index
    def __getitem__(self,i):
        return self.cars[i]
    
    def __repr__(self):
        return f"<Garage: {self.cars}>"
    
    # def __str__(self):
    #     return f"Garage with {len(self)} cars."


    
ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford)

for car in ford:
    print(car)

# print(len(ford))

# print(ford[0])   #Garage.__getitem__(ford,0)