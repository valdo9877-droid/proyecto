from validaciones import validar_entero_positivo, validar_texto_no_vacio, validar_rango

def agregar_entrada(bitacora):
    print("\n--- ➕ AGREGAR NUEVA ENTRADA ---")
    semana = validar_entero_positivo("Ingrese el número de semana: ")
    actividades = validar_texto_no_vacio("Actividades realizadas: ")
    conceptos = validar_texto_no_vacio("Conceptos aprendidos: ")
    problemas = validar_texto_no_vacio("Problemas encontrados: ")
    soluciones = validar_texto_no_vacio("Soluciones aplicadas: ")
    dominio = validar_rango("Nivel de dominio (escala 1-5): ", 1, 5)

    nueva_entrada = {
        "semana": semana,
        "actividades": actividades,
        "conceptos": conceptos,
        "problemas": problemas,
        "soluciones": soluciones,
        "dominio": dominio
    }
    bitacora.append(nueva_entrada)
    print("✅ Entrada registrada exitosamente.")
    return bitacora