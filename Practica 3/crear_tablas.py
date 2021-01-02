def crear_tablas(cursor):
	# cargar las sentencias sql que crea todas las tablas
	sentencias = open('sql/create.sql', 'r').read().split(';')
	
	# ejecutar la sentencia
	for sentencia in sentencias:
		cursor.execute(sentencia)

