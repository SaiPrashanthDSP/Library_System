
# Book Class (Base Class)
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availabilityStatus = "Available"
        self.loanedId = None


# FictionBook Class (Derived  Class)
class FictionBook(Book):
    def __init__(self, title, author, ISBN, genre):
        Book.__init__(self, title, author, ISBN)
        self.genre = genre


# NonFictionBook Class (Derived  Class)
class NonFictionBook(Book):
    def __init__(self, title, author, ISBN, subject):
        Book.__init__(self, title, author, ISBN)
        self.subject = subject


# Member Class (Base  Class)
class Member:
    def __init__(self, name, memberId, email):
        self.name = name
        self.memberId = memberId
        self.email = email


# Student Class (Derived  Class)
class Student(Member):
    def __init__(self, name, memberId, email, grade):
        Member.__init__(self, name, memberId, email)
        self.grade = grade


# Teacher Class (Derived  Class)
class Teacher(Member):
    def __init__(self, name, memberId, email, subject):
        Member.__init__(self, name, memberId, email)
        self.subject = subject


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.registered_members = []

    # Function to add book
    def add_book(self, book):
        self.books.append(book)
        if isinstance(book, FictionBook):
            print(f"Added: {book.title} "
                  f"by {book.author} (ISBN: {book.ISBN}) - {book.availabilityStatus} - "
                  f"Genre: {book.genre}")
        else:
            print(f"Added: {book.title} "
                  f"by {book.author} (ISBN: {book.ISBN}) - {book.availabilityStatus} - "
                  f"Subject: {book.subject}")

    # Function to register member
    def register_member(self, member):
        self.registered_members.append(member)
        if isinstance(member, Student):
            print(f"Registered: {member.name} (ID: {member.memberId}, "
                  f"Email: {member.email}) - Grade: {member.grade}")
        else:
            print(f"Registered: {member.name} (ID: {member.memberId}, "
                  f"Email: {member.email}) - Subject: {member.subject}")

    # Function to list the books
    def list_books(self):
        print("Books in Library:")
        for book in self.books:
            if isinstance(book, FictionBook):
                print(f"{book.title} "
                      f"by {book.author} (ISBN: {book.ISBN}) - {book.availabilityStatus} - "
                      f"Genre: {book.genre}")
            else:
                print(f"{book.title} "
                      f"by {book.author} (ISBN: {book.ISBN}) - {book.availabilityStatus} - "
                      f"Subject: {book.subject}")

    # Function to list the members
    def list_members(self):
        print("Registered Members:")
        for member in self.registered_members:
            if isinstance(member, Student):
                print(f"{member.name} (ID: {member.memberId}, "
                      f"Email: {member.email}) - Grade: {member.grade}")
            else:
                print(f"{member.name} (ID: {member.memberId}, "
                      f"Email: {member.email}) - Subject: {member.subject}")

    # Function to loan a book to student and check for availability
    def loan_book(self, ISBN, student_id):

        bookExist = [book for book in self.books if book.ISBN == ISBN]
        if len(bookExist) and bookExist[0].availabilityStatus == "Available":
            bookExist[0].availabilityStatus = "Checked Out"
            bookExist[0].loanedId = student_id
            print(f"Book {bookExist[0].title} loaned to member ID: {student_id}")
        else:
            print(f"Book {bookExist[0].title} is currently checked out.")

    # Function to change the availability status of returned book
    def return_book(self, ISBN):
        bookExist = [book for book in self.books if book.ISBN == ISBN]
        if len(bookExist) and bookExist[0].availabilityStatus == "Checked Out":
            bookExist[0].availabilityStatus = "Available"
            bookExist[0].loanedId = None
            print(f"Book {bookExist[0].title} returned to the library.")
        else:
            print(f"Book {bookExist[0].title}  not exist")
