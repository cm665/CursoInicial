name = ""

while len(name) == 0:
    name = input("enter your name: ")

print("hello "+name)

for i in range (10+1) :
    print(i)

for i in range (5,10+1) :
    print(i)

for i in range (5,10+1,2) :
    print(i)

for i in "carlos montelongo" :
    print(i)

rows = int(input("how many rows: "))
columns = int(input("how many columns: "))
symbol = input("enter a symbol to use: ")

for i in range(rows): 
    for j in range(columns) :
        print(symbol, end="")
    print()

while True :
    name2 = input("enter your name: ")
    if name2 != "":
        break

phone_number = "284-342-2445"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range (1,15):

    if i == 13:
        pass
    else:
        print(i)
