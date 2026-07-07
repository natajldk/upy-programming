#Año bisiesto
year=int(input("enter a year: ")) #str
if (year % 4 == 0 and year %100 !=0) or (year % 100 ==0):
    print ("lap year {year}")
else:
    print("Nain")
    
    
#Validar un número dentro de un rango
num= int(input("Ingresa un número cualquiera: "))
rango = 10 <= num <= 15
print (rango)

#vocal o consonante

let=input("Ingresa una letra cualquiera: ")
vocal= let.upper () in "AEIOU"
""" upper - mayusculas / lower - minusculas
"""
print (vocal)