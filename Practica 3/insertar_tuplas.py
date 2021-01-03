from crear_tablas import *
from run_sql import run_sql

def insertar_tuplas(cursor):
	crear_tablas(cursor)

	print("Insertando tuplas de ejemplo...")
	run_sql(cursor, 'sql/insert.sql')
	print("Hecho")
	
	#FALTA HACER UN COMMIT
