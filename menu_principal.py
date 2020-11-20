from menu_principal_1 import *
from menu_principal_2 import *
from menu_principal_3 import *

def menu_principal(cursor):
	opciones_validas = range(1, 5) # 1, 2, 3, 4
	
	salir = False
	while not salir:
		opcion = 0
		while not opcion in opciones_validas:
			print("MENÚ PRINCIPAL:\n\tOpciones:\n\t\t1: reinicializar tablas\n\t\t2: dar de alta un pedido\n\t\t3: borrar un pedido\n\t\t4: salir\n")
			opcion = int(input())
			
			if not opcion in opciones_validas:
				print("Por favor introduzca una opción válida")
			
		if opcion == 1:
			menu_principal_1(cursor)
			
		elif opcion == 2:
			menu_principal_2(cursor)
			
		elif opcion == 3:
			menu_principal_3(cursor)
			
		elif opcion == 4: # salir: se encarga el programa principal de finalizar correctamente
			print("Gracias por su visita")
			salir = True
			
