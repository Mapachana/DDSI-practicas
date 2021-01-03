from crear_tablas import *
from insertar_tuplas import *

def menu_principal(cursor):
	print("Bienvenido al sistema de información para hoteles MODEST")

	salir = False
	while not salir:
		# Mostrar el menú principal
		print("\nMENÚ PRINCIPAL")
		print("\t0. Restaurar la BD: eliminar las tablas, crearlas de nuevo")
		print("\t1. Insertar tuplas de ejemplo")
		print("\t2. noseque")
		print("\t9. salir")
		
		# solicitar una opción al usuario
		opciones_validas = range(0, 10)
		opcion = int(input("Elija una opción: "))
		while not opcion in opciones_validas:
			opcion = int(input("Incorrecto. Elija una opción válida: "))
		
		# procesar la opción escogida por el usuario
		if (opcion == 0):
			crear_tablas(cursor)
			
		elif (opcion == 1):
			insertar_tuplas(cursor)	
			
		elif (opcion == 2):
			print("entra en opcion 2")
			
		elif (opcion == 9):
			print("\nGracias por su visita")
			salir = True # devolver el flujo a la rutina invocante
