CREATE TABLE Empleado( 
	DNI VARCHAR2(9) PRIMARY KEY, 
	Nombre VARCHAR2(50) NOT NULL, 
	Apellidos VARCHAR2(50) NOT NULL, 
	Telefono INT, 
	Puesto VARCHAR2(50) CHECK(
		Puesto='Gerente' OR 
		Puesto='Recepcionista' OR
		Puesto='Mantenimiento' OR
		Puesto='Limpieza' OR
		Puesto='Eventos'
	) NOT NULL, 
	FechaNacimiento DATE,
	NSeguridadSocial VARCHAR2(8) NOT NULL UNIQUE, Cuenta INT
)

