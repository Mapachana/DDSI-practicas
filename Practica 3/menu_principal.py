def menu_principal(cursor):
	# Mostrar el menú principal
	print("Bienvenido al sistema de información para hoteles MODEST")
	print("\nMENÚ PRINCIPAL")
	print("\t1. tal")
	print("\t2. cual")
	print("\t9. salir")
	
	# solicitar una opción al usuario
	opciones_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	opcion = int(input("Elija una opción: "))
	while not opcion in opciones_validas:
		opcion = int(input("Incorrecto. Elija una opción válida: "))
	
	# procesar la opción escogida por el usuario
	if (opcion == 1):
		print("entra en opcion 1")
		
	elif (opcion == 2):
		print("entra en opcion 2")
		
	elif (opcion == 9):
		print("\nGracias por su visita")
