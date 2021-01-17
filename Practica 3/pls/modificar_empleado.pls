CREATE OR REPLACE PROCEDURE modificar_empleado(
   	dniId VARCHAR2,
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
	UPDATE Empleado SET DNI = dniId WHERE DNI = dniId;
	UPDATE Empleado SET Nombre = nombreE WHERE DNI = dniId;
	UPDATE Empleado SET Apellidos = apellidosE WHERE DNI = dniId;
	UPDATE Empleado SET Telefono = telefonoE WHERE DNI = dniId;
	UPDATE Empleado SET Puesto = puestoE WHERE DNI = dniId;
	UPDATE Empleado SET FechaNacimiento = fechaNacimientoE WHERE DNI = dniId;
	UPDATE Empleado SET NSeguridadSocial = nSeguridadSocialE WHERE DNI = dniId;
	UPDATE Empleado SET Cuenta = cuentaE WHERE DNI = dniId;
END;
