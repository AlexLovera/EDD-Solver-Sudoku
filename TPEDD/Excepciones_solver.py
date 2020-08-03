from math import sqrt as raiz_cuadrada;
from colorama import init, Style

init()
formato_error = '\033[4;31m'


class Solver_sudoku_exception(Exception):
    pass


class Tipo_de_archivo_incorrecto_exception(Solver_sudoku_exception):
    """tipo de archivo incorrecto"""

    def __init__(self, archivo_entrada):
        self.archivo_entrada = archivo_entrada

    def __str__(self):
        return formato_error + Style.BRIGHT+ f"El tipo de archivo indicado como:{self.archivo_entrada}, es incorrecto.Debe " \
            f"ser .csv"

    pass


# class Tablero_irregular_exception(Solver_sudoku_exception):#rompe el for?
#     def __str__(self):
#         return "\033[4;31m"+"El tablero debe tener la misma cantidad de filas y columnas, del mismo tamaño"
class Dimension_incorrecta_exception(Solver_sudoku_exception):
    """valor de dimension incorrecto"""

    # pass
    def __init__(self, dimension):
        # super()
        if int(dimension) < 0:
            self.mensaje = formato_error + Style.BRIGHT+ 'El valor para indicar la dimension debe ser mayor que cero'
        elif not raiz_cuadrada(dimension) / int(raiz_cuadrada(dimension)) == 1:
            self.mensaje = formato_error + Style.BRIGHT+'La raiz cuadrada del valor debe ser un entero'
        elif type(dimension) is int:  # "\033[4;31m" + Style.BRIGHT+
            self.mensaje = formato_error + Style.BRIGHT+ 'El valor ingresado para indicar la dimension debe ser un entero'

    def __str__(self):
        return self.mensaje


class Opcion_incorrecta_exception(Solver_sudoku_exception):
    def __str__(self):
        return formato_error + Style.BRIGHT+ "Opcion no valida.Debe ingresar alguna de las siguientes opciones:'RSN','REP' o 'MDT'"


class Cantidad_tableros_incorrecta_exception(Exception):
    def __str__(self):
        return formato_error + Style.BRIGHT+ "Cantidad de tableros a generar incorrecta.Se pueden generar de 1 a 10 tableros."
