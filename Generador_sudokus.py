import csv, random;
from time import sleep as esperar
from math import sqrt as raiz_cuadrada
from Verificador_de_reglas import Verificador_reglas
from Excepciones_solver import Dimension_incorrecta_exception, Cantidad_tableros_incorrecta_exception


class Generador_Sudokus:
    def generar_sudokus_en_csv(self, dimension, cantidad):
        # ejemplo: 3*3, es dimension 9--> que seria 9*9, 81 casilleros
        try:
            if not 0 < cantidad < 10 and type(cantidad) == int:
                raise Cantidad_tableros_incorrecta_exception
            if not (0 < dimension and type(dimension) is int and raiz_cuadrada(dimension) / int(
                    raiz_cuadrada(dimension)) == 1):
                raise Dimension_incorrecta_exception(dimension)
            cantidad_casilleros = dimension * dimension
            cantidad_de_valores_random = cantidad_casilleros // 3
            for num_tableros in range(cantidad):
                tablero = self._generar_tablero_en_matriz(dimension)
                # rellenar con valores random
                for i in range(cantidad_de_valores_random):
                    fila_random, columna_random = random.randint(0, dimension - 1), random.randint(0, dimension - 1)
                    valor_random = random.randint(0, dimension)
                    if Verificador_reglas().verificar_posicion_libre(tablero, valor_random,
                                                                     (fila_random, columna_random), dimension):
                        tablero[fila_random][columna_random] = valor_random
                    # else:
                    # cantidad_de_valores_random+=1#si no se puede agregar en ese lugar, se suma un intento mas
                csv_archivo = csv.writer(open("archivos/sudokus_generados.csv", "a", newline=''))  # carpeta archivos
                for i in range(dimension):
                    lista = tablero[i]
                    csv_archivo.writerow(lista)
        except Dimension_incorrecta_exception as e:
            print(e)
            esperar(5)
        except Cantidad_tableros_incorrecta_exception as e:
            print(e)
            esperar(5)

    def _generar_tablero_en_matriz(self, dimension):
        if not type(raiz_cuadrada(int(dimension))) is int:
            # raise DimensionException
            pass
        tablero = list()
        for i in range(dimension):
            fila_temporal = list()
            for j in range(dimension):
                fila_temporal.append(0)
            tablero.append(fila_temporal)
        return tablero
