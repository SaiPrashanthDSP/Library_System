# usage2.py

from Library_System import Library, FictionBook, Student

def main():
    library = Library()

    # Adding books
    book1 = FictionBook("1984", "George Orwell", "111111111", "Dystopian")
    library.add_book(book1)

    # Registering a member
    member1 = Student("Bob", "S002", "bob@example.com", "11th Grade")
    library.register_member(member1)

    # Loaning a book
    library.loan_book("111111111", "S002")  # Successful loan
    library.loan_book("111111111", "S002")  # Attempting to loan again

    # Listing books to check availability
    library.list_books()

if __name__ == "__main__":
    main()