import csv,random,time
from math import sqrt as raiz_cuadrada
from colorama import Fore, init,Back,Style
# from .validador import Validador_posiciones
# from curses import *
init()
class Solver_sudoku_exception(Exception):
    pass
class Tipo_de_archivo_incorrecto_exception(Solver_sudoku_exception):
    '''tipo de archivo incorrecto'''
    pass
class Dimension_incorrecta_exception(Solver_sudoku_exception):
    '''valor de dimension incorrecto'''
    pass
    # def __init__(self,dimension):
    #     super()
    #     if dimension<0:
    #         self.mensaje = "El valor para indicar la dimension debe ser mayor que cero"
    #     elif not raiz_cuadrada(dimension) is int:
    #         self.mensaje = "La raiz cuadrada del valor debe ser un entero"
    #     elif type(dimension) is int:
    #         self.mensaje = "El valor ingresado para indicar la dimension debe ser un entero"
    # def __str__(self):
    #     return self.mensaje
class Verificador_reglas():
    def verificar_posicion_libre(self,tablero, num, posicion,dimension):
        longitud_submatriz=int(raiz_cuadrada(dimension))

        # verifica fila
        for i in range(len(tablero)):
            if tablero[posicion[0]][i] == num:
                return False

        # verifica columna
        for i in range(len(tablero)):
            if tablero[i][posicion[1]] == num:
                return False

        # verifica submatriz, EL 3 DEBE SER RAIZ DE DIMENSION
        inicio_columna = (posicion[1] // longitud_submatriz)*longitud_submatriz
        inicio_fila = (posicion[0] // longitud_submatriz)*longitud_submatriz

        for i in range(inicio_fila,inicio_fila + longitud_submatriz):
            for j in range(inicio_columna, inicio_columna + longitud_submatriz):
                if tablero[i][j] == num:
                    return False
        return True

    def verificar_tamaño_del_tablero(self,tablero,dimension):
        tamaño_correcto=True
        for i in tablero:
            longitud_columna_temporal = len(i)
            if not longitud_columna_temporal == dimension:
                tamaño_correcto=False
                break
                #raise errorEnDimensionException?
        return tamaño_correcto

validador=Verificador_reglas()

class Generador_Sudokus:
    validador = Verificador_reglas()
    #agregar dificultad?
    def generar_sudokus_en_csv(self,dimension,cantidad):
        #ejemplo: 3*3, es dimension 9--> que seria 9*9, 81 casilleros
        if not 0<cantidad<10 and type(cantidad)==int:
            # raise CantidadException
            # raise TipoIncorrecto
            pass
        cantidad_casilleros=dimension*dimension
        cantidad_de_valores_random=cantidad_casilleros//3
        for num_tableros in range(cantidad):
            tablero=self._generar_tablero_en_matriz(dimension)
            #rellenar con valores random
            for i in range(cantidad_de_valores_random):
                fila_random, columna_random = random.randint(0, dimension - 1), random.randint(0, dimension - 1)
                valor_random = random.randint(0, dimension - 1)
                if validador.verificar_posicion_libre(tablero, valor_random, (fila_random, columna_random),dimension):
                    tablero[fila_random][columna_random]=valor_random
                else:
                    cantidad_de_valores_random+=1#si no se puede agregar en ese lugar, se suma un intento mas
            csv_archivo=csv.writer(open("sudokus_generados.csv","a",newline=''))
            for i in range(dimension):
                # csv_archivo.writerow("\n")
                # for j in range(dimension):
                # print(tablero[i])
                lista=tablero[i]
                csv_archivo.writerow(lista)

    def _generar_tablero_en_matriz(self,dimension):
        if not type(raiz_cuadrada(int(dimension))) is int:
            #raise DimensionException
            pass
        tablero=list()
        for i in range(dimension):
            fila_temporal=list()
            for j in range(dimension):
                fila_temporal.append(0)
            tablero.append(fila_temporal)
        return tablero

class Solucionador_sudokus():
    def resolver_sudokus(self):
        try:
            opcion_menu = input("Puede: Resolver sudokus nuevos o Recuperar una ejecucion parcial.\nElija con 'RSN' o 'REP' respectivamente\n")
            if str(opcion_menu).lower().__eq__("rsn"):
                path_archivo = input("Introduzca el path del archivo con sudokus en formato .csv: ")
                dimension = int(input("Introduzca la dimension del tablero: "))
                self._carga_archivo_y_resuelve(path_archivo, dimension)
            elif str(opcion_menu).lower().__eq__("rep"):
                pass
            else:
                pass#raise exception
        except ValueError:
            print("\033[4;31m" + Style.BRIGHT+"La dimension debe ser un numero, entero y raiz cuadrada como entero")
            time.sleep(5)

    def _carga_archivo_y_resuelve(self,archivo_entrada,dimension):
        '''recibe un archivo csv con los numeros separados por coma y otro parametro para
            comprobar que la dimension de todos los tableros sea la correcta, debe ser un entero'''
        try:
            if not (0 < dimension and type(dimension) is  int and raiz_cuadrada(dimension) / int(raiz_cuadrada(dimension))==1):
                raise Dimension_incorrecta_exception("\033[4;31m" + Style.BRIGHT+"El valor ingresado debe ser entero, mayor que 0 y su raiz cuadrada tambien")
            if not archivo_entrada.__contains__(".csv"):
                raise Tipo_de_archivo_incorrecto_exception
            archivo = csv.reader(open(archivo_entrada, "r"), delimiter=",")
            fila_temporal, tablero = list(), list()
        # archivo = csv.reader(open(archivo_entrada, "r"), delimiter=",")
            num_linea = 0
            for linea in archivo:
                num_linea += 1
                for numero in linea:
                    fila_temporal.append(int(numero))
                tablero.append(fila_temporal)
                #clear?
                fila_temporal = list()
                if num_linea % dimension == 0:
                    print(Fore.YELLOW + str(archivo.line_num))
                    #termina de cargar el tablero, y lo resuelve
                    if Verificador_reglas().verificar_tamaño_del_tablero(tablero, dimension):
                        self._resolver(tablero,dimension)
                    else:
                        print("\033[4;31m"+Style.BRIGHT+"ERROR EN DIMENSION")
                        # pass#raise errorEnDimension?
                    tablero.clear()
            print(Fore.YELLOW+Style.NORMAL+ str(archivo.line_num))
        except FileNotFoundError:
            print("\033[4;31m" + Style.BRIGHT + f"No se encontró el archivo{archivo_entrada}")
            time.sleep(5)
        except Tipo_de_archivo_incorrecto_exception:
            print("\033[4;31m" + Style.BRIGHT + f"El tipo de archivo indicado como:{archivo_entrada}, es incorrecto")
            time.sleep(5)
        except Dimension_incorrecta_exception as e:
            print(e)
            time.sleep(5)
            # if dimension < 0:
            #     print("El valor para indicar la dimension debe ser mayor que cero")
            # elif not raiz_cuadrada(dimension) is int:
            #     print("La raiz cuadrada del valor debe ser un entero")
            # elif type(dimension) is not int:
            #     print("El valor ingresado para indicar la dimension debe ser un entero")
        except KeyboardInterrupt:
            print("Ctrl+C presionado")
            time.sleep(5)
    def _resolver(self,tablero,dimension):
        espacio_libre = self._buscar_espacio_libre(tablero,dimension)
        if not espacio_libre:
            temporal = csv.writer(open("salida_tableros.csv", "a",newline=""))
            for j in tablero:
                temporal.writerow(j)
            self._mostrar_tablero_consola(tablero,dimension)
            return True
        else:
            fila, columna = espacio_libre

        for i in range(1,dimension+1):
            if validador.verificar_posicion_libre(tablero, i, (fila, columna),dimension):
                tablero[fila][columna] = i

                if self._resolver(tablero,dimension):
                    return True

                tablero[fila][columna] = 0

        return False

    def _mostrar_tablero_consola(self,tablero,dimension):
        for i in range(dimension):
            if i % 3 == 0 and i != 0:
                print(Fore.RED+"- - - - - - - - - - - - ")

            for j in range(dimension):
                if j % 3 == 0 and j != 0:
                    print(Fore.RED+" | ", end="")

                if j == 8:
                    print(Fore.WHITE + str(tablero[i][j]))
                else:
                    print(Fore.WHITE + str(tablero[i][j]) + " ", end="")
        print(Fore.GREEN+"___________________________________\n")

    def _buscar_espacio_libre(self,tablero,dimension):
        for i in range(dimension):
            for j in range(dimension):
                if tablero[i][j] == 0:
                    return (i, j)
        return None
def guardar_progreso():

    pass

# generador=Generador_Sudokus()
# generador.generar_sudokus_en_csv(9,1)#FUNCIONA MAL, NO TIRA SIEMPRE SUDOKUS POSIBLES
# resolver=Solucionador_sudokus()
# resolver._carga_archivo_y_resuelve("tableros.csv",10)

def main():
    resolvedor=Solucionador_sudokus()
    resolvedor.resolver_sudokus()

if __name__=="__main__":
    main()