from clima_API import obtener_clima, obtener_pronostico,filtrar_por_ciudad,filtrar_por_fecha,detectar_codificacion
from Settings import cambiar_unidades, obtener_unidades
from errores import ValidationError, APIError
from datetime import datetime

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Consultar clima")
        print("2. Consultar pronóstico a 5 días")
        print("3. Configuración")
        print("4. Ver consultas guardadas")
        print("5. Filtrar consultas por ciudad")
        print("6. Filtrar consultas por fecha")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                ciudad = input("Ingrese el nombre de la ciudad: ")
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                clima = obtener_clima(ciudad)
                if clima.get("error"):
                    print(f"Error al obtener el clima: {clima['error']}")
                else:
                    mostrar_clima(clima)
            except ValidationError as e:
                print(e)
            except APIError as e:
                print(e)
        elif opcion == '2':
            try:
                ciudad = input("Ingrese el nombre de la ciudad: ")
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                pronostico = obtener_pronostico(ciudad)
                if pronostico.get("error"):
                    print(f"Error al obtener el pronóstico: {pronostico['error']}")
                else:
                    mostrar_pronostico(pronostico)
            except ValidationError as e:
                print(e)
            except APIError as e:
                print(e)
        elif opcion == '3':
            mostrar_configuracion()
        elif opcion == '4':
            mostrar_consultas_guardadas()
        elif opcion == '5':
            ciudad = input("Ingrese el nombre de la ciudad: ")
            filtrar_por_ciudad(ciudad)
        elif opcion == '6':
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            filtrar_por_fecha(fecha)
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def mostrar_clima(clima):
    if "error" in clima:
        print(f"\nError: {clima['error']}")
    else:
        print(f"\nClima actual en {clima['ciudad']}:")
        print(f"Temperatura: {clima['temperatura']}")
        print(f"Presion: {clima['presion']}")
        print(f"Humedad: {clima['humedad']}")
        print(f"Descripcion: {clima['descripcion']}")

def mostrar_pronostico(pronostico):
    if "error" in pronostico:
        print(f"\nError: {pronostico['error']}")
    else:
        print(f"\nPronóstico a 5 días para {pronostico['ciudad']}:")
        for item in pronostico['pronostico']:
            print(f"Fecha y hora: {item['fecha_hora']}")
            print(f"Temperatura: {item['temperatura']}")
            print(f"Descripcion: {item['descripcion']}")
            print("-------------------------")

def mostrar_configuracion():
    while True:
        print("\nConfiguración:")
        print("1. Cambiar unidades de medida")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\nOpciones de unidades de medida:")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin")
            
            unidad = input("Seleccione una unidad (1/2/3): ")
            
            if unidad == '1':
                cambiar_unidades("metric")
            elif unidad == '2':
                cambiar_unidades("imperial")
            elif unidad == '3':
                cambiar_unidades("standard")
            else:
                print("Opción no válida. Se configurarán las unidades en Celsius por defecto.")
                cambiar_unidades("metric")
            
            print(f"Unidades de medida establecidas a: {obtener_unidades()}")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
codificacion = detectar_codificacion("consultas_clima.txt")


        
def mostrar_consultas_guardadas():
    try:
        codificacion = detectar_codificacion("consultas_clima.txt")
        with open("consultas_clima.txt", "r", encoding=codificacion) as file:
            print("-------------------------------------------------------")
            print("\nConsultas guardadas:")
            consultas = file.readlines()  # Leer todas las líneas del archivo
            
            # Para mostrar cada consulta como un bloque separado
            consulta_actual = []
            for linea in consultas:
                if linea.strip() == "-------------------------":
                    if consulta_actual:
                        print("".join(consulta_actual))  # Imprimir el bloque completo de la consulta
                        print("-------------------------------------------------------")
                        consulta_actual = []  # Resetear para la siguiente consulta
                else:
                    consulta_actual.append(linea)  # Agregar línea a la consulta actual
            
            # Imprimir cualquier consulta pendiente al final
            if consulta_actual:
                print("".join(consulta_actual))
                print("-------------------------------------------------------")
    except FileNotFoundError:
        print("No hay consultas guardadas.")




if __name__ == "__main__":
    mostrar_menu()





