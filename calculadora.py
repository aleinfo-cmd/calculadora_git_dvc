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
    return math.sin(math.radians(angulo))  # Calcula el seno.