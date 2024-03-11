inköpslista = [1, 3, 2]
print(inköpslista)
inköpslista.index(1) == (2)
print(inköpslista)
inköpslista.extend([4])
print(inköpslista)
inköpslista.sort()
print("sorterad:", inköpslista)

import random
tärningar = []
for i in range (6):
    tärningar.append(random.randint(1,6))
print("antal treor", tärningar.count(3))

