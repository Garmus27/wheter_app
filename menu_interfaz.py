<<<<<<< HEAD
from clima_API import obtener_clima, obtener_pronostico, filtrar_por_ciudad, filtrar_por_fecha
=======
from clima_API import obtener_clima, obtener_pronostico,filtrar_por_ciudad,filtrar_por_fecha,detectar_codificacion
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
from Settings import cambiar_unidades, obtener_unidades
from errores import ValidationError, APIError
from datetime import datetime

<<<<<<< HEAD
import pyfiglet
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def mostrar_menu():
    while True:
        # Crear el banner con pyfiglet
        banner = pyfiglet.figlet_format("Clima App", font="banner3-D")
        print(Fore.LIGHTRED_EX + banner)
        
        print(Fore.CYAN + "Menú:")
        print(Fore.GREEN + "1. Consultar clima")
        print(Fore.GREEN + "2. Consultar pronóstico a 5 días")
        print(Fore.GREEN + "3. Configuración")
        print(Fore.GREEN + "4. Ver consultas guardadas")
        print(Fore.GREEN + "5. Filtrar consultas por ciudad")
        print(Fore.GREEN + "6. Filtrar consultas por fecha")
        print(Fore.RED + "7. Salir")
        
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")
        
        if opcion == '1':
            try:
                ciudad = input(Fore.YELLOW + "Ingrese el nombre de la ciudad: ")
=======
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
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                clima = obtener_clima(ciudad)
                if clima.get("error"):
<<<<<<< HEAD
                    print(Fore.RED + f"Error al obtener el clima: {clima['error']}")
                else:
                    mostrar_clima(clima)
            except ValidationError as e:
                print(Fore.RED + str(e))
            except APIError as e:
                print(Fore.RED + str(e))
        elif opcion == '2':
            try:
                ciudad = input(Fore.YELLOW + "Ingrese el nombre de la ciudad: ")
=======
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
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                pronostico = obtener_pronostico(ciudad)
                if pronostico.get("error"):
<<<<<<< HEAD
                    print(Fore.RED + f"Error al obtener el pronóstico: {pronostico['error']}")
                else:
                    mostrar_pronostico(pronostico)
            except ValidationError as e:
                print(Fore.RED + str(e))
            except APIError as e:
                print(Fore.RED + str(e))
=======
                    print(f"Error al obtener el pronóstico: {pronostico['error']}")
                else:
                    mostrar_pronostico(pronostico)
            except ValidationError as e:
                print(e)
            except APIError as e:
                print(e)
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
        elif opcion == '3':
            mostrar_configuracion()
        elif opcion == '4':
            mostrar_consultas_guardadas()
        elif opcion == '5':
<<<<<<< HEAD
            ciudad = input(Fore.YELLOW + "Ingrese el nombre de la ciudad: ")
            filtrar_por_ciudad(ciudad)
        elif opcion == '6':
            fecha = input(Fore.YELLOW + "Ingrese la fecha (YYYY-MM-DD): ")
            filtrar_por_fecha(fecha)
        elif opcion == '7':
            print(Fore.RED + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, intente de nuevo.")

def mostrar_clima(clima):
    if "error" in clima:
        print(Fore.RED + f"\nError: {clima['error']}")
    else:
        print(Fore.CYAN + f"\nClima actual en {clima['ciudad']}:")
        print(Fore.CYAN + f"Temperatura: {clima['temperatura']}")
        print(Fore.CYAN + f"Presion: {clima['presion']}")
        print(Fore.CYAN + f"Humedad: {clima['humedad']}")
        print(Fore.CYAN + f"Descripcion: {clima['descripcion']}")

def mostrar_pronostico(pronostico):
    if "error" in pronostico:
        print(Fore.RED + f"\nError: {pronostico['error']}")
    else:
        print(Fore.CYAN + f"\nPronóstico a 5 días para {pronostico['ciudad']}:")
        for item in pronostico['pronostico']:
            print(Fore.CYAN + f"Fecha y hora: {item['fecha_hora']}")
            print(Fore.CYAN + f"Temperatura: {item['temperatura']}")
            print(Fore.CYAN + f"Descripcion: {item['descripcion']}")
            print(Fore.CYAN + "-------------------------")

def mostrar_configuracion():
    while True:
        print(Fore.CYAN + "\nConfiguración:")
        print(Fore.GREEN + "1. Cambiar unidades de medida")
        print(Fore.RED + "2. Volver al menú principal")
        
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")
        
        if opcion == '1':
            print(Fore.CYAN + "\nOpciones de unidades de medida:")
            print(Fore.GREEN + "1. Celsius")
            print(Fore.GREEN + "2. Fahrenheit")
            print(Fore.GREEN + "3. Kelvin")
            
            unidad = input(Fore.YELLOW + "Seleccione una unidad (1/2/3): ")
=======
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
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
            
            if unidad == '1':
                cambiar_unidades("metric")
            elif unidad == '2':
                cambiar_unidades("imperial")
            elif unidad == '3':
                cambiar_unidades("standard")
            else:
<<<<<<< HEAD
                print(Fore.RED + "Opción no válida. Se configurarán las unidades en Celsius por defecto.")
                cambiar_unidades("metric")
            
            print(Fore.CYAN + f"Unidades de medida establecidas a: {obtener_unidades()}")
        elif opcion == '2':
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, intente de nuevo.")

def mostrar_consultas_guardadas():
    try:
        with open("consultas_clima.txt", "r") as file:
            print(" ******************************************************")
            print(Fore.CYAN + "\nConsultas guardadas:")
            consultas = file.readlines()
            for consulta in consultas:
                print(consulta, end='')
            print(" ******************************************************")
    except FileNotFoundError:
        print(Fore.RED + "No hay consultas guardadas.")
=======
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



>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a

if __name__ == "__main__":
    mostrar_menu()





<<<<<<< HEAD


=======
>>>>>>> e445196bd51b30efa54b97a2a65843bb9d73fd6a
