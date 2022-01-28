# Ejecuta una rutina PL/SQL de un fichero
# El fichero debe contener una única función
def run_pls(cursor, file_path):
	sentencia = open(file_path, 'r').read().strip()
	if sentencia != '':
		cursor.execute(sentencia)
