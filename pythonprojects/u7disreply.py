class Car:
    def __init__(self, color, speed=0, position=0):
        self.color = color  # Color of the car
        self.speed = speed  # Speed in mph
        self.position = position  # Position in miles

    def drive(self, time):
        # Moves the car based on speed and time
        self.position += self.speed * time
        return f"The car is now at position {self.position} miles."

# Example of creating and using a Car object
my_car = Car(color="Red", speed=60)
print(my_car.drive(2))  # Drive for 2 hours at 60 mph

carro = Car("Blue", 120)
print(carro.drive(6))