from person import Person
from book import Book
from list import List
import random

# ===== initializing book & people objects =====

library = List() # will contain book objects soon

bookFile = open("newbooklist.txt","r")
for aline in bookFile.readlines(): # creating book objects & add to library
    values = aline.split(",")
    library.append(Book(values[0],values[1],values[2],values[3]))

titleList = List() # catalogue of all book titles
authorList = List() # catalogue of all book authors
topicList = List() # catalogue of all book topics
for book in library: # helps with the random borrowing function
    titleList.append(book.getName())
    authorList.append(book.getAuthor())
    topicList.append(book.getTopic())


population = List() # will contain person objects soon

peopleFile = open("person.txt","r")
fileLines = peopleFile.readlines()
for aline in fileLines: # creating person objects and add to population
    values = aline.split(",")
    population.append(Person(values[0],values[1]))

for aline in fileLines:
    values = aline.split(",")
    person = population.find(values[0],"name")
    bookInfo = values[2].split()
    for ID in bookInfo: # add book objects to each person's possession
        book = library.find(int(ID),"ID")
        person.addBook(book)
    friendInfo = values[3].split()
    for name in friendInfo: # add friends to each person
        friend = population.find(name,"name")
        person.addFriend(friend)


# ===== end of initialization =====

def showPplState():
    print("\n====== Current state of bibliophiles in this world ======\n")
    for person in population:
        print(person)


def showBookState():
    print("\n====== Current state of books in this world ======\n")
    for book in library:
        print(book)


def randBorrow(person):
    """random generation of book information and type for the borrower"""
    infoType = random.randint(0,2)
    if infoType == 0:
        bookInfo = titleList.index(random.randint(0,titleList.getSize()-1))
        infoType = "title"
    elif infoType == 1:
        bookInfo = authorList.index(random.randint(0,authorList.getSize()-1))
        infoType = "author"
    elif infoType == 2:
        bookInfo = topicList.index(random.randint(0,topicList.getSize()-1))
        infoType = "topic"
    person.borrow(bookInfo,infoType)


def everybodyBorrows():
    """every person borrows one random book, by title, author, or topic"""
    for person in population:
        randBorrow(person)


def retrieveAnnotatedBook():
    """retrieving an annotated book,
    nothing will be returned if no one has annotated any book
    or if the annotated book is already in his/her possession"""
    for person in population:
        person.borrow(person.getID(),"annotation")


def viewBookHistory():
    for person in population:
        print(person.getName()+"'s book history:\n"+str(person.getBookHistory()),"\n")


def sortPeople():
    """sort people by name, ID, age, or the number of books"""
    attribute = input('>>> Do you want to sort people by "name","ID","age",or "number of books"?')
    if attribute == "name" or attribute == "ID" or attribute == "age" or attribute == "number of books":
        sorted = population.mergeSort(attribute)
        print("\n>>> The population sorted by",attribute.upper()+", in ascending order:\n\t"+str(sorted)+"\n")
    else:
        print(">>> Sorry! The attribute you entered is not valid...\n")


def sortBooks():
    """sort books by title, author, or rating"""
    attribute = input('>>> Do you want to sort books by "title","author",or "rating"?')
    if attribute == "title" or attribute == "author" or attribute == "rating":
        sorted = library.mergeSort(attribute)
        print("\n>>> The library sorted by",attribute.upper()+", in ascending order:\n")
        for book in sorted:
            print(book.getName())
    else:
        print(">>> Sorry! The attribute you entered is not valid...\n")


#========================== end of functions ========================================

showPplState()
# uncomment the next line if you want to see detailed info on each book. It's quite long
# showBookState()

print("========================================================================\n"
              ">>> Welcome to the world of bibliophiles!\n\n")

def userDecision():
    numberOfTimes = input(">>> How many rounds of borrowing would you like? Please enter an integer\n")
    for n in range(int(numberOfTimes)):
        start = input(">>> Please press return to start a new round of borrowing.\n")
        if start == "":
            print("\n============ Starting Round",str(n+1),"============\n")
            everybodyBorrows()
            print("============ End of Round",str(n+1),"============\n\n")

        showState = input("If you would like to see the current state of the system, "
                          "enter 's'. If not, press something else and return\n")
        if showState == "s":
            showPplState()

userDecision()

# uncomment the next line if
# at least one person has annotated a book and someone borrowed it from them
# otherwise calling retrieveAnnotatedBook() isn't very meaningful
# retrieveAnnotatedBook()

# uncomment the next line if you want to see everyone's book history
# personally I don't find this interesting enough to be included in showPplState()
# viewBookHistory()

# "medium-brother" stuff...
sortPeople()
sortBooks()