import pyodbc
from datetime import datetime
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name= practbd.oracle0.ugr.es;User ID=x7770080;Password=x7770080')

cursor = cnxn.cursor()
num_pedidos = 0
#cursor.execute("CREATE TABLE prueba (personid INT, cosa INT)")

insert_list = [(1, 10), (2, 13), (3, 24), (4, 89), (5, 36), (6, 17), (7, 52), (8, 43), (9, 32), (10, 96)]

cursor.execute("DROP TABLE DetallePedido")
cursor.execute("DROP TABLE Pedido")
cursor.execute("DROP TABLE Stock")

cursor.execute("CREATE TABLE Stock (Cproducto INT PRIMARY KEY, Cantidad INT)")
cursor.executemany("INSERT INTO Stock (Cproducto, Cantidad) VALUES (?, ?)", insert_list)

cursor.execute("CREATE TABLE Pedido (CPedido INT PRIMARY KEY, CCliente INT, FechaPedido DATE)")

cursor.execute("CREATE TABLE DetallePedido (Cpedido REFERENCES Pedido(Cpedido), Cproducto REFERENCES Stock(Cproducto), Cantidad INT, CONSTRAINT clave_primaria PRIMARY KEY (Cpedido, Cproducto))")

cursor.commit()

q = cursor.execute("SELECT * FROM Stock")
rows = q.fetchall()
# Recorrer cada una de las filas e imprimirlas en pantalla.
if rows is not None:
    for row in rows:
        print(row)
else:
    print("No hay datos en la tabla.")


def menu_principal():
	print("Pulse 1 para reinicializar las tablas,\n 2 para dar de alta un pedido,\n 3 para borrar un pedido,\n 4 para salir\n")
	opcion = input()
	if opcion == "1":
		print("jaja no lo has hecho")
	elif opcion == "2":
		menu_pedido()
	elif opcion == "3":
		print("otro menu")
	elif opcion == "4":
		cursor.close()
		cnxn.close()
		print("Gracias por usarnos")
		exit(0)

def menu_pedido():
	print("Por favor introduzca el codigo de cliente")
	codigo = input()
	pidiendo = true
	num_pedidos += 1
	cursor.execute("INSERT INTO Pedido VALUES ("+str(num_pedidos)+", "+codigo+", "+datetime.today().strftime('%Y-%m-%d')+")")
	
	while(pidiendo):
		print("Pulse 1 para añadir detalle de producto,\n 2 para eliminar todos los detalles de producto,\n 3 para cancelar pedido,\n 4 para confirmar y terminar pedido\n")
		opcion = input()
		if opcion == "1":
			print("jaja no lo has hecho")
		elif opcion == "2":
			print("llora")
		elif opcion == "3":
			print("otro menu")
			pidiendo = false
		elif opcion == "4":
			cursor.close()
			cnxn.close()
			print("Gracias por usarnos")
			pidiendo = false
			exit(0)

		
	



