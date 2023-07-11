class Borrower:
    def __init__(self, borrower_id, name, contact_number):
        self.borrower_id = borrower_id
        self.name = name
        self.contact_number = contact_number

    def add_borrower(self):
        borrower_data = f"{self.borrower_id},{self.name},{self.contact_number}\n"
        with open("borrower_data.csv", "a") as file:
            file.write(borrower_data)
        print("Borrower added successfully!")

    def search_borrower_by_borrower_id(self, borrower_id):
        found = False
        with open("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split(",")
                if borrower_info[0] == borrower_id:
                    print("Borrower Found")
                    print("ID:", borrower_info[0])
                    print("Name:", borrower_info[1])
                    print("Contact Number:", borrower_info[2])
                    found = True
                    break
        if not found:
            print("Borrower not found")

    def update_borrower(self, borrower_id, updated_data):
        found = False
        with open("borrower_data.csv", "r") as file:
            lines = file.readlines()

        with open("borrower_data.csv", "w") as file:
            for line in lines:
                borrower_info = line.strip().split(",")
                if borrower_info[0] == borrower_id:
                    updated_line = f"{borrower_id},{updated_data['name']},{updated_data['contact_number']}\n"
                    file.write(updated_line)
                    print("Borrower updated successfully")
                    found = True
                else:
                    file.write(line)

        if not found:
            print("Borrower not found")
