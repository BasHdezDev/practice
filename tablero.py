from linkedlist import LinkedList


class Tablero:
    def __init__(self, tamano):
        self.tamano: int = tamano
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = LinkedList()

        for i in range(self.tamano):
            fila = LinkedList()
            for j in range(self.tamano):
                fila.add_head(None)
            tablero.add_head(fila)

        return tablero

    def mostrar_tablero(self):
        fila = self.tablero.head
        while fila:
            col = fila.value.head
            fila_mostrar = ''
            while col:
                fila_mostrar += col.value
                col = col.next
            print(fila_mostrar)
            fila = fila.next

    def celdas(self):
        celdas = '🔳'

        fila = self.tablero.head
        while fila:
            col = fila.value.head
            while col:
                if col.value is None:
                    col.value = celdas
                col = col.next
            fila = fila.next


    def posicion_inicial_x(self):
        fila = self.tamano - 1
        col = (self.tamano // 2)

        self.cambiar_casilla(fila, col, '❌')

        return fila, col

    def posicion_inicial_y(self):
        fila = 0
        col = (self.tamano // 2)

        self.cambiar_casilla(fila, col, '🤖')

        return fila, col

    def verificar_posicion(self, fila: int, col: int):
        validacion: bool = 0 <= fila < self.tamano and 0 <= col < self.tamano
        
        return validacion

    def obtener_posicion(self, fila, col):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        return current.value

    def cambiar_casilla(self, fila, col, valor):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        current.value = valor


    def punto_medio(self):
        fila_punto_medio = self.tamano//2
        col_punto_medio = self.tamano//2

        return fila_punto_medio , col_punto_medio

    

    def verificar_camino_por_el_punto(self, i_pos, fila_ganar, fila_bloqueo, col_bloqueo, paso_por_el_centro = None):

        fila, col = i_pos
        casilla_original = self.obtener_posicion(fila_bloqueo, col_bloqueo)
        self.cambiar_casilla(fila_bloqueo, col_bloqueo, "⛔")

        if fila == fila_ganar and paso_por_el_centro:
            return True
        

        valor_actual = self.obtener_posicion(fila, col)
        punto = self.punto_medio()
        if i_pos == punto:
            paso_por_el_centro = True
        

        self.cambiar_casilla(fila, col, "0")

        direcciones = LinkedList()
        direcciones.add_head((-1,0))
        direcciones.add_head((0,-1))
        direcciones.add_head((1,0))
        direcciones.add_head((0,1))

        current = direcciones.head

        while current:

            temp_mov_f, temp_mov_c = current.value
            nueva_fila, nueva_col = fila + temp_mov_f, col + temp_mov_c

            if self.verificar_posicion(nueva_fila, nueva_col):
                if self.obtener_posicion(nueva_fila, nueva_col) != "0":
                    if self.obtener_posicion(nueva_fila, nueva_col) != "⛔":
                        if self.verificar_camino_por_el_punto((nueva_fila, nueva_col), fila_ganar, fila_bloqueo, col_bloqueo, paso_por_el_centro):
                            self.cambiar_casilla(fila, col, valor_actual)
                            self.cambiar_casilla(fila_bloqueo, col_bloqueo, casilla_original)
                            return True
                        
            current = current.next
                            
        self.cambiar_casilla(fila, col, valor_actual)
        self.cambiar_casilla(fila_bloqueo, col_bloqueo, casilla_original)

        return False
