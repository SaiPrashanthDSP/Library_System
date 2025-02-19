# usage1.py

from Library_System import Library, FictionBook, NonFictionBook, Student, Teacher

def main():
    library = Library()

    # Adding books
    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "123456789", "Classic")
    book2 = NonFictionBook("Sapiens", "Yuval Noah Harari", "987654321", "History")
    library.add_book(book1)
    library.add_book(book2)

    # Registering members
    member1 = Student("Alice", "S001", "alice@example.com", "10th Grade")
    member2 = Teacher("Mr. Smith", "T001", "smith@example.com", "Mathematics")
    library.register_member(member1)
    library.register_member(member2)

    # Listing books and members
    library.list_books()
    library.list_members()

if __name__ == "__main__":
    main()