def consultar_estado(cursor):
	# obtener lista de tablas
	tablas = cursor.execute("select table_name from user_tables").fetchall()
	tablas = [x[0] for x in tablas]
	
	# interacción con usuario
	print("Lista de tablas:")
	print(tablas)
	
	tabla_consultar = input("Indique el nombre de la tabla que desea consultar (en mayúsculas): ")
	
	# resultado de la busqueda
	if tabla_consultar in tablas:
		# nombre de las columnas
		for column in cursor.columns(table=tabla_consultar):
			print(column.column_name, end='\t')
		print('')
		
		# tuplas
		cursor.execute("SELECT * FROM " + tabla_consultar)
		for row in cursor:
			for field in row:
				print(field, end='\t')
			print('')
	else:
		print("Tabla no dispobible. Indique una de la lista")
	
