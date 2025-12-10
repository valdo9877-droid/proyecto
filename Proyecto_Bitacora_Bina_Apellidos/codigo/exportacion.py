from validaciones import validar_texto_no_vacio

def generar_archivo(bitacora):
    if not bitacora:
        print("Vacía. Nada que exportar.")
        return
    nombre = validar_texto_no_vacio("Tu nombre (sin espacios): ")
    archivo_nom = f"Bitacora_{nombre}.txt"
    try:
        with open(archivo_nom, "w", encoding="utf-8") as f:
            f.write(f"BITÁCORA - {nombre}\n\n")
            for e in sorted(bitacora, key=lambda x: x['semana']):
                f.write(f"SEMANA {e['semana']}\nDom: {e['dominio']}/5\nAct: {e['actividades']}\n----------------\n")
            concl = validar_texto_no_vacio("Conclusión final: ")
            f.write(f"\nCONCLUSIÓN:\n{concl}")
        print(f"✅ Archivo {archivo_nom} creado.")
    except Exception as e:
        print(f"Error: {e}")