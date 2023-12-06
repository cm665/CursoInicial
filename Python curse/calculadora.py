import math as m
num1 = input("dame el primer numero")

num2 = input("dame el segundo numero")

if float(num1) and float(num2):
    num1 = float(num1)
    num2 = float(num2)

    suma = num1 + num2
    divicion = num1 / num2
    multiplicacion = num1 * num2
    resta = num1 - num2
    raiz = m.sqrt(num1)
    raiz2 = m.sqrt(num2)
    suma2 = raiz + raiz2
    cuadrado = num1 ** 2
    cuadrado2 = num2 ** 2
    suma3 = cuadrado + cuadrado2
    mensaje = f"""
    la suma de numero 1 y numero 2 = {str(suma)}
    la resta de numero 1 y numero 2 = {str(resta)}
    la divicion de numero 1 y numero 2 = {str(divicion)}
    la multiplicacion de numero 1 y numero 2 = {str(multiplicacion)}
    la raiz de numero 1 = {str(raiz)}
    la raiz de numero 2 = {str(raiz2)}
    la suma de raiz 1 y raiz 2 = {str(suma2)}
    el numero 1 al cuadrado es = {str(cuadrado)} 
    el numero 2 al cuadrado es ={str(cuadrado2)}
    la suma de cuadrado 1 y cuadrado 2 = {str(suma3)}
    """
    print(mensaje)
else:
    print("Los datos ingresados no son numericos ")