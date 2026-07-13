#IMC < 18.5 desnutrición
#IMC 18.5<= x <=25 normal
#IMC 25<x<30 sobrepeso
#IMC >= 30 Majin boo
weight= float(input("Ingrese su peso: "))
height= float(input("Ingresa tu altura: "))
IMC= weight/(height*height)
if IMC < 18.5:
    print("Hay desnutrición")
elif IMC <= 25:
    print("IMC normal")
elif IMC <=30:
    print("Estas gordito")
else:
    print("Estas Majin boo")