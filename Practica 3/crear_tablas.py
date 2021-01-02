def crear_tablas(cursor):
	# cargar la sentencia sql que crea todas las tablas
	sentencia = open('sql/create.sql', 'r').read().replace("\n", " ")
	
	# ejecutar la sentencia
	cursor.execute(str(sentencia))

