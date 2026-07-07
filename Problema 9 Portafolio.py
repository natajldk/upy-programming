#Problema 9
usuario = "admin"
contraseña = "1234"

u = input("Ingresa el usuario: ")

if u == usuario:
    c = input("Ingresa la contraseña: ")
    if c == contraseña:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario desconocido")