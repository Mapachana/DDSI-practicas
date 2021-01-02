# Realizado por Ana Buendía Ruiz-Azuaga, José Luis Ruiz Benito, Antonio Merino Gallardo y Paula Villanueva Núñez. Grupo 5.
import pyodbc
from datetime import datetime

import config
from menu_principal import * # menu principal

# PROGRAMA PRINCIPAL
def main():
	# conexión con la base de datos:
	cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')
	cursor = cnxn.cursor()

	# Inicialización variable global
	hay_pedidos_previos = (len(cursor.execute('SELECT * from Pedido').fetchall()) != 0)
	if hay_pedidos_previos:
		config.num_pedidos = int(cursor.execute('SELECT MAX(Cpedido) from Pedido').fetchall()[0][0])
	else:
		config.num_pedidos = 0


	menu_principal(cursor) # menú principal

	# Finalización del programa:
	cursor.close()
	cnxn.close()
	exit(0)

# iniciar programa principal:
main()
