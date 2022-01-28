# Siguiente id a uno dado
# Asumimos que id es de la fora caracter alfabetico + caracteres numericos
def siguiente_id(id):
	car = id[0]
	sig = str(int(id[1:]) + 1)
	return str(car) + (8-len(sig))*'0' + sig

# nombre_clave (id) de la proxima tupla que se insertara en la tabla
# tabla debe existir en la bd
def siguiente_id_tabla(cursor, tabla, nombre_clave):
	max_id = cursor.execute("SELECT MAX(" + nombre_clave + ") FROM " + tabla).fetchall()[0][0]
	return siguiente_id(max_id)
