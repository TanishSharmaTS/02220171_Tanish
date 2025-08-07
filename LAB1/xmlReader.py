import xml.etree.ElementTree as ET

path = r'books.xml'

# create element tree object
tree = ET.parse(path)
    
# get root element
root = tree.getroot()


def parseXML():

    for books in root.findall('book'):
        title = books.find('title').text
        author = books.find('author').text
        yearPublished = books.find('yearPublished').text
        price = books.find('price').text

        print(f'Title: ' + title + '\nAuthor: ' + author + '\nYear published: ' + yearPublished + '\nPrice: ' + price + '\n')


def addBook(title, author, yearPublished, price):

    new_book = ET.Element('book')
    ET.SubElement(new_book, 'title').text = str(title)
    ET.SubElement(new_book, 'author').text = str(author)
    ET.SubElement(new_book, 'yearPublished').text = str(yearPublished)
    ET.SubElement(new_book, 'price').text = str(price)

    root.append(new_book)

    print(f'Book with title "{title}" added.')

     
    tree.write(path)


def deleteBook(title):
    for book in root.findall('book'):
        if book.find('title').text == title:
            root.remove(book)
            tree.write(path)
            print(f'Book with title "{title}" deleted.')
            return
    print(f'Book with title "{title}" not found.')



while(True):

    print('\nEnter Values to Get the output.\n1.Parse XML\n2.Add Book\n3.Delete Book')

    value = int(input())

    match value:
        case 1:
            parseXML()

        case 2: 
            print('Add book title')
            title = input()
            print('Add book author')
            author = input()
            print('Add published year')
            publishedYear = input()
            print('Add price')
            price = input()

            addBook(title, author, publishedYear, price)


        case 3:
            print('Add title to delete')
            title = input()
            deleteBook(title)
    
        case _:
            print('Invalid Option')










        

