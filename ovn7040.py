'''tal = int(input("Mata in ett heltal: "))
if tal >= 0 and tal < 10:
    print("positiv ental")
else:
    print("negativt eller flersiffrigt")
    

tal = int(input("Mata in näst sista siffran i ditt personnummer:"))
if tal %2 == 0:
    print('du är en kvinna')
if tal %2 == 1:
    print('du är en pojk')

tal = int(input("Mata in ett tal:"))
tal2 = int(input("Mata in ett tal till:"))
if tal>tal2:
          print('tal ett är större än tal två')
if tal2>tal:
          print('tal två är större än tal ett')
tal = int(input("Mata in ett heltal: "))
if tal>=0 and tal<10:
    print("ensiffrigt tal")
if tal>=10 and tal<99:
    print("tvåsiffrigt tal")
if tal>=100 and tal<999:
    print("tresiffrigt tal")
if tal<=0:
    print("Negativt tal")

tal1 = int(input("mata in ett tal: "))
tal2 = int(input("mata in ett tal till: "))
tal3 = int(input("mata in ytterligare ett tal: "))
if tal1 < tal2 and tal1 < tal3:
    print("Tal 1 är minst")
if tal2 < tal1 and tal1 < tal3:
    print("Tal 2 är minst")
if tal3 < tal1 and tal1 < tal2:
    print("Tal 3 är minst")
    '''
tal1 = int(input("mata in ett tal: "))
tal2 = int(input("mata in ett tal till: "))
tal3 = int(input("mata in ytterligare ett tal: "))
if tal1 < tal2 and tal3 and tal2 < tal3:
    print(tal1, tal2, tal3)
elif tal1 < tal2 and tal3 and tal3 < tal2:
    print(tal1, tal3, tal2)
elif tal2 < tal1 and tal3 and tal1 < tal3:
    print(tal2, tal1, tal3)
elif tal2 < tal1 and tal3 and tal3 < tal1:
    print(tal2, tal3, tal1)
elif tal3 < tal1 and tal2 and tal1 < tal2:
    print(tal3, tal1, tal2)
elif tal3 < tal1 and tal2 and tal2 < tal1:
    print(tal3, tal2, tal1)
