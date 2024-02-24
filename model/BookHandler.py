from model.database import Database

class BookHandler:

    def fetch_list_of_subjects(self, db: Database):
        query = """SELECT subject FROM books GROUP BY subject"""
        subjects_tuple = db.execute_and_fetchall(query)
        subjects = []
        for genres in subjects_tuple:
            subjects.append(genres[0])
        return subjects

    def book_fetch_by_sbuject(self, subject, db: Database, limit, offset):
      query = """SELECT * FROM books WHERE subject = %s LIMIT %s OFFSET %s ;"""
      options_tuple = (subject, limit, offset)
      books_tuple = db.execute_and_fetchall(query, options_tuple)
    
      list_of_books = []
      for book in books_tuple:
        list_of_books.append(self._books_to_dictionary(book))
      return list_of_books

    
    def _books_to_dictionary(self, book_info):
        keys = ['ISBN', 'Author', 'Title', 'Price', 'Subject']
        return dict(zip(keys, book_info))