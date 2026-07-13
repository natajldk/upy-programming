#Año bisiesto
year=int(input("enter a year: ")) #str
if (year % 4 == 0 and year %100 !=0) or (year % 100 ==0):
    print ("lap year {year}")
else:
    print("Nain")
