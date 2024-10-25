class OnlineMarket:
    def __init__(self):
        # Initialize the price list with 100 slots (empty values set to None)
        self.size = 100
        self.price_list = [None] * self.size
    
    # Define a hash function to map item codes to index
    def hash_function(self, item_code):
        return item_code % self.size
    
    # Insert an item with its price into the price list
    def insert_item(self, item_code, price):
        index = self.hash_function(item_code)
        
        # Handle collisions using linear probing
        while self.price_list[index] is not None:
            index = (index + 1) % self.size
        
        # Store the (item_code, price) at the found index
        self.price_list[index] = (item_code, price)
    
    # Retrieve the price for an item given its code
    def get_price(self, item_code):
        index = self.hash_function(item_code)
        
        # Use linear probing to find the correct index in case of collisions
        while self.price_list[index] is not None:
            if self.price_list[index][0] == item_code:
                return self.price_list[index][1]
            index = (index + 1) % self.size
        
        return None  # Item not found
    
    # Print the entire price list (for debugging)
    def print_price_list(self):
        for i, entry in enumerate(self.price_list):
            if entry:
                print(f"Index {i}: Item Code {entry[0]}, Price {entry[1]}")

# Create the market price list object
market = OnlineMarket()

# Insert 100 items with prices
for item_code in range(1, 101):
    price = item_code * 10  # Example price logic: price is 10 times the item code
    market.insert_item(item_code, price)

# Example: Retrieve price for a specific item
item_code_to_lookup = 50
price = market.get_price(item_code_to_lookup)
print(f"Price of item with code {item_code_to_lookup}: {price}")

# Optional: Print the entire price list to see all items
market.print_price_list()

#Arkia Ebrahimi 20235443