palabra = input("Ingrese una palabra en infinitivo: ")

pronombres = ["yo" , "tu" , "el" , "nosotros" , "vosotros", "ellos"]

terminaciones = { "ar": ["o", "as", "a", "amos", "ais", "an"],
                  "er": ["o", "es", "e", "emos", "eis", "en"],
                  "ir": ["o", "es", "e", "imos", "is", "en"]
                  }


stem = palabra[:-2]
ending = palabra[-2:]

for key in terminaciones.keys():
    if key == ending:
        for i in range(len(pronombres)):
            print(pronombres[i], stem + terminaciones[ending][i])