#FUNCIONES

#rama magdiel
def datos_magdiel():
    print (f"Mi nombre es Magdiel Esther Reynoso Ramirez y tengo 22 años.")
  

#rama juan
def datos_juan():
    print("Mi nombre es Juan Pablo Taulis y tengo 18 años.")
    
    
#rama franco
def datos_franco():
     print("Mi nombre es Franco Inostroza y tengo 26 años.")

#rama mario
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
        datos_magdiel()
    elif op == "3":
        datos_mario()
    elif op == "4":
        datos_juan()

    else:
        print(" Opción inválida.")
