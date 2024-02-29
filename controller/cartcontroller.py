from model.CartHandler import CartHandler
from model.database import Database
from view.cartui import CartUi
from datetime import date

class CartController:

    def __init__(self, db: Database, loggedInUser):
        self.db = db
        self.cart_handler = CartHandler(db)
        self.loggedInUser = loggedInUser
        self.view = CartUi()

    
    def checkout(self):
       cart_list = self.cart_handler.fetch_cart(self.loggedInUser["Email"])
       if len(cart_list) == 0:
           print("\nYour cart is empty")
           return
       self.view.print_contents(cart_list)
       
       while(True):
        OPTION_PROCEED = "y"
        OPTION_CANCEL = "n"
        input = self.view.get_input("Proceed to checkout (Y/N)?: ")

        if input.lower() == OPTION_PROCEED:
            self._save_order(cart_list)
            break
        elif input.lower() == OPTION_CANCEL:
            break
        else: 
            print("Invalid input")
            continue
        
    
    def _save_order(self, cartlist):
        order_date = date.today()
        last_row_id = self.cart_handler.save_order(order_date, self.loggedInUser)
        self.cart_handler.save_order_details(cartlist, last_row_id)
        self.cart_handler.empty_cart(self.loggedInUser["UserId"])
        self.view.print_invoice(cartlist, last_row_id, self.loggedInUser)