from listar_tablas import *
from run_sql import run_sql
from run_pls import *
import os # para listar directorio pls

# IMPORTANTE: Esta función elimina todas las tablas de la BD y las crea de nuevo
def crear_tablas(cursor):
	# borrar todas las tablas de la bd
	print("Eliminando todas las tablas de la BD...")
	tablas = listar_tablas(cursor)
	for t in tablas:
		cursor.execute("DROP TABLE " + t + " CASCADE CONSTRAINTS");

	# Crear tablas
	print("Creando nuevas tablas...")
	run_sql(cursor, 'sql/create.sql')
	
	# Añadir disparadores
	print("Añadiendo disparadores...")
	pls_dir = 'pls'
	pls_files = os.listdir(pls_dir)
	for pls_file in pls_files:
		run_pls(cursor, pls_dir + '/' + pls_file)
	
	print("Hecho")
