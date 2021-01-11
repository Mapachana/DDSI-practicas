def reserva(cursor):
	dni = input('Introduce el DNI del cliente: ')
	
	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del cliente: ')

	tipoHabitacion = input('Introduce el tipo de habitacion que desea reservar: ')
	
	diaE = input('Introduce el dia de entrada: ')
	
	while int(diaE) <= 0 or int(diaE) > 31:
		diaE = input('El dia de entrada debe estar comprendido entre 1 y 31.\nIntroduce el dia de entrada: ')
		
	mesE = input('Introduce el mes de entrada: ')

	while int(mesE) <= 0 or int(mesE) > 12:
		mesE = input('El mes de entrada debe estar comprendido entre 1 y 12.\nIntroduce el mes de entrada: ')
	
	anioE = input('Introduce el anio de entrada: ')
	
	while int(anioE) <= 0:
		anioE = input('El anio de entrada debe ser un numero positivo.\nIntroduce  el anio de entrada: ')

	fechaE = '-'.join([anioE, mesE, diaE])
	
	diaS = input('Introduce el dia de salida: ')

	while int(diaS) <= 0 or int(diaS) > 31:
		diaS = input('El dia de salida debe estar comprendido entre 1 y 31.\nIntroduce el dia de salida: ')

	mesS = input('Introduce el mes de salida: ')

	while int(mesS) <= 0 or int(mesS) > 12:
		mesS = input('El mes de salida debe estar comprendido entre 1 y 12.\nIntroduce el mes de salida: ')
	
	anioS = input('Introduce el anio de salida: ')
	
	while int(anioS) <= 0:
		anioS = input('El anio de salida debe ser un numero positivo.\nIntroduce  el anio de salida: ')

	fechaS = '-'.join([anioS, mesS, diaS])
	
	idReserva = 0 # como lo asignamos?
	
	datos = ("'"+dni+"'", "'"+tipoHabitacion+"'", "TO_DATE("+fechaE+", 'YYYY-MM-DD')", "TO_DATE("+fechaS+", 'YYYY-MM-DD')", "'"+idReserva+"'")
# TO DO
#cursor.execute('{CALL reserva (?, ?, ?, ?, ?)}', datos)
#print("Se ha aniadido la reserva con identificador: " + datos[4]) # decir dentro del proceduce

def checkin(cursor):
	dni = input('Introduce el DNI del cliente: ')
	
	while len(dni) != 9:
		dni = input('El DNI debe tener 9 caracteres.\nIntroduce el DNI del cliente: ')
	
	diaE = input('Introduce el dia de entrada: ')
	
	while int(diaE) <= 0 or int(diaE) > 31:
		diaE = input('El dia de entrada debe estar comprendido entre 1 y 31.\nIntroduce el dia de entrada: ')
		
	mesE = input('Introduce el mes de entrada: ')
	
	while int(mesE) <= 0 or int(mesE) > 12:
		mesE = input('El mes de entrada debe estar comprendido entre 1 y 12.\nIntroduce el mes de entrada: ')
		
	anioE = input('Introduce el anio de entrada: ')
	
	while int(anioE) <= 0:
		anioE = input('El anio de entrada debe ser un numero positivo.\nIntroduce  el anio de entrada: ')
	
	fechaE = '-'.join([anioE, mesE, diaE])
	
	idReserva = input('Introduce el identificador de la reserva: ')
	
	while len(idReserva) != 9:
		idReserva = input('El identificador de la reserva debe tener una longitud de 9 caracteres.\nIntroduce el identificador de la reserva: ')
	
	idHabitacion = 0 # como los asignamos?
	datos = ("'"+dni+"'", "TO_DATE("+fechaE+", 'YYYY-MM-DD')", "'"+idReserva+"'", "'"+idHabitacion+"'")

# TO DO
#cursor.execute('{CALL checkin (?, ?, ?, ?)}', datos)
#print("Se ha reservado la habitacion con identificador: " + datos[3]) # decir dentro del proceduce

def checkout(cursor):
	idHabitacion = input('Introduce el identificador de la habitacion: ')
# TO DO
#cursor.execute('{CALL checkout (?)}', idHabitacion)

def cancelar_reserva(cursor):
	idReserva = input('Introduce el identificador de la reserva: ')
	
	while len(idReserva) != 9:
		idReserva = input('El identificador de la reserva debe tener una longitud de 9 caracteres.\nIntroduce el identificador de la reserva: ')
# TO DO
#cursor.execute('{CALL cancelar_reserva (?)}', idReserva)
	
def disponibilidad(cursor):
	idTipoH = input('Introduce el identificador de tipo de habitacion: ')
	
	dia = input('Introduce el dia: ')
	
	while int(dia) <= 0 or int(dia) > 31:
		dia = input('El dia debe estar comprendido entre 1 y 31.\nIntroduce el dia de entrada: ')
	
	mes = input('Introduce el mes: ')
	
	while int(mes) <= 0 or int(mes) > 12:
		mes = input('El mes debe estar comprendido entre 1 y 12.\nIntroduce el mes: ')
	
	anio = input('Introduce el anio: ')
	
	while 