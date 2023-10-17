from random import randint
from tablero import Tablero


class Juego:
    def __init__(self, tablero: Tablero):
        self.tablero = tablero
        self.pos_x = None
        self.pos_y = None

    def iniciar_x(self):
        self.pos_x = self.tablero.posicion_inicial_x()

    def iniciar_y(self):
        self.pos_y = self.tablero.posicion_inicial_y()

    def casilla_pasar_ganar(self):
        fila = 1
        col = 0
        self.tablero.cambiar_casilla(fila, col, "🟨")

    def movimiento_x(self):
        while True:
            direccion = input("Movimiento:\n1: arriba\n2: abajo\n3: izquierda\n4: derecha\n->  ")

            
            nueva_fila, nueva_col = self.pos_x

            if direccion == "1":
                nueva_fila -= 1
            elif direccion == "2":
                nueva_fila += 1
            elif direccion == "3":
                nueva_col -= 1
            elif direccion == "4":
                nueva_col += 1
            else:
                print('Ingrese 1, 2, 3 o 4')
                continue

            if self.tablero.verificar_posicion(nueva_fila, nueva_col):
                node_value = self.tablero.obtener_posicion(nueva_fila, nueva_col)

                if node_value == '⛔':
                    print("La celda está bloqueada, intente de nuevo")
                    continue

                if node_value == '🤖':
                    fila_salto, col_salto = self.saltar_dos_veces(nueva_fila, nueva_col, direccion, self.pos_x)
                    self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                    self.pos_x = (fila_salto, col_salto)
                    self.tablero.cambiar_casilla(fila_salto, col_salto, '❌')
                    return

                else:
                    self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                    self.tablero.cambiar_casilla(nueva_fila, nueva_col, '❌')
                self.pos_x = (nueva_fila, nueva_col)
                return

            else:
                print("No puedes hacer ese movimiento")
                continue



    def movimiento_y(self):
        while True:
            direccion = str(randint(1, 4))
            nueva_fila, nueva_col = self.pos_y

            if direccion == "1":
                nueva_fila -= 1
            elif direccion == "2":
                nueva_fila += 1
            elif direccion == "3":
                nueva_col -= 1
            elif direccion == "4":
                nueva_col += 1
            else:
                continue

            if self.tablero.verificar_posicion(nueva_fila, nueva_col):
                valor_nodo = self.tablero.obtener_posicion(nueva_fila, nueva_col)

                if valor_nodo == '⛔':
                    continue

                if valor_nodo == '❌':
                    fila_salto, col_salto = self.saltar_dos_veces(nueva_fila, nueva_col, direccion, self.pos_y)
                    self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                    self.pos_y = (fila_salto, col_salto)
                    self.tablero.cambiar_casilla(fila_salto, col_salto, '🤖')
                    return

                else:
                    self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                    self.tablero.cambiar_casilla(nueva_fila, nueva_col, '🤖')
                self.pos_y = (nueva_fila, nueva_col)
                return
            else:
                continue

    def bloqueo_x(self):
        while True:
            fila = int(input("Fila a bloquear ->  "))
            col = int(input("Columna a bloquear ->  "))

            if not self.tablero.verificar_posicion(fila, col):
                print()
                print("Posición invalida ")
                continue

            if self.tablero.verificar_camino_por_el_punto(self.pos_x, 0, fila, col) == False or self.tablero.verificar_camino_por_el_punto(self.pos_y, self.tablero.tamano -1, fila, col) == False:
                print("\nNo puedes bloquear acá porque no queda camino disponible para ganar\n")
                continue

            if self.tablero.obtener_posicion(fila, col) == '⛔':
                print()
                print("\nLa celda ya está bloqueada\n")
                continue

            if self.tablero.obtener_posicion(fila, col) == '🤖' or self.tablero.obtener_posicion(fila, col) == '❌':
                print("\nHay un jugador en la celda\n")
                continue

            self.tablero.cambiar_casilla(fila, col, '⛔')
            break

    def bloqueo_y(self):
        while True:
            fila = randint(0, self.tablero.tamano)
            col = randint(0, self.tablero.tamano)

            if not self.tablero.verificar_posicion(fila, col):
                continue

            if self.tablero.verificar_camino_por_el_punto(self.pos_x, 0, fila, col) == False or self.tablero.verificar_camino_por_el_punto(self.pos_y, self.tablero.tamano -1, fila, col) == False:
                continue

            if self.tablero.obtener_posicion(fila, col) == '⛔':
                continue

            if self.tablero.obtener_posicion(fila, col) == '🤖' or self.tablero.obtener_posicion(fila, col) == '❌':
                continue

            self.tablero.cambiar_casilla(fila, col, '⛔')
            break

    def verificar_ganador(self):

        filax, colx = self.pos_x
        if filax == 0:
            return "\n!!!!!!!!!!!!!!!!El jugador X gana!!!!!!!!!!!!!!!"
        filay, coly = self.pos_y
        if filay == self.tablero.tamano - 1:
            self.tablero.mostrar_tablero()
            return "\nLa maquina gana :("
        else:
            return None

    def saltar_dos_veces(self, fila, col, direccion, pos):
        if direccion == "1":
            fila -= 1
        elif direccion == "2":
            fila += 1
        elif direccion == "3":
            col -= 1
        elif direccion == "4":
            col += 1

        if not self.tablero.verificar_posicion(fila, col):
            print("No te puedes salir de los bordes")
            fila, col = pos

        valor = self.tablero.obtener_posicion(fila, col)
        if valor == '⛔':
            print("La celda está bloqueada")
            fila, col = pos

        return fila, col
    
    def punto_por_donde_pasa(self,fila,col):
        if self.tablero.verificar_posicion(fila,col):
            self.tablero.cambiar_casilla(fila,col,'🌲')
        else:
            print("Tiene que poner el punto dentro de los limites del tablero")
                

def menu_crear_tablero():
    while True:
        tamano_tablero = int(input("\nIngresa el tamaño del tablero\n-> "))
        print("")
        if tamano_tablero < 3:
            print("El tablero debe ser minimo de 3x3")
            continue
        tablero = Tablero(tamano_tablero)
        juego = Juego(tablero)
        menu_inicio(tablero, juego)

def menu_inicio(tablero, juego):
    while True:
        opcion = input("Menú del juego\n1. Iniciar\n2. Salir\n-> ")
        print("\n Iniciando el juego \n")
        if opcion == "1":

            fila = int(input("Digite la fila por donde quiere que pase el punto: "))
            col = int(input("Digite la columna por donde quiere que pase el punto: "))
            tablero.celdas()
            juego.iniciar_x()
            juego.iniciar_y()

            juego.punto_por_donde_pasa(fila,col)
            menu_turnos(tablero, juego)
            break

        elif opcion == "2":
            break

        else:
            print('Opción invalida, ingrese 1 o 2')
            continue

def menu_turnos(tablero, juego):
    while True:
        tablero.mostrar_tablero()

        print("\nTurno del jugador X\n")
        opcion_x = input("1. Moverse\n2. Bloquear casilla\n-> ")
        if opcion_x == "1":
            juego.movimiento_x()
        elif opcion_x == "2":
            juego.bloqueo_x()
        else:
            print("Ingrese 1 o 2")
            continue
        
        
        ganador = juego.verificar_ganador()
        if ganador:
            print(ganador)
            quit()
        
        print("\nTurno de la maquina\n")

        opcion_y  = str(randint(1, 2))
        if opcion_y  == "1":
            juego.movimiento_y()
        if opcion_y  == "2":
            juego.bloqueo_y()
        
        ganador = juego.verificar_ganador()
        if ganador:
            print(ganador)
            quit()

        menu_turnos(tablero, juego)


menu_crear_tablero()
