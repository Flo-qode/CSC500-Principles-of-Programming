class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# Example usage of the class
item = ItemToPurchase("Bottled Water", 1.0, 10)
item.print_item_cost()

def get_item_details(item_number):
    print(f"Item {item_number}")
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    return ItemToPurchase(item_name, item_price, item_quantity)

# Get details for two items from the user
item1 = get_item_details(1)
item2 = get_item_details(2)

# Calculate the total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

# Print the individual item costs
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

# Print the total cost
print(f"Total: ${total_cost:.2f}")
