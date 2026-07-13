#Problema 8
temp = float(input("Ingresa la temperatura en °C: "))

if temp <= 0:
    print("Sólido (hielo)")
elif temp < 100:
    print("Líquido (agua)")
else:
    print("Gaseoso (vapor)")