tal = [23, 45, 43, 25, 33]
print(tal[2])
print(tal[-2])

a = [10, 20, 20]
for b in a:
    if b == 20:
        print(b)
    else:
        print(0)
    
for x in range(1,5):
    print(x)

tärningar = [1, 4, 2]
print(len(tärningar))
tärningar.sort()
print(tärningar)

x = 0
y = [1, 0, 1, 1, 0]
for z in y:
    if z == 1:
        x = x + 10
print(x)