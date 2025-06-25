
def datos_franco():
     print("Mi nombre es Franco Inoostroza y tengo 26 años.")


def datos_mario():
    print("Mi nombre es mario contreras y tengo 28 años.")

  
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("4. Función de integrante 4")
    print("0. Salir")
    
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_franco()   
    elif op == "2":
    
    
    elif op == "3":
        datos_mario()
        
    elif op == "4":
    pass 

    else:
        print(" Opción inválida.")
