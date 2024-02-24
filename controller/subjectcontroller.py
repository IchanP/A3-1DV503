from model.database import Database
from view.ui import ui
from model.BookHandler import BookHandler

class SubjectController:

     def __init__(self, db: Database, view: ui):
        self.db = db
        self.view = view
        self.book_handler = BookHandler()

     def subject_menu(self):
        while(True):
            self.view.print_header("Subject Menu")
            
            subjects = self.book_handler.fetch_list_of_subjects(self.db)      
            subjects.insert(0, "Exit")
            self.view.print_options(subjects)

            subjectChoice = self.view.get_choice(len(subjects))
            subjectChoice -= 1
            
            self._books_by_subject_menu(subjects[subjectChoice])                    
    
     def books_by_subject_menu(self, books):
        while(True):
            self.view.print_header("Books by Subject")
            self.view.print_books(books)
            self.view.print_options(["Back to Subject Menu"])
            choice = self.view.get_choice(1)
            if choice == 1:
                break

     def _books_by_subject_menu(self, subject):
        offset = 0
        while(True):
           books = self.book_handler.book_fetch_by_sbuject(subject, self.db, 2, offset)
           for book in books:
                self.view.print_dictionary(book)
           
           options = ["Enter ISBN to add to Cart", "View next page", "View Previous Page", "Back to Subject Menu"]
           self.view.print_options(options)
            
           choice = self.view.get_choice(len(options))

           if choice == 2:
             offset += 2
           elif choice == 3:
             if offset-2 < 0:
                print("No previous page.")
           elif choice == 4:
             break
           else:
             if choice == book[0]["ISBN"] or choice == book[1]["ISBN"]:
                quantity = input("Quantity: ")
                # TODO add to cart
             else: 
                print("Invalid choice")
                input("Press any key to continue")

    