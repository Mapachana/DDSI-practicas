from consultar_estado import *
from crear_tablas import *
from insertar_tuplas import *

def menu_principal(cursor):
	print("Bienvenido al sistema de información para hoteles MODEST")

	salir = False
	while not salir:
		# Mostrar el menú principal
		print("\nMENÚ PRINCIPAL")
		print("\tc: consulta estado de la BD (para depuración)")
		print("\t0: Restaurar la BD: eliminar las tablas y crearlas de nuevo")
		print("\t1: Restaurar la BD e insertar tuplas de ejemplo")
		print("\t2: noseque")
		print("\tq: salir")
		
		# solicitar una opción al usuario
		opciones_validas = ['c', 'q', '0', '1', '2']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
		
		# procesar la opción escogida por el usuario
		if opcion == 'c':
			consultar_estado(cursor)
			
		if opcion == '0':
			crear_tablas(cursor) # elimina las tablas y vuelve a crearlas
			
		elif opcion == '1':
			insertar_tuplas(cursor) # elimina las tablas, vuelve a crearlas e inserta tuplas de ejemplo
			
		elif opcion == '2':
			print("entra en opcion 2")
			
		elif opcion == 'q':
			print("\nGracias por su visita")
			salir = True # devolver el flujo a la rutina invocante
