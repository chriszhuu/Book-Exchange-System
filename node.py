class Node: # user doesn't use this class at all
    num = 0

    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous
        self.ID = Node.num
        Node.num += 1

    def getID(self):
        return self.ID

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrevious(self,previous):
        self.previous = previous

    def getPrevious(self):
        return self.previous

    def __str__(self):
        return self.getData()

    def __repr__(self):
        return self.getData()

