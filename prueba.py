import pyodbc
from datetime import datetime

from inicializar_tablas import * # inicialización de las tablas
from opcion1 import * # primera opcion del menu


cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')
cursor = cnxn.cursor()

inicializar_tablas(cursor)


def menu_principal():
	print("Pulse 1 para reinicializar las tablas,\n 2 para dar de alta un pedido,\n 3 para borrar un pedido,\n 4 para salir\n")
	opcion = input()
	if opcion == "1":
		opcion1()
	elif opcion == "2":
		menu_pedido()
	elif opcion == "3":
		print("otro menu")
	elif opcion == "4":
		cursor.close()
		cnxn.close()
		print("Gracias por usarnos")
		exit(0)

def menu_pedido():
	print("Por favor introduzca el codigo de cliente")
	codigo = input()
	pidiendo = true
	num_pedidos += 1
	cursor.execute("INSERT INTO Pedido VALUES ("+str(num_pedidos)+", "+codigo+", "+datetime.today().strftime('%Y-%m-%d')+")")
	
	while(pidiendo):
		print("Pulse 1 para añadir detalle de producto,\n 2 para eliminar todos los detalles de producto,\n 3 para cancelar pedido,\n 4 para confirmar y terminar pedido\n")
		opcion = input()
		if opcion == "1":
			print("jaja no lo has hecho")
		elif opcion == "2":
			print("llora")
		elif opcion == "3":
			print("otro menu")
			pidiendo = false
		elif opcion == "4":
			cursor.close()
			cnxn.close()
			print("Gracias por usarnos")
			pidiendo = false
			exit(0)
			
# inicio del menu principal
menu_principal()				

		
	



