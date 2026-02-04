#!/usr/bin/env python3
"""Calculadora CLI simple"""
def pedir_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def main():
    menu = """\nCalculadora simple
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Potencia (a^b)
6) Módulo (a % b)
q) Salir
Elige una opción: """
    while True:
        opcion = input(menu).strip().lower()
        if opcion == 'q':
            print("Hasta luego.")
            break
        if opcion in ('1','2','3','4','5','6'):
            a = pedir_numero("Número a: ")
            b = pedir_numero("Número b: ")
            if opcion == '1':
                res = a + b
            elif opcion == '2':
                res = a - b
            elif opcion == '3':
                res = a * b
            elif opcion == '4':
                if b == 0:
                    print("Error: división por cero.")
                    continue
                res = a / b
            elif opcion == '5':
                res = a ** b
            elif opcion == '6':
                if b == 0:
                    print("Error: módulo por cero.")
                    continue
                res = a % b
            print("Resultado:", res)
        else:
            print("Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    main()
