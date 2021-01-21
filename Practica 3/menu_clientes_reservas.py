from siguiente_id_tabla import *

def reserva(cursor):
	dni = input('Introduzca el DNI del cliente: ')

	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduzca el DNI del cliente: ')

	tipoHabitacion = input('Introduzca el tipo de habitación que desea reservar: ')

	diaE = input('Introduzca el día de entrada: ')

	while int(diaE) <= 0 or int(diaE) > 31:
		diaE = input('El día de entrada debe estar comprendido entre 1 y 31.\nIntroduzca el día de entrada: ')

	mesE = input('Introduzca el mes de entrada: ')

	while int(mesE) <= 0 or int(mesE) > 12:
		mesE = input('El mes de entrada debe estar comprendido entre 1 y 12.\nIntroduzca el mes de entrada: ')

	anioE = input('Introduzca el año de entrada: ')

	while int(anioE) <= 0:
		anioE = input('El año de entrada debe ser un número positivo.\nIntroduzca el anio de entrada: ')

	fechaE = '-'.join([anioE, mesE, diaE])

	diaS = input('Introduzca el día de salida: ')

	while int(diaS) <= 0 or int(diaS) > 31:
		diaS = input('El día de salida debe estar comprendido entre 1 y 31.\nIntroduzca el día de salida: ')

	mesS = input('Introduzca el mes de salida: ')

	while int(mesS) <= 0 or int(mesS) > 12:
		mesS = input('El mes de salida debe estar comprendido entre 1 y 12.\nIntroduzca el mes de salida: ')

	anioS = input('Introduzca el año de salida: ')

	while int(anioS) <= 0:
		anioS = input('El año de salida debe ser un número positivo.\nIntroduzca el año de salida: ')

	fechaS = '-'.join([anioS, mesS, diaS])

	idReserva = siguiente_id_tabla(cursor, "Reserva", "Identificador")

	datos = ("'"+idReserva+"'", "'"+dni+"'", "'"+tipoHabitacion+"'", "TO_DATE('"+fechaE+"', 'YYYY-MM-DD')", "TO_DATE('"+fechaS+"', 'YYYY-MM-DD')")

	sentencia = 'CALL reservar (' + ', '.join(datos) + ')'
	cursor.execute(sentencia)

	print("Se ha añadido la reserva con identificador: " + datos[0])

def checkin(cursor):

	idReserva = input('Introduzca el identificador de la reserva: ')

	fecha = input("Introduzca fecha y hora (AAAA-MM-DD-HH24:MI): ")

	elegir_habitacion = 'SELECT  IdentificadorHabitacion \
			             FROM Habitacion h \
			             WHERE h.Tipo=(select TipoHab from Reserva where Identificador=\''+idReserva+'\') \
			             MINUS \
			             (SELECT DISTINCT IdentificadorHabitacion \
			             FROM ReservaOcupada r\
			             WHERE r.Identificador NOT IN (SELECT Identificador FROM ReservaFinalizada)) \
			             '
	q = cursor.execute(elegir_habitacion).fetchall()

	if(len(q)==0):
		print("No hay habitaciones disponibles.")
		return

	habitacion = str(q[0][0])

	sentencia = "CALL hacer_checkin ('" + idReserva + "', '" + habitacion + "', TO_DATE('" + fecha + "', 'YYYY-MM-DD-HH24-MI'))"
	cursor.execute(sentencia)

	print("Se ha asignado la habitación con identificador: " + habitacion)

def checkout(cursor):
	num_hab = input('Introduzca el número de la habitación: ')
	while len(num_hab) != 3:
		num_hab = input('El número de habitación debe tener 3 dígitos.\nIntroduzca el número de la habitación: ')


	fecha = input("Introduzca fecha y hora (AAAA-MM-DD-HH24:MI): ")

	obtener_id = 'SELECT Identificador \
				 FROM ReservaOcupada \
				 WHERE IdentificadorHabitacion='+num_hab+'\
				 MINUS \
				 SELECT Identificador \
				 FROM ReservaFinalizada \
				 '
	q = cursor.execute(obtener_id).fetchall()

	if(len(q)==0):
		print("Número de habitación no válido.")
		return;

	idReserva = q[0][0]

	sentencia = "CALL hacer_checkout ('" + idReserva + "', TO_DATE('" + fecha + "', 'YYYY-MM-DD-HH24-MI'))"
	cursor.execute(sentencia)

	print("Se ha realizado el checkout de la reserva " + idReserva);


def cancelar_reserva(cursor):
	idReserva = input('Introduzca el identificador de la reserva: ')

	while len(idReserva) != 9:
		idReserva = input('El identificador de la reserva debe tener una longitud de 9 caracteres.\nIntroduzca el identificador de la reserva: ')

	sentencia = "CALL cancelar_reserva ('" + idReserva + "')"
	cursor.execute(sentencia)

	print("Reserva cancelada.")

def disponibilidad(cursor):
	idTipoH = input('Introduzca el identificador de tipo de habitación: ')

	dia = input('Introduzca el día: ')

	while int(dia) <= 0 or int(dia) > 31:
		dia = input('El día debe estar comprendido entre 1 y 31.\nIntroduzca el día de entrada: ')

	mes = input('Introduzca el mes: ')

	while int(mes) <= 0 or int(mes) > 12:
		mes = input('El mes debe estar comprendido entre 1 y 12.\nIntroduzca el mes: ')

	anio = input('Introduzca el año: ')

	while int(anio) <= 0:
		anio = input('El año debe ser un número positivo.\nIntroduzca el año: ')

	fecha = '-'.join([anio, mes, dia])

	datos = ("'"+idTipoH+"'", "TO_DATE('"+fecha+"', 'YYYY-MM-DD')")

	sentencia1 = 'SELECT COUNT(*) \
	              FROM Habitacion \
	              WHERE Tipo=' + datos[0] + ' \
	             '
	sentencia2 = 'SELECT COUNT(*) \
	              FROM Reserva \
	              WHERE TipoHab=' + datos[0] + '\
	                    AND FechaEntrada <= ' + datos[1] + '\
	                    AND FechaSalida >= ' + datos[1] + '\
	                    AND Identificador NOT IN \
	                    (\
	                    SELECT Identificador FROM ReservaCancelada\
	                    UNION\
	                    SELECT Identificador FROM ReservaFinalizada\
	                    )\
	             '
	totalHabs = cursor.execute(sentencia1).fetchall()[0][0]
	habsOcupadas = cursor.execute(sentencia2).fetchall()[0][0]
	habsDisponibles = int(totalHabs - habsOcupadas)

	if habsDisponibles > 0:
		print("Quedan " + str(habsDisponibles) + " habitaciones disponibles del tipo " + idTipoH + " para la fecha " + fecha)
	else:
		print("No quedan habitaciones disponibles del tipo " + idTipoH + " para la fecha " + fecha)

def menu_clientes_reservas(cursor):
	salir = False
	while not salir:
		print("\nMENÚ PARA LA GESTIÓN DE CLIENTES, RESERVAS Y OCUPACIONES")
		print("\t1: Registrar una reserva")
		print("\t2: Registrar check-in")
		print("\t3: Registrar check-out")
		print("\t4: Cancelar una reserva")
		print("\t5: Consultar la disponibilidad de un tipo de habitación")
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
