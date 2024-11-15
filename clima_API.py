import os
import requests
from dotenv import load_dotenv
from Settings import obtener_unidades
from errores import manejar_error_api
from datetime import datetime

load_dotenv()
api_key = os.getenv('api_key')  
base_url = "http://api.openweathermap.org/data/2.5/"
medidas = obtener_unidades()

def obtener_clima(ciudad):
    complete_url = f"{base_url}weather?q={ciudad}&appid={api_key}&lang=es&units={medidas}"
    response = requests.get(complete_url)
    manejar_error_api(response)

    if response.status_code != 200:
        return {"ciudad": ciudad, "error": "llamada mal hecha"}
    
    data = response.json()
    if "main" in data and "weather" in data:
        main = data["main"]
        temperature = main.get("temp", "No disponible")
        pressure = main.get("pressure", "No disponible")
        humidity = main.get("humidity", "No disponible")
        weather_desc = data["weather"][0].get("description", "No disponible")
        
        guardar_consulta(ciudad, temperature, pressure, humidity, weather_desc)
        
        return {
            "ciudad": ciudad,
            "temperatura": f"{temperature}°{unidad_medida()}",
            "presion": f"{pressure} hPa",
            "humedad": f"{humidity}%",
            "descripcion": weather_desc
        }
    else:
        return {"ciudad": ciudad, "error": "datos incompletos"}

def obtener_pronostico(ciudad):
    complete_url = f"{base_url}forecast?q={ciudad}&appid={api_key}&lang=es&units={medidas}"
    response = requests.get(complete_url)
    manejar_error_api(response)

    if response.status_code != 200:
        return {"ciudad": ciudad, "error": "llamada mal hecha"}
    
    data = response.json()
    if "list" in data:
        pronostico = []
        for item in data["list"]:
            fecha_hora = item["dt_txt"]
            temperatura = item["main"].get("temp", "No disponible")
            descripcion = item["weather"][0].get("description", "No disponible")
            pronostico.append({
                "fecha_hora": fecha_hora,
                "temperatura": f"{temperatura}°{unidad_medida()}",
                "descripcion": descripcion
            })
        return {
            "ciudad": ciudad,
            "pronostico": pronostico
        }
    else:
        return {"ciudad": ciudad, "error": "datos incompletos"}



def guardar_consulta(ciudad, temperatura, presion, humedad, descripcion):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("consultas_clima.txt", "a") as file:
        file.write(f"Fecha: {fecha}\n")
        file.write(f"Ciudad: {ciudad}\n")
        file.write(f"Temperatura: {temperatura}°{unidad_medida()}\n")
        file.write(f"Presion: {presion} hPa\n")
        file.write(f"Humedad: {humedad}%\n")
        file.write(f"Descripcion: {descripcion}\n")
        file.write("-------------------------\n")

def filtrar_por_ciudad(ciudad):
    try:
        with open("consultas_clima.txt", "r") as file:
            print(f"\nConsultas guardadas para la ciudad: {ciudad}")
            consultas = file.readlines()
            mostrar = False
            for linea in consultas:
                if "Ciudad:" in linea and ciudad.lower() in linea.lower():
                    mostrar = True
                if linea.strip() == "-------------------------":
                    mostrar = False
                if mostrar:
                    print(linea, end='')
    except FileNotFoundError:
        print("No hay consultas guardadas.")

def filtrar_por_fecha(fecha):
    try:
        with open("consultas_clima.txt", "r") as file:
            print(f"\nConsultas guardadas para la fecha: {fecha}")
            consultas = file.readlines()
            mostrar = False
            for linea in consultas:
                if "Fecha:" in linea and fecha in linea:
                    mostrar = True
                if linea.strip() == "-------------------------":
                    mostrar = False
                if mostrar:
                    print(linea, end='')
    except FileNotFoundError:
        print("No hay consultas guardadas.")



def unidad_medida():
    unidades = obtener_unidades()
    if unidades == "metric":
        return "C"
    elif unidades == "imperial":
        return "F"
    else:
        return "K"
    

