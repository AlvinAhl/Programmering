form = input("Skriv en form")

while form != 'rund':
    print('fel, gissa igen')
    form = input("Skriv en form, igen")
print('bra')

tal = input("skriv en siffra")
if tal<"42":
    print("för litet")
elif tal>"42":
    print("för stor")
else:
    print("rätt")
print("tack o hej")

