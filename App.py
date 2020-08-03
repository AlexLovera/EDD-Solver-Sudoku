from Excepciones_solver import *;
from colorama import init, Style
from time import sleep as esperar

init()
from Resolvedor import Solucionador_sudokus


def resolver_sudokus():
    try:
        opcion_menu = input(
            "Puede: Resolver sudokus nuevos, Recuperar una ejecucion parcial.\nElija con 'RSN' o 'REP' respectivamente\nO "
            "medir tiempos de resolucion de tableros vacios, marcando 'MDT'\n")
        if str(opcion_menu).lower().__eq__("rsn"):
            path_archivo = input("Introduzca el path del archivo con sudokus en formato .csv: ")
            dimension = int(input("Introduzca la dimension del tablero: "))
            Solucionador_sudokus()._carga_archivo_y_resuelve(path_archivo, dimension)
        elif str(opcion_menu).lower().__eq__("rep"):
            # path_archivo_recuperacion, cambio para generalizar
            path_archivo = input("Introduzca el path de recuperacion: ")
            Solucionador_sudokus()._recuperar_progreso_con_json(path_archivo)
        elif str(opcion_menu).lower().__eq__("mdt"):
            Solucionador_sudokus()._medir_tiempos_de_diferentes_dimensiones()
        else:
            raise Opcion_incorrecta_exception
    except ValueError:
        print("\033[4;31m" + Style.BRIGHT + "La dimension debe ser un numero, entero y raiz cuadrada como entero")
        esperar(5)
    except Opcion_incorrecta_exception as e:
        print(e)
    except FileNotFoundError:
        print('\033[4;31m' + Style.BRIGHT + f"No se encontró el archivo: {path_archivo}")
        esperar(5)  # time.sleep(5)


def main():
    # from Generador_sudokus import Generador_Sudokus
    # Generador_Sudokus().generar_sudokus_en_csv(9,1)
    # Solucionador_sudokus()._carga_archivo_y_resuelve("archivos/sudokus_generados.csv",9)

    resolver_sudokus()

    # para recuperar, escribirlo en archivos/... preferentemente


if __name__ == "__main__":
    main()
