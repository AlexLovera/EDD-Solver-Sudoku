import csv, random, time, json, sys  # ;import calendar
# import TPEDD.Excepciones_solver as Excepciones #para Pycharm
from Excepciones_solver import *
# from TPEDD import Verificador_de_reglas,Generador_sudokus
from time import sleep as esperar, time;from math import sqrt as raiz_cuadrada
from colorama import init, Style  # ,Fore
# from curses import *
from Generador_sudokus import Generador_Sudokus
from Verificador_de_reglas import Verificador_reglas

init()


class Solucionador_sudokus():
    def __init__(self):
        self.contador_fallos = 0
        self.formato_predeterminado = '\033[0;37m'

    def _suma_fallos_provocados(self):
        # global contador_fallos
        self.contador_fallos += 1
        return self.contador_fallos

    def _carga_archivo_y_resuelve(self, archivo_entrada, dimension, num_linea_recuperacion=0):
        '''recibe un archivo csv con los numeros separados por coma y otro parametro para
            comprobar que la dimension de todos los tableros sea la correcta, debe ser un entero'''
        try:
            formato_error = '\033[4;31m'
            if not (0 < dimension and type(dimension) is int and raiz_cuadrada(dimension) / int(
                    raiz_cuadrada(dimension)) == 1):
                raise Dimension_incorrecta_exception(dimension)
            if not archivo_entrada.__contains__(".csv"):
                raise Tipo_de_archivo_incorrecto_exception(archivo_entrada)
            archivo = csv.reader(open(archivo_entrada, "r"), delimiter=",")
            fila_temporal, tablero = list(), list()
            num_linea = 0
            for linea in archivo:
                if num_linea_recuperacion is not 0:  # va a saltear las lineas necesarias
                    num_linea_recuperacion -= 1
                    continue
                num_linea += 1
                for numero in linea:
                    fila_temporal.append(int(numero))
                tablero.append(fila_temporal) # agrega de a filas
                fila_temporal = list()
                if num_linea % dimension == 0: # cuando el tablero este completo, verifica y resuelve?. Hacer test
                    print('\033[1;33m' + f"Sudoku N°:{int(archivo.line_num / dimension)}")
                    print('\033[1;33m' + f"Linea de archivo N°:{archivo.line_num}")
                    # termina de cargar el tablero, y lo resuelve
                    if Verificador_reglas().verificar_tamaño_del_tablero(tablero, dimension) \
                            and Verificador_reglas().verificar_valores_predeterminados_correctos(tablero, dimension):
                        self._resolver(tablero, dimension, num_linea, archivo_entrada)
                    elif not Verificador_reglas().verificar_tamaño_del_tablero(tablero, dimension):
                        # raise Tablero_irregular_exception
                        print(
                            formato_error + Style.BRIGHT+ "El tablero debe tener la misma cantidad de filas y columnas, del mismo tamaño")
                    else:
                        print(formato_error + Style.BRIGHT+ f"El tablero solo puede contener valores entre 0 y {dimension}")
                    tablero.clear()
        except ValueError:
            print("\033[4;31m" + Style.BRIGHT + "El archivo solo debe contener numeros y el separador")
            esperar(5)
        except Tipo_de_archivo_incorrecto_exception as e:
            print(e)
            esperar(5)
        except Dimension_incorrecta_exception as e:
            print(e)
            esperar(5)

    def _resolver(self, tablero, dimension, num_linea=0,
                  archivo_entrada=None):  # no se  puede poner parametro por "defecto"
        # agrego num_linea para poder guardar el num_linea por el cual se quedo la lectura el archivo de entrada
        try:
            espacio_libre = self._buscar_espacio_libre(tablero, dimension)
            if not espacio_libre:
                if num_linea == -1:
                    if self._suma_fallos_provocados() <= 10:
                        # print("'fallo' provocado")#entra las 10 veces...
                        return False
                else:
                    temporal = csv.writer(open("archivos/salida_tableros.csv", "a", newline=""))
                    for j in tablero:
                        temporal.writerow(j)
                    self._mostrar_tablero_consola(tablero, dimension)
                return True
            else:
                fila, columna = espacio_libre

            for i in range(1, dimension + 1):
                if Verificador_reglas().verificar_posicion_libre(tablero, i, (fila, columna), dimension):
                    tablero[fila][columna] = i

                    if self._resolver(tablero, dimension, num_linea, archivo_entrada):
                        return True

                    tablero[fila][columna] = 0

            return False
        except KeyboardInterrupt:
            path_archivo_serializacion = input("Introduzca el path donde querra guardar la resolucion parcial: ")
            # a dic de datos se le tiene que pasar: tablero actual, num_linea, dimension, y archivo de entrada
            dic_datos = {"tablero": tablero,
                         "num_linea": num_linea,
                         "dimension": dimension,
                         "ruta_entrada": archivo_entrada}
            self._guardar_progreso_json(dic_datos, path_archivo_serializacion)
            sys.exit()

    def _pintar_separador_horizontal(self):
        print('\033[0;31m' + " ---------------------------" + self.formato_predeterminado)

    def _mostrar_tablero_consola(self, tablero, dimension):
        formato_separador_columna = '\033[0;31m'
        long_submatriz = int(raiz_cuadrada(dimension))
        self._pintar_separador_horizontal()
        for i in range(dimension):
            if i % long_submatriz == 0 and i != 0:  # 3/3 6/3 9*9
                self._pintar_separador_horizontal()

            for j in range(dimension):
                if j % long_submatriz == 0:
                    print(formato_separador_columna + " | " + self.formato_predeterminado, end="")

                if j == dimension - 1:
                    print(str(tablero[i][j]) + " ", end="")
                    print(formato_separador_columna + "|" + self.formato_predeterminado)
                else:
                    print(str(tablero[i][j]) + " ", end="")

        self._pintar_separador_horizontal()
        print('\033[0;32m' + "___________________________________\n" + self.formato_predeterminado)

    def _buscar_espacio_libre(self, tablero, dimension):
        for i in range(dimension):
            for j in range(dimension):
                if tablero[i][j] == 0:
                    return (i, j)
        return None

    def _guardar_progreso_json(self, dic_datos, ruta_guardado):
        with open("archivos/" + ruta_guardado, 'w') as archivo:
            json.dump(dic_datos, archivo)

    def _recuperar_progreso_con_json(self, ruta):
        with open(ruta, "rb") as archivo:
            dic_datos_recuperados = {}
            dic_datos_recuperados = json.load(archivo)
            estructura_recuperacion = list()
            for datos in dic_datos_recuperados:
                estructura_recuperacion.append(dic_datos_recuperados[datos])
            tablero = estructura_recuperacion[0]  # seria el tablero en el que quedo la resolucion parcial
            num_linea_recuperar = estructura_recuperacion[1]  # seria el num de linea donde se quedo la resolucion
            dimension = estructura_recuperacion[2]
            ruta_de_inicio = estructura_recuperacion[3]
            self._resolver(tablero, dimension, 0, ruta_de_inicio)  # no creo que tenga importancia el numero de linea
            self._carga_archivo_y_resuelve(ruta_de_inicio, dimension, num_linea_recuperar)

    def _medir_tiempos_de_diferentes_dimensiones(self):
        '''Mide el tiempo que tarda en resolver tableros de 3x3...5x5, en el ultimo caso se resuelve 1 solo tab'''
        print("N\t\tTiempo[seg]\n")
        for i in range(3, 6):
            dimension_tablero = i * i
            if i <= 4:
                # for j in range(11):
                tablero_vacio = Generador_Sudokus()._generar_tablero_en_matriz(dimension_tablero)
                inicio_contador = time()
                self._resolver(tablero_vacio, dimension_tablero, -1)  # verificar si funciona
                final_contador = time()
                tiempo_de_resolucion = final_contador - inicio_contador
                # tiempo_promedio_de_resolucion=tiempo_de_resolucion/10
                print(f"{dimension_tablero}\t\t{tiempo_de_resolucion}\n")
                self.contador_fallos = 0
            else:
                tablero_vacio = Generador_Sudokus()._generar_tablero_en_matriz(dimension_tablero)
                inicio_contador = time()
                self._resolver(tablero_vacio, dimension_tablero, -1)  # verificar si funciona
                final_contador = time()
                print(f"{dimension_tablero}\t{final_contador - inicio_contador}\n")
