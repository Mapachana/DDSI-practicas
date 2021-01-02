CREATE TABLE Empleado( 
	DNI VARCHAR2(9) PRIMARY KEY, 
	Nombre VARCHAR2 NOT NULL, 
	Apellidos VARCHAR2 NOT NULL, 
	Telefono INT(9), 
	Puesto VARCHAR2 CHECK(
		Puesto=’Gerente’ OR 
		Puesto=’Recepcionista’ OR
		Puesto=’Mantenimiento’ OR
		Puesto=’Limpieza’ OR
		Puesto=’Eventos’
	) NOT NULL, 
	FechaNacimiento DATE,
	NSeguridadSocial VARCHAR2(8) NOT NULL UNIQUE, Cuenta INT(20) 
); 

