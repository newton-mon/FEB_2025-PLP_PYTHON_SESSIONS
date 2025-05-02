'''Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.'''

# Parent class
class Building:
    def __init__(self, location, floors, use):
        self.location = location
        self.floors = floors
        self.use = use  # e.g., "Residential", "Commercial"
    
    def describe(self):
        return f"This is a {self.floors}-floor {self.use} building located in {self.location}."
    
    def renovate(self, new_use):
        self.use = new_use
        return f"The building is now repurposed for {self.use} use."

# Subclass with inheritance
class Skyscraper(Building):
    def __init__(self, location, floors, use, has_helipad):
        super().__init__(location, floors, use)
        self.has_helipad = has_helipad

    # Polymorphism: override describe method
    def describe(self):
        base_description = super().describe()
        helipad_info = " It has a helipad." if self.has_helipad else " It does not have a helipad."
        return base_description + helipad_info

    # Encapsulation example
    def get_helipad_status(self):
        return self.has_helipad

    def set_helipad_status(self, status):
        if isinstance(status, bool):
            self.has_helipad = status
        else:
            raise ValueError("Helipad status must be a boolean.")

# Example
b1 = Building("Nairobi", 3, "Residential")
print(b1.describe())
print(b1.renovate("Commercial"))

s1 = Skyscraper("New York", 80, "Commercial", True)
print(s1.describe())
s1.set_helipad_status(False)
print(s1.describe())



'''Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()). 
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() 
prints "Flying" ✈️).'''

# Parent class
class Vehicle:
    def move(self):
        pass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print(" Flying through the sky...")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print(" Sailing on the water...")

# Subclass: Train
class Train(Vehicle):
    def move(self):
        print(" Running on the tracks...")

# Function to demonstrate polymorphism
def show_movement(vehicles):
    for v in vehicles:
        v.move()

# Example 
vehicles = [Car(), Plane(), Boat(), Train()]
show_movement(vehicles)
