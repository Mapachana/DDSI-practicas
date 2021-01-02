import pyodbc

from menu_principal import *
from crear_tablas import * # quitar despues

def main():
	# Incialización de la conexión
	cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')
	cursor = cnxn.cursor()
	
	# llamada a creacion de tablas (quitar despues)
	crear_tablas(cursor)
	
	# Llamada a menu_principal
	menu_principal(cursor)
	
	# Finalización del programa:
	cursor.close()
	cnxn.close()
	exit(0)

# Llamada al programa principal
main()
