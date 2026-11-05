#Write a Python program to create two classes BMW and Ferrari. 
#Both the classes have similar methods - fuel_type and max_speed 
#that will display the fuel type and max speed for respective cars. 
#Implement polymorphism on these two classes.
class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Diesel"

    def max_speed(self):
        return "300 km/h"

car1 = BMW()
car2 = Ferrari()
print(car1.fuel_type())
print(car1.max_speed())
print(car2.fuel_type())
print(car2.max_speed())