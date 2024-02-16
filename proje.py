import tempfile
import shutil

class Library:
    #constructor method 
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "a+")

    #destructor method
    def __del__(self):
        self.file.close()

    #this method will list all the books in the file
    def list_books(self):
        self.file.seek(0)
        contents = self.file.read()
        lines = contents.splitlines()
        for line in lines:
            line = line.strip()
            words = line.split(",")
            book_name = words[0].strip().capitalize()
            author = words[1].strip().capitalize()
            print("Book Name:", book_name, ",", "Author:", author)

    #This method adds the books entered by the user
    def add_books(self):
        while True:
            
            book_title = input("Please enter the book title (type 'q' to quit): ")
            if book_title.lower() == 'q':
                break

            if not book_title.strip():  #empty input control
                print("Book title cannot be empty.")
                continue
            
            while True:
                 book_author = input("Enter the author of the book: ")
                 if any(char.isdigit() for char in book_author):
                    print("Author's name cannot contain numbers.")
                 elif any(char.isalpha() for char in book_author):
                    break
                 else:
                    print("Author's name cannot be empty.")
           
                    
            while True:
                release_year = input("In which year was it published?: ")
                try:
                    release_year = int(release_year)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number.")
                 
            while True:
               number_of_pages = input("How many pages?: ")
               try:
                number_of_pages = int(number_of_pages)
                break
               except ValueError:
                print("This is not a number. Please enter a valid number.")


            book_information = f"{book_title.capitalize()}, {book_author.capitalize()}, {release_year}, {number_of_pages}\n"

            with open(self.filename, "a") as file:
                file.write(book_information)

            print("Book information has been successfully added.")

    #This method deletes the books entered by the user
    def remove_book(self):
        while True:
            book_title = input("Please enter the title of the book to remove (type 'q' to quit): ")
            if book_title.lower() == 'q':
                break

            removed_book = False
            book_title = book_title.capitalize()

            #Generate a temporary file name
            temp_filename = tempfile.mktemp()  

            with open(temp_filename, "w") as temp_file:
                with open(self.filename, "r") as file:
                    for line in file:
                        words = line.strip().split(",")
                        current_book_name = words[0].strip().capitalize()
                        if book_title != current_book_name:
                            temp_file.write(line)
                        else:
                            removed_book = True

            shutil.copy(temp_filename, self.filename)

            if removed_book:
                print(f"The book '{book_title}' has been successfully removed.")
            else:
                print("Book not found.")

    #Print menu
    def menu(self):
        while True:
            print("""
                     ***MENU***
                     1. List Books
                     2. Add Book
                     3. Remove Book
                     4. Exit
            """)

            user_choice = input("Choose an action (1-4): ")
            if user_choice == "1":
                self.list_books()
            elif user_choice == "2":
                self.add_books()
            elif user_choice == "3":
                self.remove_book()
            elif user_choice == "4":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

library = Library("books.txt")
library.menu()
