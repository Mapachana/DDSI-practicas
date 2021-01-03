from run_sql import run_sql

# IMPORTANTE: Esta función elimina todas las tablas de la BD y las crea de nuevo
def crear_tablas(cursor):
	# borrar todas las tablas de la bd
	print("Eliminando todas las tablas de la BD...")
	tablas = cursor.execute("select table_name from user_tables").fetchall()
	tablas = [x[0] for x in tablas]
	for t in tablas:
		cursor.execute("DROP TABLE " + t + " CASCADE CONSTRAINTS");

	print("Creando nuevas tablas...")
	run_sql(cursor, 'sql/create.sql')

	#print(cursor.execute("select table_name from user_tables").fetchall())
	
	print("Hecho")
