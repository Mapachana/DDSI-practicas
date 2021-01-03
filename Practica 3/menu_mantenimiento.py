def aviso_reparacion(cursor):
	print("implementar")
	
def reparacion_resuelta(cursor):
	print("implementar")

def limpieza(cursor):	
	print("implementar")

def provisiones(cursor):
	print("implementar")


def menu_mantenimiento(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE MANTENIMIENTO")
		print("\t1: Registrar aviso de reparacion")
		print("\t2: Marcar reparación como resuelta")
		print("\t3: Planificar limpieza de una habitación")
		print("\t4: Registrar provisiones")
		print("\tq: salir")
		
		opciones_validas = ['1', '2', '3', '4', 'q']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
			
		if opcion == '1':
			aviso_reparacion(cursor)
			
		elif opcion == '2':
			reparacion_resuelta(cursor)
			
		elif opcion == '3':
			limpieza(cursor)
			
		elif opcion == '4':
			provisiones(cursor)
			
		elif opcion == 'q':
			salir = True
			
