from linkedQFile import LinkedQ # importera antingen linkedQFile eller arrayQFile

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


# Test av ArrayQ
# q = ArrayQ()
# q.enqueue(1)
# q.enqueue(2)
# x = q.dequeue()
# y = q.dequeue()
# if (x == 1 and y == 2):
#     print("OK")
# else:
#     print("FAILED")

kort = input().split() # Ber om en input
q = LinkedQ() # Skapar ett länkat kö objekt alternativt ett array objekt
for i in kort:
    q.enqueue(i) # Matar in varje element i kön 

while not q.isEmpty(): # körs till kön är tom
    q.enqueue(q.dequeue()) # Tar ut första elementet och lägger till det längst bak i kön
    x = q.dequeue() # tar bort första elementet i kön och skriver ut det.
    print(x, end= " ")

