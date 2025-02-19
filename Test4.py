# usage4.py

from Library_System import Library, FictionBook, NonFictionBook, Student, Teacher

def main():
    library = Library()

    # Adding multiple books
    book1 = FictionBook("The Catcher in the Rye", "J.D. Salinger", "333333333", "Classic")
    book2 = NonFictionBook("Educated", "Tara Westover", "444444444", "Memoir")
    book3 = FictionBook("The Hobbit", "J.R.R. Tolkien", "555555555", "Fantasy")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Registering multiple members
    member1 = Student("Dave", "S004", "dave@example.com", "9th Grade")
    member2 = Teacher("Ms. Johnson", "T002", "johnson@example.com", "English")
    library.register_member(member1)
    library.register_member(member2)

    # Loaning books to members
    library.loan_book("333333333", "S004")  # Loaning to Dave
    library.loan_book("444444444", "T002")  # Loaning to Ms. Johnson
    library.loan_book("555555555", "S004")  # Dave tries to loan another book

    # Listing books to check availability
    library.list_books()

    # Returning a book
    library.return_book("333333333")

    # Listing books again to check updated availability
    library.list_books()

if __name__ == "__main__":
    main()