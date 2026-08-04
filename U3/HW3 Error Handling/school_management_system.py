usuarios = { "prangel" : { "password" : "1234", "rol" : "alumno", "nombre" : "Pilar Rangel" },
             "jarias" : { "password" : "1234", "rol" : "alumno", "nombre" : "Jorge Arias" },
             "dflores" : { "password" : "1234", "rol" : "alumno", "nombre" : "Diego Flores" },
             "jecheverria" : { "password" : "1234", "rol" : "alumno", "nombre" : "Jaén Echeverria" },
             "spool" : { "password" : "1234", "rol" : "alumno", "nombre" : "Sabrina Pool" },
             "mmedina" : { "password" : "1234", "rol" : "alumno", "nombre" : "Martín Medina" },
             "gvillegas": { "password" : "1234", "rol" : "maestro", "nombre" : "Gabriela Villegas" },
             "jjimenez": { "password" : "1234", "rol" : "coordinador", "nombre" : "Joaquin Jimenez" },
              }

materias = ("Matemáticas", "Programación", "Ingles")

calificaciones = { "prangel" : {"Matemáticas" : 7, "Programación": 8.9, "Inglés": 7.5},
                   "jarias" : {"Matemáticas" : 9.4, "Programación": 10, "Inglés": 6.0},
                   "dflores" : {"Matemáticas" : 9.0, "Programación": 8.5, "Inglés": 9.0},
                   "jecheverria" : {"Matemáticas" : 10.0, "Programación": 10.0, "Inglés": 7.0},
                   "spool" : {"Matemáticas" : 7.8, "Programación": 9.0, "Inglés": 5.0},
                   "mmedina" : {"Matemáticas" : 8.7, "Programación": 8.0, "Inglés": 8.0},
                   }
materias_aprobadas= set()
materias_reprobadas= set()
usuario= input("Ingrese su usario: ")
contraseña= input("Ingrese su contraseña: ")

while usuario not in usuarios.keys() or contraseña != usuarios[usuario]["password"]:
    print("Usuario o Contraseña incorrecta")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
else:
    print(f"Bienvenido, {usuarios[usuario]["nombre"]} ({usuarios[usuario]["rol"]}) ")
                   
if usuarios[usuario]["rol"] == "alumno":
    print(f"Boleta de {usuarios[usuario]["nombre"]}")
    for materia in calificaciones[usuario]:
        print(materia, ":", calificaciones[usuario][materia])
        if calificaciones[usuario][materia] >= 8:
            materias_aprobadas.add(materia)
        else:
            materias_reprobadas.add(materia)
    print(f"Materias aprobadas: {materias_aprobadas}")
    print(f"Materias reprobadas: {materias_reprobadas}")    
elif usuarios[usuario]["rol"] == "maestro":
    alumno = input("Ingrese el usuario del alumno deseado: ")
    materia = input("Ingrese la materia deseada: ")
    calificacion = float(input("Ingrese la nueva calificación: "))
    calificaciones[alumno][materia] = calificacion
    print(f"Alumno: {alumno}")
    print(f"Materia: {materia}")
    print(f"Nueva calificación: {calificacion}")
    print("Calificación actualizada.")
else:
    for personal in usuarios:
        if usuarios[personal]["rol"] == "maestro":
            print(f"Maestra/o {usuarios[personal]["nombre"]}")
    for materia in materias:
        print(materia)
    for estudiante in calificaciones:
        print(f"Estudiante {usuarios[estudiante]["nombre"]}: {calificaciones[estudiante]}")
