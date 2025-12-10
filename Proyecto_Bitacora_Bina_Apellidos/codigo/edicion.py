from validaciones import validar_rango, validar_texto_no_vacio, validar_entero_positivo
from consulta import consultar_entradas

def editar_entrada(bitacora):
    consultar_entradas(bitacora)
    if not bitacora: return bitacora
    
    semana = validar_entero_positivo("\nSemana a editar: ")
    for entrada in bitacora:
        if entrada['semana'] == semana:
            print("1.Actividades 2.Conceptos 3.Problemas 4.Soluciones 5.Dominio 6.Cancelar")
            opcion = validar_rango("Opción: ", 1, 6)
            if opcion == 1: entrada['actividades'] = validar_texto_no_vacio("Nuevo valor: ")
            elif opcion == 2: entrada['conceptos'] = validar_texto_no_vacio("Nuevo valor: ")
            elif opcion == 3: entrada['problemas'] = validar_texto_no_vacio("Nuevo valor: ")
            elif opcion == 4: entrada['soluciones'] = validar_texto_no_vacio("Nuevo valor: ")
            elif opcion == 5: entrada['dominio'] = validar_rango("Nuevo dominio (1-5): ", 1, 5)
            print("✅ Editado.")
            return bitacora
    print("⛔ No encontrada.")
    return bitacora