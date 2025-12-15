# ==============================
# PROGRAMACIÓN TRADICIONAL
# Promedio semanal del clima
# ==============================

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana.
    Retorna una lista con 7 valores.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal del programa.
    """
    print("PROMEDIO SEMANAL DEL CLIMA - PROGRAMACIÓN TRADICIONAL")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal es: {promedio:.2f} °C")


# Ejecutar el programa
main()
