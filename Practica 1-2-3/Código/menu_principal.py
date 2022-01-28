from consultar_estado import *
from crear_tablas import *
from insertar_tuplas import *
from menu_empleados import menu_empleados
from menu_clientes_reservas import menu_clientes_reservas
from menu_mantenimiento import menu_mantenimiento
from menu_grupos_eventos import menu_grupos_eventos

def menu_principal(cursor):
	print("Bienvenido al sistema de información para hoteles MODEST")

	salir = False
	while not salir:
		# Mostrar el menú principal
		print("\nMENÚ PRINCIPAL")
		print("\tc: consulta estado de la BD (para depuración)")
		print("\tr: Restaurar la BD: eliminar las tablas y crearlas de nuevo")
		print("\ti: Restaurar la BD e insertar tuplas de ejemplo")
		print("\t1: Menú para la gestión de empleados")
		print("\t2: Menú para la gestión de clientes, reservas y ocupaciones")
		print("\t3: Menú para la gestión del mantenimiento")
		print("\t4: Menú para la gestión de grupos y eventos")
		print("\tq: salir")
		
		# solicitar una opción al usuario
		opciones_validas = ['c', 'r', 'i', '1', '2', '3', '4', 'q']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
		
		# procesar la opción escogida por el usuario
		if opcion == 'c':
			consultar_estado(cursor)
			
		if opcion == 'r':
			crear_tablas(cursor) # elimina las tablas, vuelve a crearlas, crea (o actualiza) los triggers
			
		elif opcion == 'i':
			insertar_tuplas(cursor) # llama a crear_tablas(cursor) e inserta tuplas de ejemplo
			
		elif opcion == '1':
			menu_empleados(cursor)
			
		elif opcion == '2':
			menu_clientes_reservas(cursor)
			
		elif opcion == '3':
			menu_mantenimiento(cursor)
			
		elif opcion == '4':
			menu_grupos_eventos(cursor)
			
		elif opcion == 'q':
			print("\nGracias por su visita")
			salir = True # devolver el flujo a la rutina invocante
