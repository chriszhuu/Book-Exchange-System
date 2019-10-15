from list import List
import random


class Person:
    numMade = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ID = Person.numMade
        Person.numMade += 1
        self.friend = List()
        self.curBook = List()
        self.bookHistory = List()
        self.curState = ''

    def __str__(self):
        self.recordState()
        return self.curState

    def getName(self):
        return self.name

    def getID(self): return self.ID

    def getAge(self): return self.age

    def getFriend(self): return self.friend

    def countFriend(self): return self.friend.getSize()

    def addFriend(self,friend):
        self.friend.append(friend)

    def unfriend(self,friend):
        self.friend.delete(friend)

    def countBook(self): return self.curBook.getSize()

    def getBook(self):
        return self.curBook

    def getBookHistory(self):
        return self.bookHistory

    def addBook(self,book):
        self.curBook.append(book)
        self.bookHistory.append(book)

    def removeBook(self,book):
        self.curBook.delete(book)

    def rateBook(self,book,rating):
        book.setRating(rating)

    def annotateBook(self,book):
        book.setAnnotation(self.getID())

    def recBorrow(self,bookInfo,infoType,queue,historicQueue):
        friend = queue.pop()
        if friend.getFriend().isEmpty() is False:
            for new in friend.getFriend():
                if historicQueue.find(new.getName(),"name") is None:
                    queue.append(new)
                    historicQueue.append(new)
        if friend.getBook().find(bookInfo, infoType):
            found = friend.getBook().find(bookInfo, infoType)
            self.addBook(found)
            friend.removeBook(found)
            print(">>>", self.getName(), 'borrows "' + found.getName()
                  + '" from', friend.getName())

            # random decision about annotating or not
            binary = random.randint(0,1)
            if binary == 1:
                if found.notYetAnnotated(): # if the book can still be annotated
                    self.annotateBook(found)
                    print("\t"+self.getName(),"annotates this book.")
                else: # person wants to annotate, but book is already annotated
                    print("\t" + self.getName(), "wants to but cannot annotate this book.")
            else: # person decides not to annotate
                print("\t"+self.getName(),"does not want to annotate this book.")

            # random rating for the book
            rating = random.randint(2,5)
            self.rateBook(found,rating)
            print("\t"+self.getName(),"gives this book a",str(rating)+"-star rating.")
            print('\tThe overall rating of "'+found.getName()+'"'+" is now",
                  found.getRating(),"stars.\n")
            return True

        if queue.isEmpty() is False:
            self.recBorrow(bookInfo,infoType,queue,historicQueue)
        else:
            print(">>>", self.getName(), 'fails to find "' + str(bookInfo) + '"\n')
            return False

    def borrow(self,bookInfo,infoType):
        print(">>>",self.getName(),"wants to borrow:",str(bookInfo)+",["+infoType+"]")
        if self.getFriend().isEmpty():
            print("There's no one to borrow from...")
            return False
        else:
            queue = List()
            historicQueue = List()
            historicQueue.append(self)
            for friend in self.getFriend():
                queue.append(friend)
                historicQueue.append(friend)
        return self.recBorrow(bookInfo,infoType,queue,historicQueue)

    def lessThan(self,other,type):
        if type == "name":
            if self.getName() < other.getName():
                return True
            return False
        if type == "ID":
            if self.getID() < other.getID():
                return True
            return False
        if type == "age":
            if self.getAge() < other.getAge():
                return True
            return False
        if type == "number of books":
            if self.countBook() < other.countBook():
                return True
            return False

    def recordState(self):
        self.curState = ""
        self.curState += " #" + str(self.ID) +": "+ self.name
        self.curState += ", aged " + str(self.age) + "\n"
        self.curState += "\t Current books[" + str(self.countBook()) + "]: " \
                         + str(self.curBook) +"\n"
        self.curState += "\t Friends[" + str(self.countFriend()) +"]: "\
                         + str(self.friend) + "\n"
