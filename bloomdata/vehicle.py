# imagine i want to list these vehicles on Craigslist
# we can make this the "Parent" class
'''
This is a file with 2 classes
One class is a vehicle and one is a convertible.
'''
class Vehicle:

    def __init__(self, make, model, color, year, mileage):
        # when user passes in those arguments, 
        # you assign them to this particular object's attributes
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return 'HOOOOOOOONK!'

    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"

if __name__ == '__main__':
    my_vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 60000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)
    print(my_vehicle)

# imagine i want to list these vehicles on Craigslist
# We can make this the 'child' class
# the Convertible(Vehicle) notation means
# the Convertible class "inherits" from the Vehicle class
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, mileage, top_down=True):
        # super means look at the parent class
        # and look at the following attributes in parenthesis to integrate
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True
            return "Top is now down."

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} convertible with {self.mileage} miles"

if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 60000)

    # print(my_vehicle.make)
    # print(my_vehicle.mileage)

    # print(my_vehicle.honk())
    # print(my_vehicle.drive(1234))
    # print(my_vehicle.mileage)
    # print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())
    print(my_vehicle.top_down)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))