# Siguiente id a uno dado
# Asumimos que id es de la fora caracter alfabetico + caracteres numericos
def siguiente_id(id):
	car = id[0]
	return car + str(int(id[1:]) + 1)

# Id de la proxima tupla que se insertara en la tabla
# tabla debe existir en la bd
def siguiente_id_tabla(tabla):
