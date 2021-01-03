def reserva(cursor):
	print("implementar")
	
def checkin(cursor):
	print("implementar")

def checkout(cursor):
	print("implementar")

def cancelar_reserva(cursor):	
	print("implementar")
	
def disponibilidad(cursor):
	print("implementar")


def menu_clientes_reservas(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE CLIENTES, RESERVAS Y OCUPACIONES")
		print("\t1: Registrar una reserva")
		print("\t2: Registrar check-in")
		print("\t3: Registrar check-out")
		print("\t4: Cancelar una reserva")
		print("\t5: Consultar la disponibilidad de un tipo de habitacion")
		print("\tq: salir")
		
		opciones_validas = ['1', '2', '3', '4', '5', 'q']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
			
		if opcion == '1':
			reserva(cursor)
			
		elif opcion == '2':
			checkin(cursor)
			
		elif opcion == '3':
			checkout(cursor)
			
		elif opcion == '4':
			cancelar_reserva(cursor)
			
		elif opcion == '5':
			disponibilidad(cursor)
			
		elif opcion == 'q':
			salir = True
