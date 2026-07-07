#Problema 10
num = int(input("Ingrese un número: "))

if num > 0:
    if num % 2 == 0:
        print(f"{num} es positivo par")
    else:
        print(f"{num} es positivo impar")
else:
    print("No es positivo")