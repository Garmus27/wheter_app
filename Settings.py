# settings.py
unidades = "metric"

def cambiar_unidades(nuevas_unidades):
    global unidades
    unidades = nuevas_unidades

def obtener_unidades():
    return unidades
