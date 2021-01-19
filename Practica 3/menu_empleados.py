def pedirDatos():
	dni = input('Introduce el DNI del empleado: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del empleado: ')

	nombre = input('Introduce el nombre del empleado: ')

	while len(nombre) <= 0 or len(nombre) > 50:
		nombre = input('El nombre debe tener entre 1 y 50 caracteres.\nIntroduce el nombre del empleado: ')

	apellidos = input('Introduce los apellidos del empleado: ')

	while len(apellidos) < 0 or len(apellidos) > 50:
		apellidos = input('Los apellidos deben tener entre 0 y 50 caracteres.\nIntroduce los apellidos del empleado: ')

	telefono = input('Introduce el telefono del empleado: ')

	while len(telefono) != 9:
		telefono = input('El telefono debe tener 9 caracteres.\nIntroduce el telefono del empleado: ')

	puesto = input('Introduce el puesto del empleado: ')

	while len(puesto) <= 0 or len(puesto) > 50:
		puesto = input('El puesto debe tener entre 1 y 50 caracteres..\nIntroduce el puesto del empleado: ')

	diaNac = input('Introduce el dia de nacimiento del empleado: ')

	while int(diaNac) <= 0 or int(diaNac) > 31:
		diaNac = input('El dia de nacimiento debe estar comprendido entre 1 y 31.\nIntroduce el dia de nacimiento del empleado: ')

	mesNac = input('Introduce el mes de nacimiento del empleado: ')

	while int(mesNac) <= 0 or int(mesNac) > 12:
		mesNac = input('El mes de nacimiento debe estar comprendido entre 1 y 12.\nIntroduce el mes de nacimiento del empleado: ')

	anioNac = input('Introduce el anio de nacimiento del empleado: ')

	while int(anioNac) <= 0:
		anioNac = input('El anio de nacimiento debe ser un numero positivo.\nIntroduce  el anio de nacimiento del empleado: ')

	fechaNac = '-'.join([anioNac, mesNac, diaNac])

	nSeguridadSocial = input('Introduce el numero de la seguridad social del empleado: ')

	while len(nSeguridadSocial) != 8:
		nSeguridadSocial = input('El numero de la seguridad social debe tener 8 digitos.\nIntroduce el numero de la seguridad social del empleado: ')

	cuenta = input('Introduce el numero de cuenta del empleado: ')

	while len(cuenta) != 24:
		cuenta = input('El numero de cuenta debe tener 24 digitos.\nIntroduce el numero de cuenta del empleado: ')

	datos = ("'"+dni+"'", "'"+nombre+"'", "'"+apellidos+"'", "'"+telefono+"'", "'"+puesto+"'", "TO_DATE('"+fechaNac+"', 'YYYY-MM-DD')", "'"+nSeguridadSocial+"'", "'"+cuenta+"'")

	return datos

def alta_empleado(cursor):
	datos = pedirDatos()

	sentencia = 'CALL alta_empleado (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

	print("Se ha aniadido el empleado con DNI: " + datos[0])

def modificar_empleado(cursor):
	datos = pedirDatos()

	sentencia = 'CALL modificar_empleado (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

def consultar_empleado(cursor):
	dni = input('Introduce el DNI del empleado a consultar: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del empleado: ')
	
	# Compruebo que no esta dado de baja
	q = cursor.execute("SELECT DNI FROM EmpleadoDeBaja WHERE DNI = '" + dni + "';")
	rows = q.fetchall()
	
	if len(rows) == 0: # Si no esta dado de baja
		q = cursor.execute("SELECT * FROM Empleado WHERE DNI = '" + dni + "';")
		rows = q.fetchall()
		
		print("DNI \tNombre \tApellidos \tTelefono \tPuesto \tFechaNacimiento \tNSeguridadSocial \tCuenta")
	
		if rows is not None:
			for row in rows:
				print(str(row[0]) +"\t\t" + str(row[1]) +"\t\t" + str(row[2]) +"\t\t" + str(row[3]) +"\t\t" + str(row[4]) +"\t\t" + str(row[5]) +"\t\t" + str(row[6]) +"\t\t" + str(row[7]))
		else:
			print("No hay datos en la tabla.")
	else: # Si esta dado de baja
		print("El empleado con DNI " + dni + " esta dado de baja")	

def baja_empleado(cursor):
	dni = input('Introduce el DNI del empleado a dar de baja: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del empleado: ')
	
	sentencia = 'CALL baja_empleado (' + "'" + dni + "'" + ')'
	cursor.execute(sentencia)

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
