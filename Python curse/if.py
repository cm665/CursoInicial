age = int(input("cauntos años tienes: "))

if age >= 100:
    print("tu eres una persona muy vieja")
elif age>= 18:
    print("tu eres un adulto")
elif age < 0:
    print("aun no as nacido")
else:
    print("eres un niño")

number = float(input("cuanto es 6-5: "))

if number == 1:
    print("correcto")
else:
    print("incorrecto")

temp = int(input("what is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif temp < 0 or temp> 30:
    print("the temperature is bad today")
    print("stay inside")
    