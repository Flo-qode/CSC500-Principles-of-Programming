class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description=""):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                found = True
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_description != "":
                    item.item_description = item_to_modify.item_description
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        
        total_cost = 0
        for item in self.cart_items:
            item.print_item_cost()
            total_cost += item.item_price * item.item_quantity
        
        print(f"\nTotal: ${total_cost}")

    def print_descriptions(self):
        print(f"OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()
def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:
"""
    while True:
        print(menu)
        choice = input()
        
        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
            
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter the name of the item to remove:\n")
            cart.remove_item(name)
            
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(name, quantity=quantity)
            cart.modify_item(item)
            
        elif choice == 'i':
            cart.print_descriptions()
            
        elif choice == 'o':
            cart.print_total()
            
        elif choice == 'q':
            break
            
        else:
            print("Invalid choice. Please try again.")
def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    cart = ShoppingCart(customer_name, current_date)
    
    print_menu(cart)

if __name__ == "__main__":
    main()