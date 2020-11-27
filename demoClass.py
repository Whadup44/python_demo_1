class Vehicle(object):
    def __init__(self, carName, carSpeed):
        self.name = carName
        self.speed = carSpeed
    
    def displayName(self):
        return(self.name)
    
    def displaySpeed(self):
        return(self.speed)

car = Vehicle("buggy", 75)
print(car.displayName())
print(car.displaySpeed())