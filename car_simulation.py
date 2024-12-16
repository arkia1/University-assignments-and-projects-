# Car class with movement and speed calculation
class Car:
    def __init__(self, name, model, brand):
        self.name = name
        self.model = model
        self.brand = brand
        self.location = [0, 0, 0]  # Default starting position

    def move(self, target_location, time):
        """
        Moves the car to the target location and calculates the speed.
        :param target_location: A list [x, y, z] representing the new position.
        :param time: The time taken to move to the target location (in hours).
        :return: The speed in units/hour.
        """
        distance = ((target_location[0] - self.location[0]) ** 2 +
                    (target_location[1] - self.location[1]) ** 2 +
                    (target_location[2] - self.location[2]) ** 2) ** 0.5
        self.location = target_location
        if time > 0:
            speed = distance / time
        else:
            raise ValueError("Time must be greater than 0 to calculate speed.")
        return speed


# Example usage
if __name__ == "__main__":
    my_car = Car("Sedan", "Model S", "Tesla")
    try:
        speed = my_car.move([10, 15, 5], 2)  # Move to new location in 2 hours
        print(f"The car's speed was {speed} units/hour.")
    except ValueError as e:
        print(e)
