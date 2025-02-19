# usage3.py

from Library_System import Library, FictionBook, Student

def main():
    library = Library()

    # Adding books
    book1 = FictionBook("To Kill a Mockingbird", "Harper Lee", "222222222", "Classic")
    library.add_book(book1)

    # Registering a member
    member1 = Student("Charlie", "S003", "charlie@example.com", "12th Grade")
    library.register_member(member1)

    # Loaning a book
    library.loan_book("222222222", "S003")

    # Returning a book
    library.return_book("222222222")

    # Listing books to check availability
    library.list_books()

if __name__ == "__main__":
    main()