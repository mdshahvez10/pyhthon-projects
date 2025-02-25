# -*- coding: utf-8 -*-
"""projectfilehandletxt.ipynb"""

user_details = {
    "shahvez": "3456789",
    "user1": "123456",
}
registered_users = list(user_details.keys())

books = [
    {"id": "00AW", "title": "Wings of Fire", "author": "Abdul Kalam", "price": 214.99},
    {"id": "01IM", "title": "Ignited Minds", "author": "Abdul Kalam", "price": 213.50},
    {"id": "02IV", "title": "India 2020: A Vision for the New Millennium", "author": "Abdul Kalam", "price": 212.75},
    {"id": "03MJ", "title": "My Journey: Transforming Dreams into Actions", "author": "Abdul Kalam", "price": 215.25},
    {"id": "04IM", "title": "The Immortals of Meluha", "author": "Amish Tripathi", "price": 314.99},
    {"id": "05SN", "title": "The Secret of the Nagas", "author": "Amish Tripathi", "price": 313.50},
    {"id": "06OV", "title": "The Oath of the Vayuputras", "author": "Amish Tripathi", "price": 312.75},
    {"id": "07SI", "title": "Scion of Ikshvaku", "author": "Amish Tripathi", "price": 315.25},
    {"id": "08SB", "title": "A Suitable Boy", "author": "Vikram Seth", "price": 215.50},
    {"id": "09MC", "title": "Midnight's Children", "author": "Salman Rushdie", "price": 514.75},
    {"id": "10WT", "title": "The White Tiger", "author": "Aravind Adiga", "price": 311.25},
    {"id": "11TG", "title": "The Guide", "author": "R.K. Narayan", "price": 510.99},
    {"id": "12TP", "title": "Train to Pakistan", "author": "Khushwant Singh", "price": 193.80},
    {"id": "13PC", "title": "Python Crash Course", "author": "Eric Matthes", "price": 225.00},
    {"id": "14IA", "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "price": 445.00},
    {"id": "15HD", "title": "Head First Design Patterns", "author": "Eric Freeman", "price": 340.00},
    {"id": "16JG", "title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "price": 520.00}
]

file_path = "books_data.txt"
with open(file_path, "w") as file:
    for book in books:
        file.write(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}\n")
print(f"Data successfully written to '{file_path}'")

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in user_details and user_details[username] == password:
            print(f"login successful! welcome, {username}.")
            return username
        else:
            print("invalid username or password. please try again.")

def register_user():
    while True:
        new_username = input("enter new username: ")

        if new_username in user_details:
            print("username already exists. please choose a different username.")
        else:
            new_password = input("enter password for the new user: ")
            user_details[new_username] = new_password
            registered_users.append(new_username)
            print(f"user '{new_username}' registered successfully!")
            return new_username

def display():
  with open(file_path, "r") as f:
    reader = f.readlines()
    print("Content of books_data.txt:/n")
    for line in reader:
      print(line.strip())

def display_books_by_author():
  author_name = input("Enter the author's name to display books: ")
  with open(file_path, "r") as f:
    reader = f.readlines()

    book_found = False
    for data in reader:
      book_detail = data.strip().split(", ")
      ar = book_detail[2].split(": ")[1]
      if ar.lower() == author_name.lower():
        print("Books by", author_name, ":")
        print(data.strip())
        found_books = True

    if not found_books:
      print(f"No books found by the author '{author_name}'.")

def display_books_by_author():
    author_name = input("Enter the author's name to display books: ")
    found_books = False  # Initialize found_books to track if any books were found

    with open(file_path, "r") as f:
        reader = f.readlines()

        for data in reader:
            book_detail = data.strip().split(", ")
            ar = book_detail[2].split(": ")[1]

            if ar.lower() == author_name.lower():
                print("Books by", author_name, ":")
                print(data.strip())
                found_books = True

    if not found_books:
        print(f"No books found by the author '{author_name}'.")

def add_new_book():
    with open(file_path, "a") as f:
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        price = float(input("Enter book price: "))

        f.write(f"{book_id}\t{title}\t{author}\t{price}\n")
        print("Book details added successfully.")



def issue_book():
    book_id = input("Enter the book ID you want to issue: ")

    all_lines = []
    record_updated = False

    with open(file_path, "r") as f:
        all_lines = f.readlines()

    with open(file_path, "w") as f:
        for line in all_lines:
            details = line.strip().split("\t")
            if details[0] == book_id:
                if details[-1].strip().lower() != 'issued':
                    details[-1] = 'issued'
                    updated_line = "\t".join(details) + "\n"
                    f.write(updated_line)
                    print(f"Book '{details[1]}' has been issued.")
                    record_updated = True
                else:
                    print(f"Book '{details[1]}' is already issued.")
            else:
                f.write(line)

        if not record_updated:
            print(f"No record found with ID '{book_id}'.")

def issue_book():
  book_id = input("Enter the book ID you want to issue: ")

  with open(file_path, "r") as f:
    all = f.readlines()

  with open(file_path, "w") as f:
    record_updated = False

    for i in all:
      details = i.strip().split("\t")

      if details[0] == book_id:
        if details[-1].strip().lower() != 'issued':
          details[-1] = 'issued'
          up_line = "\t".join(details) + "\n"
          f.write(up_line)
          print(f"Book '{details[1]}' has been issued.")
          record_updated = True
        else:
          print(f"Book '{details[1]}' is already issued.")
      else:
        f.write(i)

      if not record_updated:
        print(f"No record found with ID '{book_id}'.")

def return_book():
    book_id = input("Enter the book ID to return: ")
    book_returned = False

    all_lines = []
    with open(file_path, "r") as f:
        all_lines = f.readlines()

    with open(file_path, "w") as f:
        for line in all_lines:
            details = line.strip().split("\t")
            if details[0] == book_id:
                if details[-1].strip().lower() == 'issued':
                    details[-1] = 'available'
                    updated_line = "\t".join(details) + "\n"
                    f.write(updated_line)
                    book_returned = True
                    print(f"Book with ID {book_id} has been successfully returned.")
                else:
                    print(f"Book with ID {book_id} is not currently issued.")
            else:
                f.write(line)

    if not book_returned:
        print(f"No book found with ID {book_id}.")

def logout(username):
    print(f"logging out {username}...")
    print("logout successful")

def main_menu():
    current_user = None

    while True:
        print("\n********** E-Library Management System **********")
        try:
            if not current_user:
                print("1. Login")
                print("2. Register a new user")
            else:
                print(f"logged in as: {current_user}")
                print("3. display all books")
                print("4. list books by author (title and price)")
                print("5. add a book")
                print("6. issue a book")
                print("7. return a book")
                print("8. logout")

            choice = input("enter your choice: ")

            if not current_user:
                if choice == '1':
                    current_user = login()
                elif choice == '2':
                    current_user = register_user()
                else:
                    print("invalid choice. please try again.")
            else:
                if choice == '3':
                    display()
                elif choice == '4':
                  display_books_by_author()
                elif choice == '5':

                  add_new_book()
                elif choice == '6':
                  display()
                  issue_book()
                elif choice == '7':
                  display()
                  return_book()
                elif choice == '8':
                    print(f"logging out {current_user}...")
                    current_user = None
                else:
                    print("invalid choice. please try again.")
        except Exception:
            print("an error occurred.")

        if current_user is None:
            break

main_menu()


