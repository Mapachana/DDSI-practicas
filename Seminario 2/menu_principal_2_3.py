def menu_principal_2_3(cursor):
    cursor.execute('ROLLBACK TO INICIO_PEDIDO')
    print("Pedido cancelado")
