class car:
    def __init__(self, make, model, year, color, max_fuel):

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.max_fuel = max_fuel
        self.__fuel_level = 0
    def refuel(self, liters):
        if liters <=0:
            return "Please enter a valid amount of fuel to refuel."
        if self.__fuel_level >= self.max_fuel:
            return "The fuel tank is already full."
        if self.max_fuel - self.__fuel_level < liters:
            return f"Cannot refuel {liters} liters. The fuel tank can only hold {self.max_fuel - self.__fuel_level} more liters."
        self.__fuel_level += liters
        return f"The car has been refueled with {liters} liters of fuel."

    def drive(self, km):
        if self.__fuel_level <= 0:
            return "The car is out of fuel. Please refuel before driving."
        fuel_needed = km / 10
        if fuel_needed > self.__fuel_level:
            return "Not enough fuel to drive the requested distance."
        self.__fuel_level -= fuel_needed
        return f"The car has driven {km} kilometers."
    def get_fuel_level(self):
        return self.__fuel_level

my_car = car("Toyota", "Camry", 2020, "Blue", 50)

print(my_car.refuel(30))
print(my_car.drive(100))
print(my_car.get_fuel_level())