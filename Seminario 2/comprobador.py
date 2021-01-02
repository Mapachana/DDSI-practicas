import pyodbc
from datetime import datetime

from inicializar_tablas import * # inicialización de las tablas
from menu_principal import * # menu principal

# PROGRAMA PRINCIPAL
def main():
	# conexión con la base de datos:
	cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')
	cursor = cnxn.cursor()


	q = cursor.execute("SELECT * FROM Stock")
	rows = q.fetchall()
	print("Tabla Stock")
	print("Cproducto \tCantidad")
	# Recorrer cada una de las filas e imprimirlas en pantalla.
	if rows is not None:
		for row in rows:
			print(str(row[0]) +"\t\t" + str(row[1]))
	else:
		print("No hay datos en la tabla.")

	
	q = cursor.execute("SELECT * FROM Pedido")
	rows = q.fetchall()
	print("\nTabla Pedido")
	print("Cpedido \tCcliente \tFecha")
	# Recorrer cada una de las filas e imprimirlas en pantalla.
	if rows is not None:
		for row in rows:
			print(str(row[0]) +"\t\t" + str(row[1]) +"\t\t" + str(row[2]))
	else:
		print("No hay datos en la tabla.")
		
		
	q = cursor.execute("SELECT * FROM DetallePedido")
	rows = q.fetchall()
	print("\nTabla DetallePedido")
	print("Cpedido \tCProducto \tCantidad")
	# Recorrer cada una de las filas e imprimirlas en pantalla.
	if rows is not None:
		for row in rows:
			print(str(row[0]) +"\t\t" + str(row[1]) +"\t\t" + str(row[2]))
	else:
		print("No hay datos en la tabla.")



	# Finalización del programa:
	cursor.close()
	cnxn.close()
	exit(0)

# iniciar programa principal:
main()
