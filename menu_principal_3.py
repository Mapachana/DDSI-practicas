import inicializar_tablas

def menu_principal_3(cursor):
	print("MENÚ BORRAR UN PEDIDO")	
	print("Por favor introduzca el codigo del pedido que desea borrar")
	codigo = input()
	q = cursor.execute("SELECT * FROM Pedido WHERE CPedido = " + codigo)
	rows = q.fetchall()

	if len(rows) == 0:
		print("No se encuentra ese producto")
	else:
		cursor.execute("DELETE FROM Pedido WHERE CPedido = " + codigo)
		inicializar_tablas.num_pedidos -= 1	

	return 0
