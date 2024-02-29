from model.CartHandler import CartHandler
from model.database import Database
from view.cartui import CartUi

class CartController:

    def __init__(self, db: Database, loggedInUser):
        self.db = db
        self.cart_handler = CartHandler(db)
        self.loggedInUser = loggedInUser
        self.view = CartUi()

    
    def checkout(self):
       cartlist = self.cart_handler.fetch_cart(self.loggedInUser)
       self.view.print_contents(cartlist)
       
       while(True):
        OPTION_PROCEED = "y"
        OPTION_CANCEL = "n"
        input = self.view.get_input("Proceed to checkout (Y/N)?: ")

        if input.lower() == OPTION_PROCEED:
         # TODO self._checkout()
            break
        elif input.lower() == OPTION_CANCEL:
            break
        else: 
            print("Invalid input")
            continue
