import json
import jsonschema
import os
from jsonschema import validate

file_path = r"books.json"


schema_file_path = r"bookSchema.json"


def get_file_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                content = json.load(file)
                return content
            except json.JSONDecodeError:
                return []
    else:
        print("File not found!")
        return []

def validate_json(data, schema):
    try:
        validate(instance = data, schema = schema)
        print("Valid JSON")
    except jsonschema.exceptions.ValidationError as e:
        print("JSON is invalid")

def print_books(content):

    print("\nBOOKS\n")

    for book in content:
        print('ID: '+ str(book["id"]))
        print('Title: ' + book["title"])
        print('Author: ' + book["author"])
        print('Year Published: ' + book["yearPublished"])
        print('Price: ' + str(book["price"]) + "\n")


def add_books(content, file_path):
    ID = int(input("Enter book id\n"))
    title = input("Enter book title\n")
    author = input("Enter author name\n")
    yearPublished = input("Enter Year Published\n")
    price = int(input("Enter price\n"))

    newBook = {
        'id': ID,
        'title': title,
        'author': author,
        'yearPublished': yearPublished,
        'price': price
    }

    content.append(newBook)

    with open(file_path, "w") as file:
        json.dump(content, file, indent=4)


def delete_books(content, file_path):

    ID = int(input("Enter the book ID you want to delete\n"))

    for book in content:
        if book.get('id') == ID:
            content.remove(book)

            with open(file_path, "w") as file:
                json.dump(content, file, indent = 4)
    
        else:
            print('Book id invalid')


def update_books(content, file_path):

    edit_book = int(input("Enter the book id that you want to edit\n"))


    for book in content:
        if book.get('id') == edit_book:
            book['title'] = input("Enter the new Title\n") or book.get('title')
            book['author'] = input("Enter the new Author\n") or book.get('author')
            book['yearPublished']= input("Enter the new Year Published\n") or book.get('yearPublished')
            new_price = input("Enter the new Price\n")
            book['price'] = int(new_price) if new_price else book.get('price')

        with open(file_path, "w") as file:
            json.dump(content, file, indent = 4)


content = get_file_content(file_path)

schema = get_file_content(schema_file_path)

validate_json(content, schema)

while(True):

    content = get_file_content(file_path)

    print('\nEnter Values to Get the output.\n1.Parse JSON\n2.Add Book\n3.Delete Book\n4.Update Book\n5.To break')

    value = int(input())

    match value:
        case 1:
            print_books(content)

        case 2:
            add_books(content, file_path)
        
        case 3:
            delete_books(content, file_path)
        
        case 4:
            update_books(content, file_path)
        
        case 5:
            break

        case _:
            print("Invalid Input")
