# --- Step 1: Create a Book Class ---
class Book:
    # The __init__ method is the constructor used to initialize new object instances
    def __init__(self, name, author, release_date):
        # Storing the passed parameters as instance attributes
        self.name = name
        self.author = author
        self.release_date = release_date
        # A boolean attribute tracking whether the book has been read, defaulting to False
        self.read = False


# --- Step 2: Create a BookCollection Class ---
class BookCollection:
    def __init__(self, books=None):
        # Defaulting to an empty list if no book list is provided
        if books is None:
            self.books = []
        else:
            # Type verification: Ensure every item in the provided list is a Book instance
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError(
                        "All elements in the initial list must be instances of the Book class."
                    )
            self.books = books

    # --- Step 3: Add Books to the Collection ---
    def add_book(self, book):
        # Defensive programming: check if the incoming argument is explicitly a Book object
        if not isinstance(book, Book):
            raise TypeError(
                "Only instances of the Book class can be added to this collection."
            )
        self.books.append(book)

    # --- Step 4: Mark Books as Read ---
    def mark_as_read(self, book_name):
        # Iterating through the collection to find a book with a matching name attribute
        for book in self.books:
            if book.name == book_name:
                book.read = True
                print(f"Successfully marked '{book_name}' as read.")
                return  # Exit the method early once found and updated

        # This executes only if the loop completes without hitting the return statement
        print(f"Notice: The book '{book_name}' is not in the collection.")

    # --- Step 5: Display Collection Status ---
    def list_books(self):
        if not self.books:
            print("The collection is currently empty.")
            return

        print("--- Book Collection ---")
        for book in self.books:
            # Using a ternary operator to format the boolean status into readable text
            status = "Read" if book.read else "Unread"
            print(
                f"Title: {book.name} | Author: {book.author} | Released: {book.release_date} | Status: {status}"
            )


# --- Optional: Example Usage / Testing the Classes ---
# Creating instances of the Book class
book1 = Book("The Hobbit", "J.R.R. Tolkien", "1937")
book2 = Book("1984", "George Orwell", "1949")

# Initializing a collection with an existing list of books
my_library = BookCollection([book1, book2])

# Adding a new book using the add_book method
book3 = Book("To Kill a Mockingbird", "Harper Lee", "1960")
my_library.add_book(book3)

# Listing the collection before modifying read status
my_library.list_books()

# Updating a book's read status
my_library.mark_as_read("1984")

# Listing the collection again to verify the status updates
my_library.list_books()
