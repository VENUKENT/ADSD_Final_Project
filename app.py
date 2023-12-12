# my_project
from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/books")

@route("/books")
def get_books():
    books = database.get_all_books()
    return template("books.tpl", books=books)

@route("/books/add")
def get_add_book():
    return template("add_book.tpl")

@post("/books/add")
def post_add_book():
    title = request.forms.get("title")
    author = request.forms.get("author")
    database.add_book(title, author)
    redirect("/books")

@route("/books/<book_id>")
def get_book_details(book_id):
    book = database.get_book_details(book_id)
    ratings = database.get_ratings_for_book(book_id)
    return template("book_details.tpl", book=book, ratings=ratings)

@route("/books/<book_id>/add_rating")
def get_add_rating(book_id):
    return template("add_rating.tpl", book_id=book_id)

@post("/books/<book_id>/add_rating")
def post_add_rating(book_id):
    rating_value = request.forms.get("rating")
    database.add_rating(book_id, rating_value)
    redirect(f"/books/{book_id}")

@route("/books/<book_id>/update")
def get_update_book(book_id):
    book = database.get_book_details(book_id)
    return template("update_book.tpl", book=book)

@post("/books/<book_id>/update")
def post_update_book(book_id):
    title = request.forms.get("title")
    author = request.forms.get("author")
    database.update_book(book_id, title, author)
    redirect("/books")

@route("/books/<book_id>/delete")
def get_delete_book(book_id):
    database.delete_book(book_id)
    redirect("/books")

run(host='localhost', port=8080)
