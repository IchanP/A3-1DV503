from model.database import Database
from view.ui import ui
from model.BookHandler import BookHandler
from model.CartHandler import CartHandler
from model.MemberHandler import MemberHandler
from mysql.connector.errors import ProgrammingError
from utils.pagination_util import handle_forward_pagination, handle_backwards_pagination

class BookController:

    def __init__(self, db: Database, view: ui, loggedInUser):
        self.db = db
        self.view = view
        self.book_handler = BookHandler(db)
        self.cart_handler = CartHandler(db)
        self.member_handler = MemberHandler(db)
        self.loggedInUser = loggedInUser

    def search_menu(self):
        while(True):
            self.view.print_header("Search Menu")

            OPTION_AUTHOR = 1
            OPTION_TITLE = 2
            OPTION_BACK = 3
            options = ["Author Search", "Title Search", "Exit"]
            self.view.print_options(options)

            choice = self.view.get_choice(len(options))

            if choice == OPTION_AUTHOR:
                self._books_by_author_menu()
            elif choice == OPTION_TITLE:
                self._books_by_title_menu()
            elif choice == OPTION_BACK:
                break

    def subject_menu(self):
        while(True):
            self.view.print_header("Subject Menu")
            
            subjects = self.book_handler.fetch_list_of_subjects()      
            subjects.insert(0, "Exit")
            self.view.print_options(subjects)

            subjectChoice = self.view.get_choice(len(subjects))
            subjectChoice -= 1
            
            if subjectChoice == 0:
                break
            
            self._books_by_subject_menu(subjects[subjectChoice])

    def _generic_books_menu(self, fetch_method, limit, input_message, attribute=None):
        offset = 0
        LIMIT = limit
        is_next_page = True
        search_value = self.view.get_input(input_message) if input_message else attribute
        while True:
            try:
                if is_next_page:
                    books = fetch_method(search_value, LIMIT + 1, offset)
                    is_next_page, books = self._handle_pagination(books, LIMIT)
                    self.view.print_list_of_dics(books)

                choice = self._handle_menu_options(["Enter ISBN to add to Cart", "View next page", "View Previous Page", "Back"])
                if choice == 1:
                    self._handle_purchase_by_isbn(books)
                elif choice == 2:
                    offset = handle_forward_pagination(self.view, offset, is_next_page, LIMIT)
                elif choice == 3:
                    offset = handle_backwards_pagination(self.view, offset, LIMIT)
                    is_next_page = True
                elif choice == 4:
                    break
            except Exception as e:
                self.view.print_error(f"An error occurred: {e}\nPlease try again.")

    def _books_by_author_menu(self):
        self._generic_books_menu(self.book_handler.book_fetch_by_author, 3, "Enter author:")

    def _books_by_title_menu(self):
        self._generic_books_menu(self.book_handler.book_fetch_by_title, 3, "Enter title:")

    def _books_by_subject_menu(self, subject):
        self._generic_books_menu(self.book_handler.book_fetch_by_subject, 50, None, subject)
    
    def _handle_purchase_by_isbn(self, books):
        isbn = self.view.get_input("Enter ISBN: ")
        if self._isIsbn(isbn, books):
            
            quanity = self.view.get_int_input("Enter quantity: ")
            userid = self.loggedInUser["UserID"]

            self._add_book_to_cart(userid, isbn, quanity)
        else:
            self.view.print_error("Invalid ISBN")

    def _isIsbn(self, isbn, books):  
        for book in books:
            if isbn == book["ISBN"]:
                return True
        return False   

    # TODO i assume this can throw different types of errors
    def _add_book_to_cart(self, userid, isbn, quantity):
        if self.cart_handler.add_book_to_cart(userid, isbn, quantity):
            print("Book successfully  added to cart")
        else: 
            self.view.print_error("Failed to add book to cart") 
    
    def _handle_pagination(self, books, limit):
        is_next_page = len(books) > limit
        return is_next_page, books[:limit] if is_next_page else books

    def _handle_menu_options(self, options_list):
        self.view.print_options(options_list)
        return self.view.get_choice(len(options_list))