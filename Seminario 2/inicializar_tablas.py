import config

def inicializar_tablas(cursor):
	config.num_pedidos = 0

	insert_list = [(1, 10), (2, 13), (3, 24), (4, 89), (5, 36), (6, 17), (7, 52), (8, 43), (9, 32), (10, 96)]

	cursor.execute("CREATE TABLE Stock (Cproducto INT PRIMARY KEY, Cantidad INT)")
	cursor.executemany("INSERT INTO Stock (Cproducto, Cantidad) VALUES (?, ?)", insert_list)

	cursor.execute("CREATE TABLE Pedido (CPedido INT PRIMARY KEY, CCliente INT, FechaPedido DATE)")

	cursor.execute("CREATE TABLE DetallePedido (Cpedido REFERENCES Pedido(Cpedido) ON DELETE CASCADE, Cproducto REFERENCES Stock(Cproducto), Cantidad INT, CONSTRAINT clave_primaria PRIMARY KEY (Cpedido, Cproducto))")

	cursor.execute("COMMIT")

	q = cursor.execute("SELECT * FROM Stock")
	rows = q.fetchall()
	print("STOCK INICIAL")
	print("Cproducto \tCantidad")
	# Recorrer cada una de las filas e imprimirlas en pantalla.
	if rows is not None:
		for row in rows:
			print(str(row[0]) +"\t\t" + str(row[1]))
	else:
		print("No hay datos en la tabla.")

def reinicializar_tablas(cursor):
	cursor.execute("DROP TABLE DetallePedido")
	cursor.execute("DROP TABLE Pedido")
	cursor.execute("DROP TABLE Stock")
	inicializar_tablas(cursor)
