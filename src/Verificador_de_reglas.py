from math import sqrt as raiz_cuadrada
class Verificador_reglas():
    def verificar_posicion_libre(self, tablero, valor, posicion, dimension): #posicion tupla (fila,columna)
        self.verificar_tamaño_del_tablero(tablero,dimension)
        fila_a_verificar = tablero[posicion[0]]
        columna_a_verificar=posicion[1]
        posicion_disponible=True

        ''' queda mejor sin modularizar? revisar funcion de fila'''
        submatriz_esta_disponible = self.verificar_si_es_posible_colocar_en_submatriz(posicion, dimension,tablero,valor)
        if not submatriz_esta_disponible:
            return submatriz_esta_disponible

        fila_esta_disponible=self.verificar_si_es_posible_colocar_en_la_fila(valor,fila_a_verificar)
        if not fila_esta_disponible:
            return fila_esta_disponible

        columna_esta_disponible=self.verificar_si_es_posible_colocar_en_la_columna(valor,columna_a_verificar,dimension,tablero)
        if not columna_esta_disponible:
            return columna_esta_disponible

        return posicion_disponible

    def verificar_si_es_posible_colocar_en_submatriz(self,posicion,dimension,tablero,valor_a_agregar):
        ''' Con dimension 9, hay 9 submatrices que a su vez tienen 9 posibles valores dentro
            El valor a agregar no puede encontrarse ya en la submatriz '''
        longitud_submatriz = int(raiz_cuadrada(dimension))  # el metodo devuelve float

        # serian las posiciones en la matriz mas grande que seria el sudoku completo
        posicion_inicial_de_columna = (int(posicion[1] / longitud_submatriz)) * longitud_submatriz  # ->pos 14 / 4 int le saca decimal
        posicion_inicial_de_fila = (int(posicion[0] / longitud_submatriz)) * longitud_submatriz
        posicion_disponible = True
        for fila in range(posicion_inicial_de_fila, posicion_inicial_de_fila + longitud_submatriz):
            for columna in range(posicion_inicial_de_columna, posicion_inicial_de_columna + longitud_submatriz):
                if tablero[fila][columna] == valor_a_agregar:
                    posicion_disponible = False
                    return posicion_disponible
        return posicion_disponible

    def verificar_si_es_posible_colocar_en_la_fila(self,valor_a_agregar,fila_a_verificar):
        ''' El valor a agregar no puede encontrarse en la fila a verificar '''
        posicion_disponible=True
        if valor_a_agregar in fila_a_verificar:
            posicion_disponible = False
            return posicion_disponible
        return posicion_disponible

    def verificar_si_es_posible_colocar_en_la_columna(self,valor_a_agregar,columna_a_verificar,dimension,tablero):
        ''' El valor a agregar no puede encontrarse en la columna a verificar '''
        posicion_disponible = True
        for fila in range(dimension): # en las diferentes filas
            if tablero[fila][columna_a_verificar] == valor_a_agregar: # comprueba la columna
                posicion_disponible = False
                return posicion_disponible
        return posicion_disponible


    def verificar_tamaño_del_tablero(self,tablero,dimension): # ver falta de datos, filas
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