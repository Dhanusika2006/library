import os
FILE_NAME = "books.txt"
# Create file if not exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()
def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{author},Available\n")
print("Book added successfully ")
def view_books():
    with open(FILE_NAME, "r") as f:
        books = f.readlines()
    if not books:
        print("No books available")
        return

    print("\n Book List:")
    for i, book in enumerate(books, start=1):
        name, author, status = book.strip().split(",")
        print(f"{i}. {name} by {author} - {status}")


def search_book():
    keyword = input("Enter book name to search: ").lower()

    with open(FILE_NAME, "r") as f:
        found = False
        for book in f:
            name, author, status = book.strip().split(",")
            if keyword in name.lower():
                print(f"Found: {name} by {author} - {status}")
                found = True

        if not found:
            print("Book not found ")


def issue_book():
    book_name = input("Enter book name to issue: ").lower()
    updated_books = []

    with open(FILE_NAME, "r") as f:
        found = False
        for book in f:
            name, author, status = book.strip().split(",")

            if book_name == name.lower() and status == "Available":
                updated_books.append(f"{name},{author},Issued\n")
                print("Book issued successfully ")
                found = True
            else:
                updated_books.append(book)

    if not found:
        print("Book not available ")

    with open(FILE_NAME, "w") as f:
        f.writelines(updated_books)


def return_book():
    book_name = input("Enter book name to return: ").lower()
    updated_books = []

    with open(FILE_NAME, "r") as f:
        found = False
        for book in f:
            name, author, status = book.strip().split(",")

            if book_name == name.lower() and status == "Issued":
                updated_books.append(f"{name},{author},Available\n")
                print("Book returned successfully ")
                found = True
            else:
                updated_books.append(book)

    if not found:
        print("Book not found or not issued ")

    with open(FILE_NAME, "w") as f:
        f.writelines(updated_books)


def menu():
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you! ")
            break
        else:
            print("Invalid choice ")
menu()