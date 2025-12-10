from validaciones import validar_entero_positivo
from consulta import consultar_entradas

def eliminar_entrada(bitacora):
    consultar_entradas(bitacora)
    if not bitacora: return bitacora
    
    semana = validar_entero_positivo("\nSemana a eliminar: ")
    for i, entrada in enumerate(bitacora):
        if entrada['semana'] == semana:
            if input("¿Seguro? (s/n): ").lower() == 's':
                bitacora.pop(i)
                print("🗑️ Eliminado.")
            return bitacora
    print("⛔ No encontrada.")
    return bitacora