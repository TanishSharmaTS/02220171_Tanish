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

    new_book = ET.SubElement(root, 'book')
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



parseXML()

addBook('Fault in Our Stars', 'John Green', 2012, 12.99)

deleteBook('Atomic Habits')






        

