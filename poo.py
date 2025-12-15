# =========================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Promedio semanal del clima
# =========================================

class Clima:
    """
    Clase base (superclase)
    Representa información general del clima.
    """

    def __init__(self):
        self._temperaturas = []  # Encapsulamiento

    def ingresar_temperaturas(self):
        """
        Método genérico para ingresar temperaturas.
        Será sobrescrito (polimorfismo).
        """
        pass

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas.
        """
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(Clima):
    """
    Clase hija que hereda de Clima
    Aplica HERENCIA y POLIMORFISMO
    """

    def ingresar_temperaturas(self):
        """
        Sobrescritura del método (POLIMORFISMO)
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)


def main():
    """
    Función principal
    """
    print("PROMEDIO SEMANAL DEL CLIMA - POO")

    # Polimorfismo: objeto de tipo ClimaSemanal
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print(f"El promedio semanal es: {promedio:.2f} °C")


# Ejecutar el programa
main()
