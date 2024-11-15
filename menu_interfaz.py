from clima_API import obtener_clima, obtener_pronostico, filtrar_por_ciudad, filtrar_por_fecha
from Settings import cambiar_unidades, obtener_unidades
from errores import ValidationError, APIError
from datetime import datetime

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
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                clima = obtener_clima(ciudad)
                if clima.get("error"):
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
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                pronostico = obtener_pronostico(ciudad)
                if pronostico.get("error"):
                    print(Fore.RED + f"Error al obtener el pronóstico: {pronostico['error']}")
                else:
                    mostrar_pronostico(pronostico)
            except ValidationError as e:
                print(Fore.RED + str(e))
            except APIError as e:
                print(Fore.RED + str(e))
        elif opcion == '3':
            mostrar_configuracion()
        elif opcion == '4':
            mostrar_consultas_guardadas()
        elif opcion == '5':
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
            
            if unidad == '1':
                cambiar_unidades("metric")
            elif unidad == '2':
                cambiar_unidades("imperial")
            elif unidad == '3':
                cambiar_unidades("standard")
            else:
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

if __name__ == "__main__":
    mostrar_menu()







