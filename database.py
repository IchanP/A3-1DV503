from mysql.connector import connect

class Database:

    # establish connection to the db
    # THis __init__ method is called when the class is instantiated
    def __init__(self, username, password) -> None:
        self.connection = connect(host="localhost", user=username, password=password, database="company") # TODO fix the database name

    #get the cursor
    def get_cursor(self):
        return self.connection.cursor()
    
    def execute_and_fetchall(self, query):
        with self.get_cursor() as cursor: # Using with statement to automatically close the cursor
            cursor.execute(query)
            return cursor.fetchall()
    
    #execute with commit
    def execute_with_commit(self, query):
        with self.get_cursor() as cursor: # Using with statement to automatically close the cursor
            cursor.execute(query)
            self.connection.commit()