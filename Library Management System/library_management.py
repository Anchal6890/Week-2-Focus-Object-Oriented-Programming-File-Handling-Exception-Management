import json

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = {"title": title, "author": author, "issued": False}
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' by {author} added successfully.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nBooks available in the library:")
        for i, book in enumerate(self.books, 1):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i}. {book['title']} by {book['author']} [{status}]")

    def search_book(self):
        title = input("Enter book title to search: ")
        found = False
        for book in self.books:
            if book["title"].lower() == title.lower():
                status = "Issued" if book["issued"] else "Available"
                print(f"Book Found: {book['title']} by {book['author']} [{status}]")
                found = True
                break
        if not found:
            print("Book not found.")

    def issue_book(self):
        title = input("Enter book title to issue: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["issued"]:
                    print("Book is already issued.")
                else:
                    book["issued"] = True
                    self.save_books()
                    print(f"Book '{title}' has been issued.")
                return
        print("Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                if not book["issued"]:
                    print("Book was not issued.")
                else:
                    book["issued"] = False
                    self.save_books()
                    print(f"Book '{title}' has been returned.")
                return
        print("Book not found.")

    def menu(self):
        while True:
            print("\n====== Library Menu ======")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.view_books()
            elif choice == 3:
                self.search_book()
            elif choice == 4:
                self.issue_book()
            elif choice == 5:
                self.return_book()
            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Library System
if __name__ == "__main__":
    lib = Library()
    lib.menu()
