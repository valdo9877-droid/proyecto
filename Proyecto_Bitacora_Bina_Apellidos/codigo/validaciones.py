def validar_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0: return valor
            print("⛔ Error: El número debe ser positivo.")
        except ValueError:
            print("⛔ Error: Debes ingresar un número entero.")

def validar_rango(mensaje, min_val, max_val):
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val: return valor
            print(f"⛔ Error: El valor debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("⛔ Error: Debes ingresar un número entero.")

def validar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0: return texto
        print("⛔ Error: Este campo no puede estar vacío.")