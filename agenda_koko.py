agenda = {}

def agregar_evento(fecha, descripcion):
    if fecha in agenda:
        agenda[fecha].append(descripcion)
    else:
        agenda[fecha] = [descripcion]

def mostrar_agenda():
    for fecha, eventos in agenda.items():
        print(f"{fecha}:")
        for e in eventos:
            print(f"  - {e}")

def buscar_evento(fecha):
    if fecha in agenda:
        print(f"Eventos en {fecha}:")
        for e in agenda[fecha]:
            print(f"  - {e}")
    else:
        print("No hay eventos en esa fecha.")

def eliminar_evento(fecha, descripcion):
    if fecha in agenda and descripcion in agenda[fecha]:
        agenda[fecha].remove(descripcion)
        print("Evento eliminado.")
    else:
        print("No se encontró el evento.")

