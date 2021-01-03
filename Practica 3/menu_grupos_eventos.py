def grupo_excursion(cursor):
	print("implementar")
	
def organizar_evento(cursor):
	print("implementar")
	
def publicitar_evento(cursor):
	print("Simulando enviar email...")


def menu_grupos_eventos(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE GRUPOS Y EVENTOS")
		print("\t1: Crear un grupo de excursion")
		print("\t2: Organizar un evento en el hotel")
		print("\t3: Publicitar un evento")
		print("\tq: salir")
		
		opciones_validas = ['1', '2', '3', 'q']
		opcion = input("Elija una opción: ")
		while not opcion in opciones_validas:
			opcion = input("Incorrecto. Elija una opción válida: ")
			
		if opcion == '1':
			grupo_excursion(cursor)
			
		elif opcion == '2':
			organizar_evento(cursor)
			
		elif opcion == '3':
			publicitar_evento(cursor)
			
		elif opcion == 'q':
			salir = True
