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
                is_next_page = self._check_for_next_page(books)

                options = ["Enter ISBN to add to Cart", "View next page", "View Previous Page", "Back to Subject Menu"]
                self.view.print_options(options)

                choice = self.view.get_choice(len(options))

                if choice == 1:
                    self._handle_purchase_by_isbn(books)
                if choice == 2:
                    if is_next_page and max_offset != offset:
                        offset = self._increase_offset(offset)
                    else:
                        print("\n---------------------------")
                        print("      No next page")
                        print("---------------------------")
                        max_offset = offset
                elif choice == 3:
                    offset = self._reduce_offset(offset)
                elif choice == 4:
                    break
            except ProgrammingError as e:
                print("An error occurred")
                print(e)
                input("Press any key to continue")
                break
    
    def _handle_purchase_by_isbn(self, books):
        isbn = self.view.get_input("Enter ISBN: ")
        if self._isIsbn(isbn, books):
            quanity = self.view.get_int_input("Enter quantity: ")
            userid = self.member_handler.get_id_by_email(self.loggedInUser)
            if self.cart_handler.add_book_to_cart(userid, isbn, quanity):
                print("Book successfully  added to cart")
                input("Press any key to continue")
        else:
            print("Invalid choice")
            input("Press any key to continue")
  

    def _increase_offset(self, offset):
        return offset+200

    def _reduce_offset(self, offset):
        if offset-2 < 0:
            print("\n---------------------------")
            print("     No previous page.")
            print("---------------------------")
            return offset
        else:
            return offset-2

    def _isIsbn(self, isbn, books):  
        for book in books:
            if isbn == book["ISBN"]:
                return True
        return False
    
    def _check_for_next_page(self, books):
        if books:
            for book in books:
              self.view.print_dictionary(book)
            return True
        else:
            return False