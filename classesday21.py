class Car:
    #  (attribute)
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # (method)
    def drive(self):
        print(f"The {self.color} {self.brand} is driving!")

# Create car objects
car1 = Car("Toyota", "red")
car2 = Car("Tesla", "black")

# Access attributes
print(car1.brand)   # Toyota
print(car2.color)   # black

# Call the method
car1.drive() 
car2.drive() 
