
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=float(0), item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
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
    
    def modify_item(self, item):
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                if item.item_price != 0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_description != "none":
                    self.cart_items[i].item_description = item.item_description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = 0.0
            for item in self.cart_items:
                item.print_item_cost()
                total_cost += item.item_price * item.item_quantity
            print(f"\nTotal: ${total_cost}")
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}") 

def print_menu(shopping_cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")
    answer = input("Choose an option: ")
    while answer != 'q':
        if answer == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item)
        elif answer == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            shopping_cart.remove_item(item_name)
        elif answer == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(item_name, 0, new_quantity, "")
            shopping_cart.modify_item(item)
        elif answer == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            print(f"{shopping_cart.customer_name}'s Shopping Cart - {shopping_cart.current_date}\n")
            print("Item Descriptions")
            for item in shopping_cart.cart_items:
                item.print_item_description()
        elif answer == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()
        else:
            print("Invalid option. Please try again.")
        print_menu(shopping_cart)    
    print("Exiting the program.")
    exit()

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)

main()
