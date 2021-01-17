def aviso_reparacion(cursor):
	num_hab = input('Introduzca el numero de habitacion donde se necesita una reparacion: ')
	while len(num_hab) != 3:
		num_hab = input('El numero de habitacion debe tener 3 digitos.\nIntroduzca el numero de habitacion donde se necesita una reparacion: ')

	descripcion = input('Introduzca la descripcion del problema: ')
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

	datos = ["'"+identificador+"'", "'"+num_hab+"'", "'"+descripcion+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD')"]

	sentencia = 'CALL registrar_aviso_reparacion (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)
	cursor.commit()

	print("Se ha aniadido el aviso de reparacion con identificador: " + datos[0])
	
def reparacion_resuelta(cursor):
	identificador = input("Introduzca el identificador de la reparacion que desea marcar como resuelta: ")
	
	while len(identificador) != 9:
		identificador = input("El numero de identificacion debe tener 9 caracteres.\nIntroduzca eel identificador de la reparacion que desea marcar como resuelta: ")
		
	datos = ["'"+identificador+"'"]

	sentencia = 'CALL marcar_reparacion_resuelta (' + ', ' .join(datos) + ')'

	cursor.execute(sentencia)
	cursor.commit()

	print("Se ha marcado como resuelto el aviso de reparacion con identificador: " + datos[0])
	

def limpieza(cursor):	
	dni = input('Introduce el DNI del empleado: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del empleado: ')
		
	num_hab = input('Introduzca el numero de habitacion donde se necesita una reparacion: ')
	while len(num_hab) != 3:
		num_hab = input('El numero de habitacion debe tener 3 digitos.\nIntroduzca el numero de habitacion donde se necesita una reparacion: ')

	diaNac = input('Introduce el dia de la incidencia: ')

	while int(diaNac) <= 0 or int(diaNac) > 31:
		diaNac = input('El dia de la limpieza debe estar comprendido entre 1 y 31.\nIntroduce el dia de limpieza: ')

	mesNac = input('Introduce el mes de la limpieza: ')

	while int(mesNac) <= 0 or int(mesNac) > 12:
		mesNac = input('El mes de debe estar comprendido entre 1 y 12.\nIntroduce el mes de lalimpieza: ')

	anioNac = input('Introduce el anio de la limpieza: ')

	while int(anioNac) <= 0:
		anioNac = input('El anio de debe ser un numero positivo.\nIntroduce  el anio de la limpieza: ')
		
	hora = input('Introduce la hora de la limpieza: ')

	while int(hora) < 0 or int(hora)>12:
		hora = input('La hora debe estar entre 0 y 12.\nIntroduce  la hora de la limpieza: ')
		
	minuto = input('Introduce el minuto de la limpieza: ')

	while int(minuto) < 0 or int(minuto) > 59:
		minuto = input('El minuto de debe ser un numero positivo menor a 59.\nIntroduce  el minuto de la limpieza: ')

	fechaNacaux = '-'.join([anioNac, mesNac, diaNac])
	auxhora = ':'.join([hora, minuto])
	fechaNac = ' '.join([fechaNacaux, auxhora])
	
	print(fechaNac)
	
	identificador = "L0000004" #FIXME hay que hacer un identificador unico

	datos = ["'"+identificador+"'", "'"+num_hab+"'", "'"+dni+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD HH:MI')"]

	sentencia = 'CALL asignar_limpieza (' + ', '.join(datos) + ')'
	print(sentencia)
	cursor.execute(sentencia)
	cursor.commit()

	print("Se ha aniadido el aviso de reparacion con identificador: " + datos[0])
		
		

def provisiones(cursor):
	identificador = input('Introduce el identificador del producto: ')

	while len(identificador) != 9:
		minuto = input('El identificador debe tener 9 caracteres.\nIntroduzca el identificador del producto: ')

	cantidad = input('Introduce a cantidad a aniadir: ')

	while int(cantidad) < 0:
		minuto = input('La cantidad de debe ser un numero positivo.\nIntroduce  la cantidad: ')
		
	datos = ["'"+identificador+"'", "'"+cantidad+"'"]

	sentencia = 'CALL incrementar_producto (' + ', '.join(datos) + ')'
	print(sentencia)
	cursor.execute(sentencia)
	cursor.commit()

	print("Se ha aniadido el aviso de reparacion con identificador: " + datos[0])
		


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
			
