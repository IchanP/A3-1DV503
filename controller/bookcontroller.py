from model.database import Database
from view.ui import ui
from model.BookHandler import BookHandler
from model.CartHandler import CartHandler
from model.MemberHandler import MemberHandler

class BookController:

    def __init__(self, db: Database, view: ui, loggedInUser):
        self.db = db
        self.view = view
        self.book_handler = BookHandler()
        self.cart_handler = CartHandler()
        self.member_handler = MemberHandler()
        self.loggedInUser = loggedInUser

    def subject_menu(self):
        while(True):
            self.view.print_header("Subject Menu")
            
            subjects = self.book_handler.fetch_list_of_subjects(self.db)      
            subjects.insert(0, "Exit")
            self.view.print_options(subjects)

            subjectChoice = self.view.get_choice(len(subjects))
            subjectChoice -= 1
            
            if subjectChoice == 0:
                break
            
            self._books_by_subject_menu(subjects[subjectChoice])                  

    def _books_by_subject_menu(self, subject):
        offset = 0
        while(True):
            books = self.book_handler.book_fetch_by_sbuject(subject, self.db, 2, offset)
            for book in books:
                self.view.print_dictionary(book)

            options = ["Enter ISBN to add to Cart", "View next page", "View Previous Page", "Back to Subject Menu"]
            self.view.print_options(options)

            choice = self.view.get_choice(len(options))

            if choice == 1:
                self._handle_purchase_by_isbn(books)
            if choice == 2:
                offset = self._increase_offset(offset)
            elif choice == 3:
                offset = self._reduce_offset(offset)
            elif choice == 4:
                break
    
    def _handle_purchase_by_isbn(self, books):
        isbn = self.view.get_input("Enter ISBN: ")
        if self._isIsbn(isbn, books):
            quanity = self._try_get_quantity()
            userid = self.member_handler.get_id_by_email(self.db, self.loggedInUser)
            self.cart_handler.add_book_to_cart(self.db, userid, isbn, quanity)
        else:
            print("Invalid choice")
            input("Press any key to continue")
  
    def _try_get_quantity(self):
        try:
            quantity = int(self.view.get_input("Enter quantity: "))
            return quantity
        except Exception as e:
            if isinstance(e, ValueError) or isinstance(e, TypeError):
                print("Please enter only numbers.")
                return self._try_get_quantity()

    def _increase_offset(self, offset):
        return offset+2

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
    