from array import array


class ArrayQ:
    def __init__(self):
        self.__items = array('l',[]) # skapar en array av data typen long int - en större integer?

    def isEmpty(self):
        return self.__items == array('l',[]) # Kollar om listan är lika med en tom lista - returnerar True/ False

    def enqueue(self, item):
        self.__items.insert(0,item) # lägger till värden i slutet på kön, index 0.

    def dequeue(self):
        return self.__items.pop() # tar bort från början på kön, index -1

    def size(self):
        return len(self.__items) # returnerar storleken på arrayn


    if __name__ == "__main__":
        pass