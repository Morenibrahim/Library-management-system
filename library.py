import sqlite3

def create_connection():
  connection = sqlite3.connect("library.db")
  return connection

def create_table(connection):
  cursor = connection.cursor()
  cursor.execute("""CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    status TEXT
  )""")

def add_book(connection, title, author, status):
  cursor = connection.cursor()
  cursor.execute("INSERT INTO books (title, author, status) VALUES (?, ?, ?)", (title, author, status))
  connection.commit()

def get_all_books(connection):
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM books")
  books = cursor.fetchall()
  return books

def main():
  connection = create_connection()
  create_table(connection)
  add_book(connection, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Available")
  add_book(connection, "The Lord of the Rings", "J.R.R. Tolkien", "Available")
  books = get_all_books(connection)
  for book in books:
    print(book)

if __name__ == "__main__":
  main()
