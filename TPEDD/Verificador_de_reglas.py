from math import sqrt as raiz_cuadrada
class Verificador_reglas():
    def verificar_posicion_libre(self, tablero, valor, posicion, dimension):
        self.verificar_tamaño_del_tablero(tablero,dimension)
        columna_a_verificar=posicion[1]
        posicion_disponible=True
        longitud_submatriz=int(raiz_cuadrada(dimension))#el metodo devuelve float
        inicio_columna = (int(posicion[1] / longitud_submatriz)) * longitud_submatriz  #  ->pos 14 / 4 int le saca decimal
        inicio_fila = (int(posicion[0] / longitud_submatriz)) * longitud_submatriz
        for fila in range(inicio_fila,inicio_fila + longitud_submatriz):
            for columna in range(inicio_columna, inicio_columna + longitud_submatriz):
                if tablero[fila][columna] == valor:
                    posicion_disponible = False
                    return posicion_disponible

        fila_a_verificar=tablero[posicion[0]]
        if valor in fila_a_verificar:
            posicion_disponible = False
            return posicion_disponible

        for fila in range(dimension):
            if tablero[fila][columna_a_verificar] == valor:
                posicion_disponible = False
                return posicion_disponible
        return posicion_disponible

    def verificar_tamaño_del_tablero(self,tablero,dimension):
        tamaño_correcto=True
        for i in tablero:
            longitud_columna_temporal = len(i)
            if not longitud_columna_temporal == dimension:
                tamaño_correcto=False
                break
        return tamaño_correcto
    def verificar_valores_predeterminados_correctos(self,tablero,dimension):
        '''verifica que ningun valor del tablero ingresado sea mayor o menor de los permitidos'''
        for fila in range(dimension):
            for columna in range(dimension):
                if not 0<=tablero[fila][columna]<=dimension:
                    return False
        return True