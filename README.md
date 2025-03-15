# 📚 Library Management System

A simple Python-based **Library Management System** that allows users to add, remove, search, and track books in their personal collection. Books are stored in a JSON-based text file (`library.txt`).

## 🚀 Features
- **Add books** with title, author, year, genre, and read status.
- **Remove books** by title.
- **Search books** by title or author.
- **Display all books** in the library.
- **View statistics** (total books, read books, percentage read).
- **Data persistence** using a JSON file (`library.txt`).

## 🛠️ Requirements
- Python 3.x

## 📥 Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/library-management.git
   cd library-management
   ```
2. **Run the script:**
   ```sh
   python library.py
   ```

## 📌 Usage
Once the script is running, you'll see the main menu:
```
📚 Library Menu
1️⃣ Add a book
2️⃣ Remove a book
3️⃣ Search the library
4️⃣ Display all books
5️⃣ Display statistics
6️⃣ Exit
```
Enter a number to perform the corresponding action.

### 📝 Example Operations
#### ➕ Adding a Book
```
Enter the title of the book: The Great Gatsby
Enter the author of the book: F. Scott Fitzgerald
Enter the year of the book: 1925
Enter the genre of the book: Fiction
Have you read the book? (yes/no): yes
📚 Book "The Great Gatsby" added successfully!
```

#### 🔍 Searching for a Book
```
Search by title or author: Fitzgerald
🔎 Search Results:
- The Great Gatsby by F. Scott Fitzgerald (1925, Fiction) - ✅ Read
```

#### ❌ Removing a Book
```
Enter the title of the book to remove: The Great Gatsby
❌ Book "The Great Gatsby" removed successfully.
```

## 🏗️ Project Structure
```
📁 library-management/
│-- 📄 library.py  # Main Python script
│-- 📄 README.md  # Documentation
│-- 📄 library.txt  # JSON-based data storage
```

## 🏆 Contributions
Feel free to **fork** the repository and submit **pull requests**. Suggestions & improvements are welcome!

