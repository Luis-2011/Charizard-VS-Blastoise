import random 
vida_blastoise = 100
vida_charizard = 100
print ("Entrenador Red te reta a un combate...")
opcion = input ("¿Aceptas el reto? (Si/No): ")
if opcion == "Si": 
    print ("¡Comienza el combate!")

    while vida_blastoise > 0 and vida_charizard > 0:

        print("\nVida Charizard:", vida_charizard)
        print("\nTu Vida:", vida_blastoise)
        eleccion_movimientob = input("\nQue movimiento eliges? (Hidrobomba, Burbuja, Arañazo, Placaje): ")
        if eleccion_movimientob == "Hidrobomba":
            daño = 50
        elif eleccion_movimientob == "Burbuja":
            daño = 30
        elif eleccion_movimientob == "Arañazo":
            daño = 15
        elif eleccion_movimientob == "Placaje":
            daño = 10
        else:
            print("Movimiento no válido")
            continue  
        vida_charizard -= daño
        print("¡Hiciste", daño, "de daño!")
        movimientos_epicos_charizard = ["Lanzallamas", "Ascuas", "Garra Metal", "Placaje"]
        eleccion_movimientoc = random.choice(movimientos_epicos_charizard)
        if eleccion_movimientoc == "Lanzallamas":
            daño_charizard = 50
        elif eleccion_movimientoc == "Ascuas":
            daño_charizard = 30
        elif eleccion_movimientoc == "Garra Metal":
            daño_charizard = 15
        elif eleccion_movimientoc == "Placaje":
            daño_charizard = 10
        print (f"Charizard te hizo {daño_charizard} de daño usando {eleccion_movimientoc}")
        vida_blastoise -= daño_charizard
        if vida_blastoise <= 0 and vida_charizard <= 0:
            print("Empate")
        elif vida_charizard <= 0:
            print("¡Ganaste!")
            input ("Presione Enter para salir")
        elif vida_blastoise <= 0:
            print("Perdiste...")
            input ("Presione Enter para salir")
        vida_charizard = max(0, vida_charizard)
        vida_blastoise = max(0, vida_blastoise)
elif opcion == "No":
    print ("Cobarde... Fin del juego")
    input ("Presione Enter para salir")