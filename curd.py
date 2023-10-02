from flask import Flask,jsonify,request

app = Flask(__name__)

# Sample data
books = [
        {"id":1,"title":"How to fuck up", "author":"Rashh"},
        {"id":2,"title":"How to be selfless","author":"Gauti"},
        {"id":3,"title":"How to learn","author":"Pedamma"}
]

# get all books
@app.route('/book',methods=['GET'])
def get_books():
    return books

# get books based on id
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return {'error':'book not found'}

# create a new book
@app.route('/book', methods=['POST'])
def create_book():
    new_book = {"id":len(books)+1,"title":request.json['title'],"author":request.json['author']}
    books.append(new_book)
    return new_book

# update a book
@app.route('/book/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return book
    return {'error':'book not found'}

# delete a book
@app.route('/book/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {'data':'book deleted succesfully'}
    return {'error':'book not found'}


# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)