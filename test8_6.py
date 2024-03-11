import random
tal =[]
for i in range(10):
    tal.append(random.randrange(1,7))

print(tal)
print("antal ettor:",tal.count(1))
antal_1 = 0
for t in tal:
    if t == 1:
        antal_1 = antal_1 + 1
print("antal ettor igen: ", antal_1)
# ta bort antal_1 ettor

for i in range(antal_1):
    tal.remove(1)
print(tal)
# räkna antalet ettor
# ta bort alla ettor
