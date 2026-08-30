from array import array


class LinkedQ:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def enqueue(self, item):
        temp = Node(item)
        temp.setNext(self.__head)
        self.__head = temp

    def dequeue(self):
        previous = None
        current = self.__head
        
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = None
            pass
        else:
            previous.setNext(None)
        return current.getData()

            
        

    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count += 1
            current.getNext()
        return count




class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



if __name__ == "__main__":
    kort = input().split()
    q = LinkedQ()
    for i in kort:
        q.enqueue(int(i))

    while not q.isEmpty():
        q.enqueue(q.dequeue())
        x = q.dequeue()
        print(x)
        