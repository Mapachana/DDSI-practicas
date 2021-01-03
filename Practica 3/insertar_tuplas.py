from run_sql import run_sql

def insertar_tuplas(cursor):
	print("Insertando tuplas de ejemplo...")
	run_sql(cursor, 'sql/insert.sql')
	print("Hecho")
