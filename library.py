import json
import os

data_file = 'library.txt'

def load_library():
    """Loads the library from a JSON file."""
    if os.path.exists(data_file) and os.stat(data_file).st_size > 0:
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Error loading library data. Resetting library.")
            return []
    return []

def save_library(library):
    """Saves the library data to a JSON file."""
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Adds a new book to the library."""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    year = input("Enter the year of the book: ").strip()
    genre = input("Enter the genre of the book: ").strip()
    read = input("Have you read the book? (yes/no): ").strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'📚 Book "{title}" added successfully!\n')

def remove_book(library):
    """Removes a book from the library."""
    title = input("Enter the title of the book to remove: ").strip().lower()

    found_book = next((book for book in library if book['title'].strip().lower() == title), None)
    
    if found_book:
        library.remove(found_book)
        save_library(library)
        print(f'❌ Book "{title}" removed successfully.\n')
    else:
        print(f'⚠️ Book "{title}" not found in the library.\n')

def search_library(library):
    """Searches for a book by title or author."""
    search_by = input("Search by title or author: ").strip().lower()
    
    if search_by not in ["title", "author"]:
        print("⚠️ Invalid search category. Choose 'title' or 'author'.\n")
        return
    
    search_term = input(f"Enter the {search_by}: ").strip().lower()
    
    results = [book for book in library if search_term in book[search_by].strip().lower()]

    if results:
        print("\n🔎 Search Results:")
        for book in results:
            status = "✅ Read" if book['read'] else "❌ Unread"
            print(f"- {book['title']} by {book['author']} ({book['year']}, {book.get('genre', 'Unknown Genre')}) - {status}")
    else:
        print(f"⚠️ No books found matching '{search_term}' in {search_by}.\n")

def display_all_books(library):
    """Displays all books in the library."""
    if not library:
        print("📭 The library is empty.\n")
        return
    
    print("\n📚 Library Collection:")
    for book in library:
        status = "✅ Read" if book['read'] else "❌ Unread"
        print(f"- {book['title']} by {book['author']} ({book['year']}, {book.get('genre', 'Unknown Genre')}) - {status}")
    print()

def display_statistics(library):
    """Displays statistics about the library."""
    total_books = len(library)
    read_books = sum(book['read'] for book in library)
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"📖 Total books: {total_books}")
    print(f"📗 Books read: {read_books}")
    print(f"📘 Percentage read: {percentage_read:.2f}%\n")

def main():
    """Main menu for the library system."""
    library = load_library()
    while True:
        print("\n📚 Library Menu")
        print("1️⃣ Add a book")
        print("2️⃣ Remove a book")
        print("3️⃣ Search the library")
        print("4️⃣ Display all books")
        print("5️⃣ Display statistics")
        print("6️⃣ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("👋 Goodbye! Have a great day.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
