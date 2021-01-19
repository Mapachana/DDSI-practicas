from siguiente_id_tabla import *

def grupo_excursion(cursor):
	# Creación del grupo con un guía asociado:
	id_grupo = siguiente_id_tabla(cursor, "GrupoDirigidoPor", "IdentificadorGrupo") # lo calcula automatico
	dni_guia = input("Introduzca DNI del guía: ")
	fecha = input("Introduzca fecha para la reunión del grupo (AAAA-MM-DD-HH24:MI): ")
	
	sentencia = "CALL grupo_excursion('" + id_grupo + "', '" + dni_guia + "', TO_DATE('" + fecha + "', 'YYYY-MM-DD-HH24:MI'))"
	cursor.execute(sentencia)
	print("Grupo creado")
	
	# Añadir participantes:
	num_participantes = int(input("Introduzca número de participantes en el grupo de excursión: "))
	for i in range(1, num_participantes+1):
		dni = input("Introduzca DNI del cliente número " + str(i) + ": ")
		sentencia = "CALL participante_grupo_excursion('" + id_grupo + "', '" + dni + "')"
		cursor.execute(sentencia)
		print("Cliente añadido a grupo")
	
	# Añadir una actividad al grupo de excursión:
	id_actividad = siguiente_id_tabla(cursor, "Actividad", "IdentificadorActividad")
	descripcion = input("Introduzca descripción de la actividad: ")
	sentencia = "CALL actividad_grupo_excursion('" + id_grupo + "', '" + id_actividad + "', '" + descripcion + "')"
	cursor.execute(sentencia)
	
	cursor.commit()
	
	
def organizar_evento(cursor):
	id_evento = siguiente_id_tabla(cursor, "EventoTieneLugarEn", "IdentificadorEvento")
	id_sala = input("Introduzca identificador de la sala en la que se celebrará el evento: ")
	descripcion = input("Introduzca una descripción: ")
	precio = float(input("Introduzca un precio: "))
	fecha = input("Introduzca fecha: (AAAA-MM-DD-HH24:MI): ")
	
	sentencia = "CALL organizar_evento('" + id_evento + "', '" + id_sala + "', '" + descripcion + "', " + str(precio) + ", TO_DATE('" + fecha + "', 'YYYY-MM-DD-HH24:MI'))"
	cursor.execute(sentencia)
	cursor.commit()
	

def publicitar_evento(cursor):
	id_evento = input("Introduzca identificador del evento que desea publicitar: ")
	consulta = cursor.execute("SELECT IdentificadorSala, Descripcion, Precio, FechaHora FROM EventoTieneLugarEn WHERE IdentificadorEvento='" + id_evento + "'").fetchall()
	
	if len(consulta) > 0 :
		datos = consulta[0]
		sala = datos[0]
		descripcion = datos[1]
		precio = datos[2]
		fechahora = datos[3]
		
		mensaje = "Le invitamos a asistir al nuevo evento en el estupendo hotel Modesto\n\t\t\tDescripción: " + descripcion + "\n\t\t\tSala: " + sala + "\n\t\t\tPrecio: " + str(precio) + "\n\t\t\tFecha y hora: " + str(fechahora)
		print("\n\tSe ha creado el siguiente mensaje:")
		print("\n\t\t" + mensaje + "\n")

		# Simulación de envío de emails
		emails = [x[0] for x in cursor.execute('SELECT CorreoElectronico FROM Cliente').fetchall()]
		for email in emails:
			print("Simulando enviar el mensaje a " + email + "...")
			
	else :
		print("No existe el evento con el identificador indicado")


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
