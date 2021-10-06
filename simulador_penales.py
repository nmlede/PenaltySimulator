import random


# Variables
opciones_lados = ("derecha","izquierda","medio")
opciones_altura = ("arriba","abajo","medio")
marcador_usuario = []
marcador_programa = []

# Funciones
def Patear():
    chances_fallar = random.randint(1,2)
    opcion_jugador = input("\n\tIngrese un lado\n-Derecha\n-Izquierda\n-Medio\nSeleccion: ").lower()
    opcion_pc = random.choice(opciones_lados)
    if opcion_jugador == opcion_pc:
        print("\nEl arquero adivina, se tira para el mismo lado")
        opcion_jugador = input("\n\tIngrese una altura\n-Arriba\n-Abajo\n-Medio\nSeleccion: ").lower()
        opcion_pc = random.choice(opciones_altura)
        if opcion_jugador == opcion_pc:
            print("\nAtaja el arquero")
            marcador_usuario.insert(i,'X')
        else:
            if chances_fallar == 1:
                print("\nGol")
                marcador_usuario.insert(i,'O')
            else:    
                print("\nAfuera")
                marcador_usuario.insert(i,'X')
    else:
        if chances_fallar == 1:
            print("\nGol")
            marcador_usuario.insert(i,'O')
        else:
            print("\nAfuera")
            marcador_usuario.insert(i,'X') 

def Atajar():
    chances_fallar = random.randint(1,2)
    opcion_jugador = input("\n\tIngresa un lado\n-Derecha\n-Izquierda\n-Medio\nSeleccion: ").lower()
    opcion_pc = random.choice(opciones_lados)
    if opcion_jugador == opcion_pc:
        print("\nAdivinaste el lado")
        opcion_jugador = input("\n\tIngresa la altura\n-Arriba\n-Abajo\n-Medio\nSeleccion: ").lower()
        opcion_pc = random.choice(opciones_altura)
        if opcion_jugador == opcion_pc:
            print("\nAtajaste")
            marcador_programa.insert(i,'X')
        else:
            if chances_fallar == 1:
                print("\nGol")
                marcador_programa.insert(i,'O')
            else:
                print("\nAfuera")
                marcador_programa.insert(i,'X')
    else:
        if chances_fallar == 1:
            print("\nGol")
            marcador_programa.insert(i,'O')
        else:
            print("\nAfuera")
            marcador_programa.insert(i,'X')


if __name__ == "__main__":
    print("     ________________________________     ")
    print("     |                              |     ")
    print("     |                              |     ")
    print("     |       Penalty Simulator      |     ")
    print("     |                              |     ")
    print("_____|______________________________|_____")
    print("                                          ")
    print("                                          ")

    for i in range(5):
        print("\nTurno de patear!")
        Patear()
        print("\nTurno de atajar!")
        Atajar()
    
    print(f"\nResultado final:\nUsuario: {marcador_usuario}\nPrograma: {marcador_programa}")
    print("\nFin del programa")

"""
    Todo:
    Ponerlo mas bonito.
    Modulizar.
"""
