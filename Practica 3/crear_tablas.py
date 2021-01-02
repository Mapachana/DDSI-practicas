def crear_tablas(cursor):
	# cargar la sentencia sql que crea todas las tablas
	sentencia = open('sql/create.sql', 'r').read()
	
	# ejecutar la sentencia
	cursor.execute(sentencia)
