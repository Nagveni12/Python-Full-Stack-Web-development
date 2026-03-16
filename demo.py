from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://Nagaveni:Naagu12@cluster0.8ktrah5.mongodb.net/?appName=Cluster0")

# Create database
db = client["libraryDB"]

# Create collection
books = db["books"]

# -------------------------------
# 1. INSERT BOOK RECORDS
# -------------------------------

book1 = {
    "book_id":101,
    "title":"Data Structures",
    "author":"Mark Allen",
    "genre":"Computer Science",
    "status":"Available"
}

book2 = {
    "book_id":102,
    "title":"Python Programming",
    "author":"John Smith",
    "genre":"Computer Science",
    "status":"Available"
}

book3 = {
    "book_id":103,
    "title":"World History",
    "author":"Robert Brown",
    "genre":"History",
    "status":"Available"
}

books.insert_many([book1,book2,book3])

print("Books inserted successfully")


# -------------------------------
# 2. DISPLAY ALL BOOKS
# -------------------------------

print("\nAll Books:")

for book in books.find():
    print(book)


# -------------------------------
# 3. DISPLAY BOOKS BY GENRE
# -------------------------------

print("\nComputer Science Books:")

for book in books.find({"genre":"Computer Science"}):
    print(book)


# -------------------------------
# 4. UPDATE BOOK STATUS
# -------------------------------

books.update_one(
    {"book_id":101},
    {"$set":{"status":"Issued"}}
)

print("\nBook status updated")


# -------------------------------
# 5. DELETE BOOK
# -------------------------------

books.delete_one({"book_id":103})

print("\nBook deleted successfully")