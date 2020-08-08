import unittest
#from  EDD-Solver-Sudoku.src.Verificador_de_reglas import *
from src.Verificador_de_reglas import *

''' va a tener las siguientes funciones iniciales:

verificar_tamaño_del_tablero(self,tablero,dimension)
    verificar_posicion_libre(self, tablero, valor, posicion, dimension)
verificar_valores_predeterminados_correctos(self,tablero,dimension)

'''
class Verificador_de_reglas_tests(unittest.TestCase):
    '''tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]'''

    def test_comprobar_que_el_tablero_como_lista_de_lista_tenga_dimension_9(self):
        tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        dimension=len(tablero_con_ceros[0])
        tablero_tiene_dimension_9=True
        self.assertEqual(Verificador_reglas().verificar_tamaño_del_tablero(tablero_con_ceros, dimension),tablero_tiene_dimension_9)

    def test_comprobar_que_la_posicion_en_un_tablero_vacio_sea_valida(self):
        ''' Esta vacio el tablero asi que tendria que ser valida la posicion, se espera True '''
        tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        dimension=len(tablero_con_ceros[0])
        es_una_posicion_valida_5_5=True
        valor_a_agregar=5
        posicion_a_verificar=(5,5)#(fila,columna)
        self.assertEqual(Verificador_reglas().verificar_posicion_libre(tablero_con_ceros, valor_a_agregar, posicion_a_verificar, dimension),es_una_posicion_valida_5_5)

    def test_comprobar_que_el_tablero_contenga_numeros_0_a_9(self):
        ''' Deberia de devolver true, ya que el tablero solo tendra valores 0. Dimension 9'''
        tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        dimension=len(tablero_con_ceros[0])
        valores_del_tablero_son_correctos=True
        self.assertEqual(Verificador_reglas().verificar_valores_predeterminados_correctos(tablero_con_ceros, dimension),valores_del_tablero_son_correctos)

    def test_comprobar_que_el_tablero_NO_contenga_numeros_0_a_9s(self):
        ''' Deberia de devolver false, ya que el tablero tendra un 20 cuando su dimension es 9'''
        tablero_con_valor_incorrecto = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 20, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        dimension=len(tablero_con_valor_incorrecto[0])
        valores_del_tablero_son_correctos=False
        self.assertEqual(Verificador_reglas().verificar_valores_predeterminados_correctos(tablero_con_valor_incorrecto, dimension),valores_del_tablero_son_correctos)

    def test_comprobar_que_sea_posible_colocar_en_fila_de_una_posicion_especifica_(self):
        ''' Deberia de devolver true ya que esta todo el tablero en 0 y no hay repeticion del valor 4'''
        tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        valor_a_agregar = 4  # no puede estar el 4 en esa misma fila
        fila_a_verificar=tablero_con_ceros[0]
        no_hay_valor_repetido_en_fila=True
        self.assertEqual(Verificador_reglas().verificar_si_es_posible_colocar_en_la_fila(valor_a_agregar, fila_a_verificar),no_hay_valor_repetido_en_fila)

    def test_comprobar_error_al_colocar__valor_repetido_en_fila_de_una_posicion_especifica_(self):
        ''' Deberia de devolver false ya que el valor 2 esta repetido en la primer fila'''
        tablero_con_valor_repetido = [[0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        valor_a_agregar = 2  # no puede estar el 4 en esa misma fila
        fila_a_verificar=tablero_con_valor_repetido[0]
        no_hay_valor_repetido_en_fila=False
        self.assertEqual(Verificador_reglas().verificar_si_es_posible_colocar_en_la_fila(valor_a_agregar, fila_a_verificar),no_hay_valor_repetido_en_fila)

    def test_comprobar_que_no_haya_valor_repetido_en_la_columna(self):
        ''' Deberia de devolver true ya que el valor 2 no esta repetido en la columna'''
        tablero_con_ceros = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        valor_a_agregar = 2  # no puede estar el 4 en esa misma fila
        columna_a_verificar=1
        dimension=len(tablero_con_ceros[0])
        no_hay_valor_repetido_en_columna=True #valor_a_agregar,columna_a_verificar,dimension,tablero
        self.assertEqual(Verificador_reglas().verificar_si_es_posible_colocar_en_la_columna(valor_a_agregar, columna_a_verificar,dimension,tablero_con_ceros),no_hay_valor_repetido_en_columna)

    def test_comprobar_que_de_false_al_verificar_repeticion_del_valor_en_columna(self):
        ''' Deberia de devolver false ya que el valor 2 esta repetido en la segunda columna'''
        tablero_con_valor_repetido = [[0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        valor_a_agregar = 2  # no puede estar el 4 en esa misma fila
        columna_a_verificar=1
        dimension=len(tablero_con_valor_repetido[0])
        no_hay_valor_repetido_en_columna=False #valor_a_agregar,columna_a_verificar,dimension,tablero
        self.assertEqual(Verificador_reglas().verificar_si_es_posible_colocar_en_la_columna(valor_a_agregar, columna_a_verificar,dimension,tablero_con_valor_repetido),no_hay_valor_repetido_en_columna)

    def test_comprobar_que_el_tablero_tenga_la_dimension_correcta(self):
        ''' Deberia de devolver true ya que el tablero tiene dimension 9 como se espera, se usa funcion len'''
        tablero_de_dimension_9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        dimension=len(tablero_de_dimension_9[0])
        tablero_tiene_dimension_correcta=True #valor_a_agregar,columna_a_verificar,dimension,tablero
        self.assertEqual(Verificador_reglas().verificar_tamaño_del_tablero(tablero_de_dimension_9,dimension),tablero_tiene_dimension_correcta)

    def test_comprobar_que_tablero_con_dimension_erronea(self):
        ''' Deberia de devolver false ya que el tablero tiene una fila con mas de 9 valores'''
        tablero_incompleto = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        dimension_ingresada_por_usuario=9
        tablero_tiene_dimension_correcta=False #valor_a_agregar,columna_a_verificar,dimension,tablero
        self.assertEqual(Verificador_reglas().verificar_tamaño_del_tablero(tablero_incompleto,dimension_ingresada_por_usuario),tablero_tiene_dimension_correcta)

if __name__ == '__main__':
    unittest.main()

