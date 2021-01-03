from listar_tablas import *
from run_sql import run_sql

# IMPORTANTE: Esta función elimina todas las tablas de la BD y las crea de nuevo
def crear_tablas(cursor):
	# borrar todas las tablas de la bd
	print("Eliminando todas las tablas de la BD...")
	tablas = listar_tablas(cursor)
	for t in tablas:
		cursor.execute("DROP TABLE " + t + " CASCADE CONSTRAINTS");

	print("Creando nuevas tablas...")
	run_sql(cursor, 'sql/create.sql')
	
	print("Hecho")
