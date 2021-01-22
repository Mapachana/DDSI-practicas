from siguiente_id_tabla import *

def aviso_reparacion(cursor):
	num_hab = input('Introduzca el número de habitación donde se necesita una reparación: ')
	while len(num_hab) != 3:
		num_hab = input('El numero de habitación debe tener 3 digitos.\nIntroduzca el numero de habitación donde se necesita una reparación: ')

	descripcion = input('Introduzca la descripción del problema: ')
	while len(descripcion) <= 0 or len(descripcion) > 300:
		descripcion = input('La descripción debe tener entre 1 y 300 caracteres.\nIntroduzca la descripción: ')

	diaNac = input('Introduzca el día de la incidencia: ')

	while int(diaNac) <= 0 or int(diaNac) > 31:
		diaNac = input('El día de la incidencia debe estar comprendido entre 1 y 31.\nIntroduzca el día de nacimiento del empleado: ')

	mesNac = input('Introduzca el mes de la incidencia: ')

	while int(mesNac) <= 0 or int(mesNac) > 12:
		mesNac = input('El mes de debe estar comprendido entre 1 y 12.\nIntroduzca el mes de la incidencia: ')

	anioNac = input('Introduzca el año de la incidencia: ')

	while int(anioNac) <= 0:
		anioNac = input('El año de debe ser un numero positivo.\nIntroduzca  el año de la incidencia: ')

	fechaNac = '-'.join([anioNac, mesNac, diaNac])

	identificador = siguiente_id_tabla(cursor, "RegistraAvisoReparacion", "IdentificadorReparacion")
	
	datos = ["'"+identificador+"'", "'"+num_hab+"'", "'"+descripcion+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD')"]

	sentencia = 'CALL registrar_aviso_reparacion (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

	print("Se ha añadido el aviso de reparación con identificador: " + datos[0])

def reparacion_resuelta(cursor):
	identificador = input("Introduzca el identificador de la reparación que desea marcar como resuelta: ")

	while len(identificador) != 9:
		identificador = input("El número de identificación debe tener 9 caracteres.\nIntroduzca el identificador de la reparación que desea marcar como resuelta: ")

	datos = ["'"+identificador+"'"]

	sentencia = 'CALL marcar_reparacion_resuelta (' + ', ' .join(datos) + ')'

	cursor.execute(sentencia)

	print("Se ha marcado como resuelto el aviso de reparación con identificador: " + datos[0])


def limpieza(cursor):
	dni = input('Introduzca el DNI del empleado: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduzca el DNI del empleado: ')

	num_hab = input('Introduzca el número de habitación a limpiar: ')
	while len(num_hab) != 3:
		num_hab = input('El número de habitacion debe tener 3 digitos.\nIntroduzca el numero de habitación donde se necesita una reparación: ')

	diaNac = input('Introduzca el día de la limpieza: ')

	while int(diaNac) <= 0 or int(diaNac) > 31:
		diaNac = input('El día de la limpieza debe estar comprendido entre 1 y 31.\nIntroduzca el día de limpieza: ')

	mesNac = input('Introduzca el mes de la limpieza: ')

	while int(mesNac) <= 0 or int(mesNac) > 12:
		mesNac = input('El mes debe estar comprendido entre 1 y 12.\nIntroduzca el mes de la limpieza: ')

	anioNac = input('Introduzca el año de la limpieza: ')

	while int(anioNac) <= 0:
		anioNac = input('El año de debe ser un numero positivo.\nIntroduzca  el año de la limpieza: ')

	hora = input('Introduzca la hora de la limpieza: ')

	while int(hora) < 0 or int(hora)>24:
		hora = input('La hora debe estar entre 0 y 24.\nIntroduzca la hora de la limpieza: ')

	minuto = input('Introduzca el minuto de la limpieza: ')

	while int(minuto) < 0 or int(minuto) > 59:
		minuto = input('El minuto de debe ser un número positivo menor a 59.\nIntroduzca  el minuto de la limpieza: ')

	fechaNacaux = '-'.join([anioNac, mesNac, diaNac])
	auxhora = ':'.join([hora, minuto])
	fechaNac = ' '.join([fechaNacaux, auxhora])

	print(fechaNac)

	identificador = siguiente_id_tabla(cursor, "Limpieza", "IdentificadorLimpieza")
	 
	datos = ["'"+identificador+"'", "'"+num_hab+"'", "'"+dni+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD HH24:MI')"]

	sentencia = 'CALL asignar_limpieza (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

	print("Se ha añadido la planificación de limpieza con identificador: " + datos[0])



def provisiones(cursor):
	identificador = input('Introduzca el identificador del producto: ')

	while len(identificador) != 9:
		identificador = input('El identificador debe tener 9 caracteres.\nIntroduzca el identificador del producto: ')

	cantidad = input('Introduzca a cantidad a añadir: ')

	while int(cantidad) < 0:
		minuto = input('La cantidad debe ser un número positivo.\nIntroduzca  la cantidad: ')

	datos = ["'"+identificador+"'", "'"+cantidad+"'"]

	sentencia = 'CALL incrementar_producto (' + ', '.join(datos) + ')'
	print(sentencia)
	cursor.execute(sentencia)
	cursor.commit()

	print("Se ha añadido el producto con identificador: " + datos[0])



def menu_mantenimiento(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE MANTENIMIENTO")
		print("\t1: Registrar aviso de reparación")
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
