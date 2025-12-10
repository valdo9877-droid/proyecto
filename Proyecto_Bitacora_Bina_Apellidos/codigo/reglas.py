# validaciones.py
def validar_entero_positivo(mensaje):
    """Valida que la entrada sea un número entero positivo (Semana)."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("⛔ Error: El número debe ser positivo.")
        except ValueError:
            print("⛔ Error: Debes ingresar un número entero.")

def validar_rango(mensaje, min_val, max_val): # <-- ¡Este nombre es CRÍTICO!
    """Valida que un número esté dentro de un rango (ej. Dominio 1-5)."""
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"⛔ Error: El valor debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("⛔ Error: Debes ingresar un número entero.")

def validar_texto_no_vacio(mensaje):
    """Valida que el texto ingresado para Actividades, Conceptos, etc., no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0:
            return texto
        else:
            print("⛔ Error: Este campo no puede estar vacío.")