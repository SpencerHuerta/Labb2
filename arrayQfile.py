class ArrayQ:
    def __init__(self):
        self.__items = array('l',[])

    def isEmpty(self):
        return self.__items == array('l',[])

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)


    if __name__ == "__main__":
        pass