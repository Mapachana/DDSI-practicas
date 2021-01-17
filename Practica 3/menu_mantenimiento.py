def aviso_reparacion(cursor):
	num_hab = input('Introduzca el numero de habitacion donde se necesita una reparacion: ')
	while len(num_hab) != 3:
		num_hab = input('El numero de habitacion debe tener 3 caracteres.\nIntroduzca el numero de habitacion donde se necesita una reparacion: ')

	descripcion = input('Introduzca la descripcion del problema')
	while len(descripcion) <= 0 or len(descripcion) > 300:
		descripcion = input('La descripcion debe tener entre 1 y 300 caracteres.\nIntroduce la descripcion: ')

	diaNac = input('Introduce el dia de la incidencia: ')

	while int(diaNac) <= 0 or int(diaNac) > 31:
		diaNac = input('El dia de la incidencia debe estar comprendido entre 1 y 31.\nIntroduce el dia de nacimiento del empleado: ')

	mesNac = input('Introduce el mes de la incidencia: ')

	while int(mesNac) <= 0 or int(mesNac) > 12:
		mesNac = input('El mes de debe estar comprendido entre 1 y 12.\nIntroduce el mes de la incidencia: ')

	anioNac = input('Introduce el anio de la incidencia: ')

	while int(anioNac) <= 0:
		anioNac = input('El anio de debe ser un numero positivo.\nIntroduce  el anio de la incidencia: ')

	fechaNac = '-'.join([anioNac, mesNac, diaNac])

	identificador = "RE0000003" #FIXME arreglar generacion de identificador

	datos = ("'"+identificador+"'", "'"+num_hab+"'", "'"+descripcion+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD')")

	sentencia = 'CALL registrar_aviso_reparacion (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

	print("Se ha aniadido el aviso de reparacion con identificador: " + datos[0])
	
def reparacion_resuelta(cursor):
	print("impdementar")

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
			
