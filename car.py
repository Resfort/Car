class car:
    def __init__(self, make, model, year, color, max_fuel):

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.max_fuel = max_fuel
    def refuel(self, liters):
        if liters <=0:
            return "Please enter a valid amount of fuel to refuel."
        if self.max_fuel <=0:
            return "The fuel tank is already full."
        

car1 = car("Toyota", "Camry", 2020, "Blue", 50)