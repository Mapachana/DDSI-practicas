# Estructura del código
- Main.py
	- Se conecta a la base de datos, crea una instancia "cursor"
	- Inicializa las tablas: función incializar_tablas(cursor) en el fichero inicializar_tablas.py
	- Menú principal: función menu_principal(cursor) en el fichero menu_principal.py
		- Salir = False
		- Pide una opción, 1 a 4 y llama a la función correspondiente:
			- Opción 1: función menu_principal_1(cursor) en el fichero menu_principal_1.py
			- Opción 2: análogo
			- Opción 3: análogo
			- Opción 4: salir = True para devolver el flujo al menu_principal
		- Si salir = False, vuelve a pedir opción; si salir = True, termina la función.
	- Termina correctamente el programa
	
# Normas de estilo
- main() es la única función que finaliza el programa, el resto de funciones sólo devuelven el flujo a la función invocante, según corresponda.
- Si la función menu_principal_i(cursor) despliega a su vez un menú con opciones y el usuario elije la opción j, se llamará a la función menu_i_j(cursor), implementada en el fichero menu_i_j.py (si no existe el fichero deberá crearse). Si la opción j consiste en "salir de menu_principal_i(cursor)", no se implementará ninguna función extra, tan sólo se escribirá la(s) sentencia(s) necesarias para devolver el flujo a menu_principal(cursor).
- Si se considera conveniente, en especial por la necesidad de reutilizar algún bloque de código, se podrán crear nuevas funciones, cada una en un fichero con el mismo nombre de la función, como sucede con la función inicializar_tablas(cursor) en el fichero inicializar_tablas.py. Esta función se llama en main(), pero también en menu_principal_1(), por lo que crearla en un fichero separado ha sido ventajoso.
- Debe prestarse especial atención al estilo de los mensajes de la interfaz de texto, usando líneas en blanco y tabulaciones cuando sea oportuno, como se hace en menu_principal(cursor)

# Otra información de interés
- Existe un fichero Makefile, por lo que para lanzar el programa basta con ejecutar la orden "make" en el directorio en el que se encuentra main.py y el resto de ficheros de código fuente.
