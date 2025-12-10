# --- IMPORTACIONES ---
import captura
import consulta
import edicion
import eliminacion
import exportacion
import validaciones
# ---------------------

def menu():
    """Función principal que muestra el menú y gestiona el flujo del programa con mejor formato."""
    # La lista principal de diccionarios, donde se guardan las entradas.
    bitacora = [] 
    
    while True:
        print("\n╔═══════════════════════════════════╗")
        print("║ ★ SISTEMA DE BITÁCORA DE APRENDIZAJE ║")
        print("╚═══════════════════════════════════╝")
        print("   [Opciones Disponibles]")
        print("  » 1. Agregar nueva entrada")
        print("  » 2. Consultar entradas")
        print("  » 3. Editar entrada")
        print("  » 4. Eliminar entrada")
        print("  » 5. Generar archivo (Exportar)")
        print("  » 6. Salir")
        print("═" * 35)
        
        try:
            # Aquí llamamos a la función de validaciones (validar_rango) para la opción
            # Como importamos 'validaciones', llamamos a sus funciones con el prefijo 'validaciones.'
            opcion_str = input("  ► Seleccione una opción (1-6): ")
            opcion = int(opcion_str)
        except ValueError:
            print("⛔ Error: Ingrese un número válido.")
            continue
        
        # Validación de rango de la opción
        if not (1 <= opcion <= 6):
            print("⛔ Error: Opción fuera de rango (1-6).")
            continue

        # Lógica del programa (Aquí usamos los prefijos de importación: captura., consulta., etc.)
        if opcion == 1:
            bitacora = captura.agregar_entrada(bitacora) 
        elif opcion == 2:
            consulta.consultar_entradas(bitacora)
        elif opcion == 3:
            bitacora = edicion.editar_entrada(bitacora)
        elif opcion == 4:
            bitacora = eliminacion.eliminar_entrada(bitacora)
        elif opcion == 5:
            exportacion.generar_archivo(bitacora)
        elif opcion == 6:
            print("\n👋 Cerrando sistema. ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()