CREATE OR REPLACE PROCEDURE alta_empleado(
    dniE VARCHAR2,
    nombreE VARCHAR2,
    apellidosE VARCHAR2,
    telefonoE CHAR,
    puestoE VARCHAR2,
    fechaNacimientoE DATE,
	nSeguridadSocialE VARCHAR2,
	cuentaE CHAR
) AS
BEGIN
   	INSERT INTO Empleado (
     	DNI,
      	Nombre,
       	Apellidos,
       	Telefono,
       	Puesto,
       	FechaNacimiento,
       	NSeguridadSocial,
       	Cuenta
    ) VALUES (
      	dniE,
       	nombreE,
       	apellidosE,
       	telefonoE,
       	puestoE,
       	fechaNacimientoE,
       	nSeguridadSocialE,
       	cuentaE
    );
END;
