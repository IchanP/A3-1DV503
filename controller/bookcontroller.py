from model.database import Database
from view.ui import ui
from model.BookHandler import BookHandler
from model.CartHandler import CartHandler
from model.MemberHandler import MemberHandler
from mysql.connector.errors import ProgrammingError

class BookController:

    def __init__(self, db: Database, view: ui, loggedInUser):
        self.db = db
        self.view = view
        self.book_handler = BookHandler(db)
        self.cart_handler = CartHandler(db)
        self.member_handler = MemberHandler(db)
        self.loggedInUser = loggedInUser

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

# TODO Fix this garbage LOL
    def _books_by_subject_menu(self, subject):
        offset = 0
        max_offset = None
        while(True):
            try:
                books = self.book_handler.book_fetch_by_sbuject(subject, 2, offset)
                self._print_books(books)
                # TODO figure out how to deal with next empty pagination.
                
                OPTION_ISBN = 1
                OPTION_NEXT = 2
                OPTION_PREV = 3
                OPTION_BACK = 4
                options = ["Enter ISBN to add to Cart", "View next page", "View Previous Page", "Back to Subject Menu"]
                self.view.print_options(options)

                choice = self.view.get_choice(len(options))

                if choice == OPTION_ISBN:
                    self._handle_purchase_by_isbn(books)
                if choice == OPTION_NEXT and is_next_page:
                    offset, max_offset = self._handle_pagination(offset, max_offset, is_next_page)
                elif choice == OPTION_PREV:
                    offset = self._reduce_offset(offset)
                elif choice == OPTION_BACK:
                    break

            # TODO not sure how to handle programmingerror
            except ProgrammingError as e:
                self.view.print_error(f"An error occurred: {e}\nPlease try again.")
                continue
    
    def _handle_purchase_by_isbn(self, books):
        isbn = self.view.get_input("Enter ISBN: ")
        if self._isIsbn(isbn, books):
            quanity = self.view.get_int_input("Enter quantity: ")
            userid = self.member_handler.get_id_by_email(self.loggedInUser)
            self._add_book_to_cart(userid, isbn, quanity)
        else:
            self.view.print_error("Invalid ISBN")


    def handle_pagination(self, offset, max_offset, is_next_page):
        if is_next_page:
            return offset + 2, None  # 
        else:
            self.view.print_header("No next page")
            return offset, offset  

    def increase_offset(self, offset):
        return offset+200

    def reduce_offset(self, offset):
        if offset-2 < 0:
            self.view.print_header("No Previous Page")
            return 0
        else:
            return offset-2

    def _isIsbn(self, isbn, books):  
        for book in books:
            if isbn == book["ISBN"]:
                return True
        return False
    
    def _print_books(self, books, ):
        if books:
            for book in books:
              self.view.print_dictionary(book)
    

    # TODO i assume this can throw different types of errors
    def _add_book_to_cart(self, userid, isbn, quantity):
        if self.cart_handler.add_book_to_cart(userid, isbn, quantity):
            print("Book successfully  added to cart")
        else: 
            self.view.print_error("Failed to add book to cart") # TODO but why?