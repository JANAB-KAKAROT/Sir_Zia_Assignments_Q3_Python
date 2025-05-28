import streamlit as st
import json
import os

# ---------- Constants ----------
FILE_NAME = 'library.json'

# ---------- Helper Functions ----------
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_library(library):
    with open(FILE_NAME, 'w') as f:
        json.dump(library, f, indent=4)

def display_book(book, index=None):
    status = 'Read' if book['read'] else 'Unread'
    text = f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}"
    return f"{index+1}. {text}" if index is not None else text

def search_books(library, search_type, search_term):
    return [
        book for book in library 
        if search_term.lower() in book[search_type].lower()
    ]

def get_statistics(library):
    total = len(library)
    if total == 0:
        return 0, 0.0
    read_books = len([b for b in library if b['read']])
    percentage = (read_books / total) * 100
    return total, percentage

# ---------- App UI ----------
st.title("📚 Personal Library Manager")

# Load library
library = load_library()

menu = st.sidebar.selectbox("Menu", [
    "Add a Book",
    "Remove a Book",
    "Search for a Book",
    "Display All Books",
    "Display Statistics",
])

# ---------- Add Book ----------
if menu == "Add a Book":
    st.header("➕ Add a New Book")
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    year = st.number_input("Enter the publication year:", min_value=0, max_value=9999, step=1)
    genre = st.text_input("Enter the genre:")
    read = st.radio("Have you read this book?", ["Yes", "No"])
    
    if st.button("Add Book"):
        if title and author and genre:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": True if read == "Yes" else False
            }
            library.append(book)
            save_library(library)
            st.success("✅ Book added successfully!")
        else:
            st.error("❌ Please fill in all fields.")

# ---------- Remove Book ----------
elif menu == "Remove a Book":
    st.header("🗑️ Remove a Book")
    book_titles = [book['title'] for book in library]
    if not book_titles:
        st.info("No books in the library.")
    else:
        book_to_remove = st.selectbox("Select a book to remove:", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book['title'] != book_to_remove]
            save_library(library)
            st.success("✅ Book removed successfully!")

# ---------- Search ----------
elif menu == "Search for a Book":
    st.header("🔍 Search for a Book")
    option = st.radio("Search by:", ["Title", "Author"])
    search_term = st.text_input(f"Enter the {option.lower()}:")
    
    if st.button("Search"):
        if search_term:
            results = search_books(library, option.lower(), search_term)
            if results:
                for idx, book in enumerate(results):
                    st.markdown(display_book(book, idx))
            else:
                st.warning("No matching books found.")
        else:
            st.error("Please enter a search term.")

# ---------- Display All Books ----------
elif menu == "Display All Books":
    st.header("📖 Your Library")
    if not library:
        st.info("No books in your library yet.")
    else:
        for i, book in enumerate(library):
            st.markdown(display_book(book, i))

# ---------- Statistics ----------
elif menu == "Display Statistics":
    st.header("📊 Library Statistics")
    total, percent = get_statistics(library)
    st.write(f"**Total books:** {total}")
    st.write(f"**Percentage read:** {percent:.2f}%")

# Save the updated library when any change occurs
save_library(library)
