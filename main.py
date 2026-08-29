from array import array

# firstarray = array('l',[1,2,3,6,7,8,9])

# firstarray.append(10)
# print(firstarray)
# firstarray.insert(3,5)
# firstarray.insert(3,4)
# print(firstarray)
# firstarray.insert(0,0)
# firstarray.pop()
# print(firstarray)
# firstarray.remove(7)

# print(firstarray)

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

# q = ArrayQ()
# q.enqueue(1)
# q.enqueue(2)
# x = q.dequeue()
# y = q.dequeue()
# if (x == 1 and y == 2):
#     print("OK")
# else:
#     print("FAILED")

kort = input().split()
q = ArrayQ()
for i in kort:
    q.enqueue(int(i))

while not q.isEmpty():
    q.enqueue(q.dequeue())
    x = q.dequeue()
    print(x)