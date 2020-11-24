import config
from inicializar_tablas import *
from menu_principal_2_1 import *
from menu_principal_2_2 import *
from menu_principal_2_3 import *
from menu_principal_2_4 import *
from datetime import datetime

def menu_principal_2(cursor):

	cursor.execute("SAVEPOINT INICIO_PEDIDO")

	print("Por favor introduzca el codigo de cliente")
	codigo = str(int(input())) #Por seguridad
	config.num_pedidos += 1
	cursor.execute("INSERT INTO Pedido VALUES (" + str(config.num_pedidos) + ", " + codigo + ", TO_DATE(\'" + datetime.today().strftime('%Y-%m-%d') + "\', \'yyyy/mm/dd\'))")

	cursor.execute("SAVEPOINT INICIO_DETALLES")

	opciones_validas = range(1, 5) # 1, 2, 3, 4
	salir = False
	while not salir:
		print("MENÚ ALTA DE PEDIDO:\n\tOpciones:\n\t\t1: aniadir detalle de producto\n\t\t2: eliminar todos los detalles de producto\n\t\t3: cancelar pedido\n\t\t4: finalizar pedido\n")
		opcion = int(input())

		if not opcion in opciones_validas:
			print("Por favor introduzca una opción válida")

		if opcion == 1:
			menu_principal_2_1(cursor)

		elif opcion == 2:
			menu_principal_2_2(cursor)

		elif opcion == 3:
			menu_principal_2_3(cursor)
			salir = True

		elif opcion == 4:
			menu_principal_2_4(cursor)
			salir = True
