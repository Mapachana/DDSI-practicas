def listar_tablas(cursor):
	tablas = cursor.execute("select table_name from user_tables").fetchall()
	tablas = [x[0] for x in tablas]
	return tablas
