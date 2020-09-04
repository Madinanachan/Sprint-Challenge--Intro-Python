# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self,name,num_wheels=4):
        self.name=name
        self.num_wheels=num_wheels;

    def drive(self):
        print("vrooooom");

    # TODO

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name,2)
      
    def drive(self):
        print("BRAAAAP!!")
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle("Maxthecar"),
    GroundVehicle("Sarathecar",3),
    Motorcycle("Harley"),
    GroundVehicle("MustangSally"),
    Motorcycle("Davidson"),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
for i in vehicles:
    print(f'{i.name} number of wheels: {i.num_wheels}')
    i.drive()
