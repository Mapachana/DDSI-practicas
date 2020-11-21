import inicializar_tablas
from datetime import datetime

def menu_principal_2(cursor):
	print("MENÚ ALTA DE PEDIDO")
	print("Por favor introduzca el codigo de cliente")
	codigo = input()
	pidiendo = True
	inicializar_tablas.num_pedidos += 1
	cursor.execute("INSERT INTO Pedido VALUES ("+str(inicializar_tablas.num_pedidos)+", "+codigo+", "+datetime.today().strftime('%Y-%m-%d')+")")
	
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
			# Salida de esta función:
			pidiendo = false




