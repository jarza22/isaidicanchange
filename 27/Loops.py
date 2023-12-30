#For
for i in range(10,21):
    if i%2 == 0:
        print(i**2)
    else:
        print(i**3)

name = "Scarlet Jadzia Maddox"
for letter in name:
    print(letter, end=" ")
print("\n")

newName = ""
for i, letter in enumerate(name):
    print("Letter #" + str(i) + ": " + letter)
    if i%2 != 0:
        newName += name[i]
    else:
        newName += name[i].upper()
print(newName)

#While
x = 4084
while x%2 == 0:
    print(x)
    x //= 2

x = 4084
while x%2 == 0 or x > 100:
    print(x)
    x //= 2

#Do-While
while True:
    choice = int(input("Make a selection (0 to exit): "))
    match choice:
        case 1:
            print("Cheeseburer Combo")
        case 2:
            print("3pc Chicken Tender Combo")
        case 3:
            print("Double BBQ Bacon Burger")
        case 0:
            print("Goodbye")
            break
        case other:
            print("Sorry, we don't have that.")