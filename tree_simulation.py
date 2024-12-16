# Tree class with branches, fruits, and leaves
class Tree:
    def __init__(self, type_of_tree):
        self.type_of_tree = type_of_tree
        self.branches = []  # List of branches
        self.fruits = []  # List of fruits
        self.leaves = []  # List of leaves

    def add_branch(self, branch):
        self.branches.append(branch)

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def add_leaf(self, leaf):
        self.leaves.append(leaf)

    def leaves_fall(self):
        """
        Simulates all leaves falling to the ground.
        """
        fallen_leaves = self.leaves
        self.leaves = []  # All leaves fall off
        return fallen_leaves


class Branch:
    def __init__(self, length, thickness):
        self.length = length
        self.thickness = thickness


class Fruit:
    def __init__(self, type_of_fruit, weight):
        self.type_of_fruit = type_of_fruit
        self.weight = weight


class Leaf:
    def __init__(self, color, size):
        self.color = color
        self.size = size


# Wind class to simulate interaction with the tree
class Wind:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def blow_leaves(self, tree):
        """
        Simulates wind blowing leaves off a tree.
        :param tree: A Tree object.
        :return: Leaves blown away by the wind.
        """
        return tree.leaves_fall()


# Flower class
class Flower:
    def __init__(self, color, petals):
        self.color = color
        self.petals = petals


# Grass class
class Grass:
    def __init__(self, height):
        self.height = height

    def grow(self, growth_rate, time):
        """
        Simulates grass growing over time.
        :param growth_rate: Growth rate in height per unit time.
        :param time: Time duration for growth.
        """
        self.height += growth_rate * time


# Example usage
if __name__ == "__main__":
    my_tree = Tree("Oak")
    my_tree.add_branch(Branch(5, 1))
    my_tree.add_leaf(Leaf("Green", "Medium"))
    my_tree.add_fruit(Fruit("Apple", 0.2))

    # Wind simulation
    light_breeze = Wind(5, "North")
    fallen_leaves = light_breeze.blow_leaves(my_tree)
    print(f"Leaves fallen: {len(fallen_leaves)}")

    # Grass simulation
    my_grass = Grass(5)  # Initial height 5
    my_grass.grow(0.2, 10)  # Grow at 0.2 units per time for 10 units of time
    print(f"The grass height is now {my_grass.height} units.")
