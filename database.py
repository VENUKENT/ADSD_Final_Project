# database.py
books = []
book_id_counter = 1

def initialize_database():
    global books, book_id_counter
    books = []
    book_id_counter = 1

def get_all_books():
    return books

def add_book(title, author):
    global book_id_counter
    book = {
        'id': book_id_counter,
        'title': title,
        'author': author,
        'ratings': []
    }
    book_id_counter += 1
    books.append(book)

def get_book_details(book_id):
    return next((book for book in books if str(book['id']) == book_id), None)

def get_ratings_for_book(book_id):
    book = get_book_details(book_id)
    return book['ratings'] if book else []

def add_rating(book_id, rating_value):
    book = get_book_details(book_id)
    if book:
        book['ratings'].append(int(rating_value))

def update_book(book_id, title, author):
    book = get_book_details(book_id)
    if book:
        book['title'] = title
        book['author'] = author

def delete_book(book_id):
    global books
    books = [book for book in books if str(book['id']) != book_id]
