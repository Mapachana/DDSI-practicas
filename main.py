import pyodbc
from datetime import datetime

from inicializar_tablas import * # inicialización de las tablas
from menu_principal import * # menu principal

# PROGRAMA PRINCIPAL
def main():
	# conexión con la base de datos:
	cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')
	cursor = cnxn.cursor()

	inicializar_tablas(cursor) # incialización de las tablas

	menu_principal(cursor) # menú principal

	# Finalización del programa:
	cursor.close()
	cnxn.close()
	exit(0)

# iniciar programa principal:
main()
