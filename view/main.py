from control.mainfile import MainFile
from model.client_file import Client
from model.Librarian_file import Librarian
from model.BorrowingOrder_file import BorrowingOrder
from model.Book_file import Book

main_file = MainFile()#instance
while True:
    # 0. Ask user to enter as a client or librarian
    user_type = input("Enter 'client' or 'librarian' else write exit:")
    if user_type == 'exit':
        break
    if user_type == 'client':
        client_id = input("Enter the client's ID: ")
        client_name = input("Enter the client's name: ")
        client_age = input("Enter the client's age: ")
        client_id_no = input("Enter the client's ID number: ")
        client_phone = input("Enter the client's phone number: ")
        main_file.add_client(client_id, client_name, client_age, client_id_no, client_phone)
        print("Client added to the system.")

        # 4. Show all books on system, then ask Librarian to borrow a book
        print("All Books: ")
        for book in main_file.books_list:
            print(book.title)
