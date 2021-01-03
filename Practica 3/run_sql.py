# Recibe un fichero con sentencias sql y devuelve un array con las sentencias listas
# para ser ejecutadas por el método execute de un cursor
def get_sql(file_path):
	sentencias = open(file_path, 'r').read().strip().split(';')
	if '' in sentencias:
		sentencias.remove('') # quitar sentencias vacías para evitar errores
	return sentencias

# Ejecuta todas las sentencias sql de un fichero	
def run_sql(cursor, file_path):
	sentencias = get_sql(file_path)
	for sentencia in sentencias:
		cursor.execute(sentencia)
