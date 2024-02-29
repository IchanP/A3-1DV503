from view.ui import ui

class CartUi(ui):

    def __init__(self):
        super().__init__()

    def print_contents(self, cart_items):
        print("Current Cart Contents:")
        print("{:<15} {:<50} {:<10} {:<10} {:<10}".format('ISBN', 'Title', '$', 'Qty', 'Total'))
        print("-" * 105) 
        
        for item in cart_items:
            self._print_item(item)
        
        self._print_total_cost(cart_items)


    def _print_item(self, cart_item):
        isbn = cart_item['ISBN']
        title = cart_item['Title']
        price = cart_item['Price']
        qty = cart_item['Quantity']
        total = cart_item['Total']
        print("{:<15} {:<50} {:<10} {:<10} {:<10.2f}".format(isbn, title, price, qty, total))

    
    def _print_total_cost(self, cart_items):
        total_price = sum(item['Price'] * item['Quantity'] for item in cart_items)
        print("-" * 105)  
        print("Total: {:>99}".format(f"${total_price:.2f}"))

    def print_invoice(self, cart_items, order_id, user):
        print("\n")
        print(" " * 25 + "Invoice for Order no." + str(order_id))
        print("Shipping Address")
        print("Name: " + user["First Name"] + " " + user["Last Name"])
        print("Address: " + user["Address"])
        print(" " * 10 + user["City"])
        print(" " * 10 + str(user["Zip"]))
        self.print_contents(cart_items)
        input("\nEnter any key to continue...")