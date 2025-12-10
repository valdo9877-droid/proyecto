def consultar_entradas(bitacora):
    print("\n--- 📖 CONSULTAR BITÁCORA ---")
    if not bitacora:
        print("La bitácora está vacía.")
        return
    
    ordenada = sorted(bitacora, key=lambda x: x['semana'])
    for e in ordenada:
        print("="*40)
        print(f"SEMANA: {e['semana']}")
        print(f"Actividades: {e['actividades']}")
        print(f"Conceptos: {e['conceptos']}")
        print(f"Problemas: {e['problemas']}")
        print(f"Soluciones: {e['soluciones']}")
        print(f"Dominio: {e['dominio']}/5")
    print("="*40)