#Problema 11
n = int(input("Ingresa un entero positivo: "))

i = 1
suma = 0

while i <= n:
    suma += i  
    i += 1     

print(f"La suma de 1 hasta {n} es: {suma}")