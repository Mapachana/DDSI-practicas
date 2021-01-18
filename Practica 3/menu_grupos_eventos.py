def grupo_excursion(cursor):
	# Creación del grupo con un guía asociado
	id_grupo = input("Introduzca un identificador para el grupo: ")
	dni_guia = input("Introduzca DNI del guía: ")
	fecha = input("Introduzca fecha para la reunión del grupo (AAAA-MM-DD): ")
	
	sentencia = "CALL grupo_excursion('" + id_grupo + "', '" + dni_guia + "', TO_DATE('" + fecha + "', 'YYYY-MM-DD'))"
	#print(sentencia)
	cursor.execute(sentencia)
	print("Grupo creado")
	
	# Añadir participantes
	num_participantes = int(input("Introduzca número de participantes en el grupo de excursión: "))
	for i in range(1, num_participantes+1):
		dni = input("Introduzca DNI del cliente número " + str(i) + ": ")
		sentencia = "CALL participante_grupo_excursion('" + id_grupo + "', '" + dni + "')"
		#print(sentencia)
		cursor.execute(sentencia)
		print("Cliente añadido a grupo")
	
	cursor.commit()
	
	
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
