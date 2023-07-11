import csv
from books import Book
from borrowers import Borrower
from transcation import Transaction

def selection_validate():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To request a new loan enter 1 \n"
                          "To return a book enter 2 \n"
                          "To extend a loan enter 3 \n"
                          "To add a user enter 4 \n"
                          "To update a user enter 5 \n"
                          "To add a book enter 6 \n"
                          "\nEnter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'
            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection
def selection_calls():
    selection = selection_validate()
    if selection == '1':
        transaction_id = input("Enter Transaction ID: ")
        book_id = input("Enter Book ID: ")
        borrower_id = input("Enter Borrower ID: ")
        borrow_date = input("Enter Borrow Date: ")
        new_transaction = Transaction(transaction_id, book_id, borrower_id, borrow_date)
        new_transaction.record_transaction()
    elif selection == '2':
        transaction_id = input("Enter Transaction ID: ")
        book_id = input("Enter Book ID: ")
        borrower_id = input("Enter Borrower ID: ")
        return_date = input("Enter Return Date: ")  
        new_transaction = Transaction(transaction_id, book_id, borrower_id, "", return_date) 
        new_transaction.return_book()  
    elif selection == '3':
        transaction_id = input("Enter Transaction ID: ")
        book_id = input("Enter Book ID: ")
        borrower_id = input("Enter Borrower ID: ")
        borrow_date = input("Enter Borrow Date: ")
        new_transaction = Transaction(transaction_id, book_id, borrower_id, borrow_date)
        new_transaction.record_transaction()
        days_to_extend = int(input("Enter the number of days to extend the loan: "))
        new_transaction.extend_loan(days_to_extend)
    elif selection == '4':
        borrower_id = input("Enter Borrower ID: ")
        name = input("Enter Name: ")
        contact_number = input("Enter Contact Number: ")
        new_borrower = Borrower(borrower_id=borrower_id, name=name, contact_number=contact_number)
        new_borrower.add_borrower()
    elif selection == '5':
        borrower_id = input("Enter Borrower ID: ")
        updated_name = input("Enter Updated Name: ")
        updated_contact_number = input("Enter Updated Contact Number: ")
        borrower = Borrower(borrower_id, updated_name, updated_contact_number)
        updated_data = {'name': updated_name, 'contact_number': updated_contact_number}
        borrower.update_borrower(borrower_id, updated_data)
        
    elif selection == '6':
        book_name = input("Enter Book Name: ")
        title = input("Enter Title: ")
        author = input("Enter author: ")
        quantity = input("Enter quantity: ")
        pub_year = input("Enter Publication Year: ")
        edition = input("Enter Edition: ")
        book_id = input("Enter Book Id: ")
        new_book = Book(book_id=book_id, book_name=book_name, title=title, author=author, quantity=quantity, pub_year=pub_year, edition=edition)

        new_book.add_book()
        transaction_id = input("Enter Transaction ID: ")
        borrower_id = input("Enter Borrower ID: ")
        borrow_date = input("Enter Borrow Date: ")
        new_transaction = Transaction(transaction_id, book_id, borrower_id, borrow_date)
        new_transaction.record_transaction()

if __name__ == '__main__':
    selection_calls()