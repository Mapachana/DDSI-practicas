def alta_empleado(cursor):
	print("implementar")

def modificar_empleado(cursor):
	print("implementar")
	
def consultar_empleado(cursor):
	print("implementar")
	
def baja_empleado(cursor):
	print("implementar")


def menu_empleados(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE EMPLEADOS")
		print("\t1: Dar de alta un empleado")
		print("\t2: Modificar la ficha de un empleado")
		print("\t3: Consultar la ficha de un empleado")
		print("\t4: Dar de baja un empleado")
		print("\tq: salir")
		
		opciones_validas = ['1', '2', '3', '4', 'q']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
			
		if opcion == '1':
			alta_empleado(cursor)
			
		elif opcion == '2':
			modificar_empleado(cursor)
			
		elif opcion == '3':
			consultar_empleado(cursor)
			
		elif opcion == '4':
			baja_empleado(cursor)
			
		elif opcion == 'q':
			salir = True
			
			
