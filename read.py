try:
    with open('c:\\users\\cesar\\desktop\\es.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("naannanannanna")