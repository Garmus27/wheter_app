print ("hello world")



def guardar_en_historial(consulta):
    historial = cargar_historial()
    fecha_actual = datetime.now().isoformat()
    historial.append()

def filtrar_historial(dias):
    historial = cargar_historial()
    limite = datetime.now() - timedelta(days=dias)
    return [item for item in historial if datetime.fromisoformat(item["fecha"]) >= limite]

print("=== Menú Historial ===")
print("1. Ver últimos 15 días")
print("2. Ver últimos 30 días")
print("3. Salir")
opcion = input("Elige una opción: ")

if opcion == "1":
    resultados = filtrar_historial(15)
elif opcion == "2":
        resultados = filtrar_historial(30)
elif opcion == "3":
    print("Saliendo del programa...")
    break
else:
    print("Opción no válida. Intenta nuevamente.")
