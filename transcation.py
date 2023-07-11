import csv
class Transaction ():
    def __init__(self, transaction_id, book_id, borrower_id, borrow_date, return_date=None):
        self.transaction_id = transaction_id
        self.book_id = book_id
        self.borrower_id = borrower_id
        self.borrow_date = borrow_date
        self.return_date = return_date
#Record the transaction in csv file
    def record_transaction (self):
        transaction_data= [self.transaction_id, self.book_id, self.borrower_id, self.borrow_date, self.return_date]
        with open('transaction_data.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow (transaction_data)
            print("Book Borrow Success")
            #After borrow success, decrease quantity in book data
            #Decrease quantity in book_data.csv by 1
        with open ('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[2] == self.book_id:
                if int(row[4]) > 0:
                    row[4] = str(int(row[4]) -1)
                    break

        with open ('book_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            #print ("Number update successfully")

    def return_book(self):
        with open('transaction_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if len(row) >= 5 and row[1] == self.book_id and row[4] is None:
                row[4] = self.get_current_date()  # Set the return_date to the current date
            break


        with open('transaction_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[0] == self.book_id:
                row[4] = str(int(row[4]) + 1)  # Increase the quantity by 1
                break

        with open('book_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Book returned successfully.")

    def extend_loan(self, days):
        # Open the transaction_data.csv file in read mode
        with open('transaction_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if len(row) >= 5 and row[1] == self.book_id and row[4] is None:
            
                from datetime import datetime, timedelta
                borrow_date = datetime.strptime(row[3], "%Y-%m-%d")
                extended_borrow_date = borrow_date + timedelta(days=days)
                row[3] = extended_borrow_date.strftime("%Y-%m-%d")
                break
        with open('transaction_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Loan extended successfully.")