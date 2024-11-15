# error_handling.py

class APIError(Exception):
    """Excepción personalizada para errores de la API."""
    def __init__(self, status_code, message="Error en la API"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    """Excepción personalizada para errores de validación."""
    def __init__(self, message="Error de validación"):
        self.message = message
        super().__init__(self.message)

def manejar_error_api(response):
    """Maneja errores de la API basados en el código de estado de la respuesta."""
    if response.status_code != 200:
        raise APIError(status_code=response.status_code, message=response.json().get('message', 'Error en la API'))

def manejar_error_entrada(invalid_input):
    """Maneja errores de validación de entrada del usuario."""
    raise ValidationError(message=f"Entrada inválida: {invalid_input}")
