from model.database import Database

class BookHandler:

    def __init__(self, db: Database):
        self.db = db

    def fetch_list_of_subjects(self):
        query = """SELECT subject FROM books GROUP BY subject ORDER BY subject ASC"""
        subjects_tuple = self.db.execute_and_fetchall(query)
        subjects = []
        for genres in subjects_tuple:
            subjects.append(genres[0])
        return subjects

    def book_fetch_by_subject(self, subject, limit, offset):
      query = """SELECT * FROM books WHERE subject = %s LIMIT %s OFFSET %s ;"""
      options_tuple = (subject, limit, offset)
      books_tuple = self.db.execute_and_fetchall(query, options_tuple)
    
      return self._tuple_to_list(books_tuple)

    def book_fetch_by_author(self, author, limit, offset):
      query = """SELECT * from books WHERE author like %s LIMIT %s OFFSET %s ;"""
      options_tuple = (f"%{author}%", limit, offset)
      books_tuple = self.db.execute_and_fetchall(query, options_tuple)

      return self._tuple_to_list(books_tuple)
    
    def book_fetch_by_title(self, title, limit, offset):
      query = """SELECT * from books WHERE title like %s LIMIT %s OFFSET %s ;"""
      options_tuple = (f"%{title}%", limit, offset)
      books_tuple = self.db.execute_and_fetchall(query, options_tuple)

      return self._tuple_to_list(books_tuple)

    def _tuple_to_list(self, tuple):
      list_of_books = []
      for book in tuple:
        list_of_books.append(self._books_to_dictionary(book))
      return list_of_books

    def _books_to_dictionary(self, book_info):
        keys = ['ISBN', 'Author', 'Title', 'Price', 'Subject']
        return dict(zip(keys, book_info))