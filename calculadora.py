import math
def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def seno(angulo):                # Recibe un ángulo en grados.
    return math.sin(math.radians(angulo))
      # Calcula el seno.
def coseno(angulo):
    return math.cos(math.radians(angulo))
      # Calcula el coseno.
def tangente(angulo):
    return math.tan(math.radians(angulo))
      # Calcula la tangente.
def exponencial(x):                # Calcula la función exponencial.
    return math.exp(x)             # Devuelve e elevado a x.
def logaritmo(x):                  # Calcula el logaritmo natural.
    if x <= 0:                    # Comprueba que x sea positivo.
        raise ValueError("x debe ser positivo")
    return math.log(x)            # Devuelve ln(x).