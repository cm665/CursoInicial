name = "bro code"

print(len(name))
print(name.find("b"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","u"))
print(name*3)

x = 1    #int
y = 2.4  #float
z = "3"  #str

x = float(x)
z = int(z)

print(x)
print("y is " +str(y))
print(z*3)


nombre = input("cual es tu nombre: ")
años = int(input("cuantos años tienes: "))
peso = float(input("cuanto pesas: "))
años = años + 2
print("hola " +nombre)
print("tu tienes " +str(años)+ " años")
print("tu pesas " +str(peso)+ " kilos")

first_name = name[0:3]
last_name = name[4:]
funkyname = name[0:8:3]
reversname = name[::-1]


print(first_name)
print(last_name)
print(funkyname)
print(reversname)

website = "http://google.com"
website2 = "http://ddd.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])