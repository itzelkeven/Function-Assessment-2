def FirstBigger(d1, d2):
    if d1 > d2:
        return True
    else:
        return False

d1 = float(input("Enter a Decimal Number: "))
d2 = float(input("Another one: "))

print(FirstBigger(d1,d2))

print()
print()

def Badger():
    for i in range(10):
        print("Badger")

Badger()
