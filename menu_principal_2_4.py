import config

def menu_principal_2_4(cursor):
    cursor.execute('COMMIT')
    print("Pedido finalizado con codifgo de pedido "+str(config.num_pedidos))
