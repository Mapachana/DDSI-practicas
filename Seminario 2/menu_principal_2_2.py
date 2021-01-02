def menu_principal_2_2(cursor):
    cursor.execute('ROLLBACK TO INICIO_DETALLES')
    print("Detalles eliminados")
    cursor.execute("SAVEPOINT INICIO_DETALLES")
