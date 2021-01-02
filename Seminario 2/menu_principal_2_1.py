import config

def menu_principal_2_1(cursor):
    print("Introduce el codigo del producto")
    codigo_producto = str(int(input()))

    print("Introduce la cantidad")
    cantidad = int(input())

    respuesta = cursor.execute("Select Cantidad from Stock where Cproducto=" + codigo_producto).fetchall()
    if len(respuesta) == 0:
        print("No existe dicho producto")

    elif len(cursor.execute("Select * from DetallePedido where Cpedido="+str(config.num_pedidos)+" and Cproducto="+codigo_producto).fetchall()) != 0:
        print("Dicho producto ya esta incluido")

    else:
        cantidadDisponible = int(respuesta[0][0])

        if cantidad <= cantidadDisponible and cantidad > 0:
            cursor.execute("INSERT INTO DetallePedido VALUES (" + str(config.num_pedidos) + ", " + codigo_producto + ", " + str(cantidad) + ")")
            cantidadDisponible -= cantidad
            cursor.execute("UPDATE Stock set cantidad=" + str(cantidadDisponible) + " where Cproducto=" + codigo_producto)
            print("Producto incluido")
        else:
            print("No hay suficiente stock de dicho producto")
