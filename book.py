class Book:
    num = 0

    def __init__(self, title, author, topic = None, edition = None):
        self.title = title
        self.author = author
        self.topic = topic
        self.edition = edition
        self.annotation = None
        self.numRating = 0
        self.rating = 0
        self.ID = Book.num
        Book.num += 1
        self.curState = ''

    def __str__(self):
        self.recordState()
        return self.curState

    def getID(self): return self.ID

    def getName(self): return self.title

    def getAuthor(self): return self.author

    def getTopic(self):
        if self.topic is not None:
            return self.topic
        return "None"

    def getEdition(self):
        if self.edition is not None:
            return self.edition
        return "None"

    def getRating(self):
        if self.rating is not None:
            return self.rating
        return "None"

    def setRating(self,rating):
        """takes new rating and updates the averaged overall rating"""
        sum = self.rating*self.numRating
        self.numRating += 1
        self.rating = (sum+rating)/self.numRating

    def setAnnotation(self,ID):
        """records ID of the annotator"""
        self.annotation = ID

    def getAnnotation(self):
        return self.annotation

    def notYetAnnotated(self):
        """checks whether book is available for annotating"""
        if self.annotation is None:
            return True

    def lessThan(self,other,type):
        """helps to sort books by title, author, rating"""
        if type == "title":
            if self.getName() < other.getName():
                return True
            return False
        if type == "author":
            if self.getAuthor() < other.getAuthor():
                return True
            return False
        if type == "rating":
            if self.rating is not None and other.rating is not None:
                if self.getRating() < other.getRating():
                    return True
            return False

    def recordState(self):
        """display of book info"""
        self.curState = ""
        self.curState += " #" + str(self.ID) + ": " + self.title
        self.curState += ", " + self.author + "\n"
        self.curState += "\t Topic: "+ self.getTopic()
        self.curState += ", Edition["+ str(self.getEdition())+ "]"
        self.curState += ", Rating["+str(self.getRating())+"]" + "\n"




