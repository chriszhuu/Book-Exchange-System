from node import Node


class List:
    def __init__(self, front = None, back = None):
        self.size = 0
        self.front = front
        self.back = back

    def __str__(self):
        s = ""
        if self.isEmpty():
            s += "None"
        else:
            node = self.front
            s = ""
            # print comma behind every item except for the last
            while node is not self.back:
                s += node.data.getName() + ", "
                # assuming node.data is object and we want to print its name
                node = node.getNext()
            s += node.data.getName()
        return s

    def __repr__(self):
        s = ""
        if self.isEmpty():
            s += "None"
        else:
            node = self.front
            while node is not self.back:
                s += node.data.getName() + ", "
                node = node.getNext()
            s += node.data.getName()
        return s

    def __iter__(self):
        """this helps with iterating through my list,with for loop"""
        self.current = self.front
        return self

    def __next__(self):
        if self.current is self.back:
            raise StopIteration
        else:
            result = self.current.getData()
            self.current = self.current.getNext()
            return result

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def getFront(self):
        return self.front

    def index(self,index):
        """get data in a specific node by index number"""
        node = self.front
        counter = 0
        while counter < index:
            node = node.getNext()
            counter += 1
        return node.getData()

    def find(self,data,type = None):
        """find stuff by name, ID, author, topic, or annotation.
           if type is specified, return data in the node;
           otherwise, return the node itself"""
        if self.isEmpty():
            return None
        else:
            return self.recFind(data,self.front,type)

    def recFind(self,data,node,type = None):
        if node is None:
            return None
        elif type == "name" or type == "title":
            if node.getData().getName() == data:
                return node.getData()
            elif node is not self.back:
                return self.recFind(data,node.getNext(),"name")
            else:
                return None
        elif type == "ID":
            if node.getData().getID() == data:
                return node.getData()
            elif node is not self.back:
                return self.recFind(data,node.getNext(),"ID")
            else:
                return None
        elif type == "author":
            if node.getData().getAuthor() == data:
                return node.getData()
            elif node is not self.back:
                return self.recFind(data,node.getNext(),"author")
            else:
                return None
        elif type == "topic":
            if node.getData().getTopic() == data:
                return node.getData()
            elif node is not self.back:
                return self.recFind(data,node.getNext(),"topic")
            else:
                return None
        elif type == "annotation":
            if node.getData().getAnnotation() == int(data):
                return node.getData()
            elif node is not self.back:
                return self.recFind(data,node.getNext(),"annotation")
            else:
                return None
        elif type is None:
            if node.getData() == data:
                return node
            elif node is not self.back:
                return self.recFind(data,node.getNext())
            else:
                return None

    def append(self,data):
        temp = Node(data)
        if self.isEmpty():
            self.front = temp
            self.back = temp
        else:
            temp.setPrevious(self.back)
            self.back.setNext(temp)
            self.back = temp
        self.size += 1

    def prepend(self,data):
        temp = Node(data)
        if self.isEmpty():
            self.front = temp
        else:
            temp.setNext(self.front)
            self.front.setPrevious(temp)
            self.front = temp
        self.size += 1

    def pop(self):
        """removes first node from queue and get its data"""
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.getNext()
        if self.front is None:
            self.back = None
        self.size -= 1
        return temp.getData()

    def insert(self, data, found):
        """inserting data behind a specific node"""
        if self.isEmpty():
            self.append(data)
        else:
            temp = Node(data)
            temp.setPrevious(found)
            temp.setNext(found.getNext())
            found.setNext(temp)
            if temp.getNext() is not None:
                temp.getNext().setPrevious(temp)
            self.size += 1

    def delete(self,data):
        found = self.find(data)
        if found is not None:
            if self.size == 1:
                found.setData(None)
            elif found.getPrevious() is not None and found.getNext() is not None:
                found.getPrevious().setNext(found.getNext())
                found.getNext().setPrevious(found.getPrevious())
            elif found.getPrevious() is None: # if data is first in the list
                found.getNext().setPrevious(None)
                self.front = found.getNext()
            elif found.getNext() is None: # if data is last in the list
                self.back = found.getPrevious()
                found.getPrevious().setNext(None)
            self.size -= 1
        else:
            print("Data not in this list...")

    def mergeSort(self,type):
        """sort the list by different attributes,
        by splitting the list down into a binary tree"""
        if self.size <= 1:
            return self
        midIndex = self.size//2
        left = List()
        right = List() # finding mid index and creating two sublists
        n = 0 # using while loop and index to add item to sublist
        while n < midIndex:
            left.append(self.index(n))
            n += 1
        while n < self.size:
            right.append(self.index(n))
            n += 1
        left = left.mergeSort(type) # keep splitting the sublists
        right = right.mergeSort(type) # till len() <= 1
        return self.iterateMerge(left,right,type) # merging returned lists

    @staticmethod
    def iterateMerge(l1,l2,type): # assuming l1, l2 already sorted
        locL1 = l1.getFront()
        locL2 = l2.getFront()
        result = List() # create something to hold sorted items
        while (locL1 is not None) and (locL2 is not None):
            a = locL1.getData() # lets just grab the data once
            b = locL2.getData() # avoid grabbing the same data multiple times
            if a.lessThan(b,type):
                result.append(a)
                locL1 = locL1.getNext()
            else:
                result.append(b)
                locL2 = locL2.getNext()
        if locL1 is None:
            while locL2 is not None:
                result.append(locL2.getData())
                locL2 = locL2.getNext()
        if locL2 is None:
            while locL1 is not None:
                result.append(locL1.getData())
                locL1 = locL1.getNext()
        return result


