from model.database import Database
from view.ui import ui
from dotenv import load_dotenv
from controller.accountcontroller import AccountController
from controller.bookcontroller import BookController
from controller.cartcontroller import CartController
import os

load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")

db = Database(username, password)
view = ui()
acc_controller = AccountController(db, view)

#Main menu
def main_menu(options):
    OPTION_LOGIN = 1
    OPTION_REGISTER = 2
    while(True):
        
        view.print_header("Welcome to the Online Book Store") 
        view.print_options(options) 
        choice = view.get_choice(len(options))

        if choice == OPTION_LOGIN:
           email = acc_controller.member_login()
           if email != None:
                member_menu(email)
        elif choice == OPTION_REGISTER:
            acc_controller.member_registration()
        else:
            quit()

def member_menu(loggedInUser):
    book_controller = BookController(db, view, loggedInUser)
    cart_controller = CartController(db, loggedInUser)
    OPTION_SUBJECT = 1
    OPTION_SEARCH = 2
    OPTION_CHECKOUT = 3
    OPTION_LOGOUT = 4
    while(True):
        view.print_header("Member Menu")
        options = ["Browse by Subject", "Search by Author/Title", "Check out", "Logout"]
        view.print_options(options)
        choice = view.get_choice(len(options))
        
        if choice == OPTION_SUBJECT:
            book_controller.subject_menu()
        elif choice == OPTION_SEARCH:
            book_controller.search_menu()
        elif choice == OPTION_CHECKOUT:
            cart_controller.checkout()
        elif choice == OPTION_LOGOUT:
            break

main_menu(["Member Login", "New Member Registration", "Quit"])
