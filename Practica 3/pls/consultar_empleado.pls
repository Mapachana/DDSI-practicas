CREATE OR REPLACE PROCEDURE consultarEmpleado(
   	dniId VARCHAR2
)
AS
	empleadoDNI Empleado%ROWTYPE;
BEGIN
	SELECT * INTO empleadoDNI FROM Empleado e WHERE e.DNI = dniId;
	DBMS_OUTPUT.PUT_LINE(to_char(empleadoDNI.DNI) || ' ' || to_char(empleadoDNI.Nombre) || ' ' || to_char(empleadoDNI.Apellidos) || ' ' || to_char(empleadoDNI.Telefono) || ' ' || to_char(empleadoDNI.Puesto) || ' ' || to_char(empleadoDNI.FechaNacimiento) || ' ' || to_char(empleadoDNI.NSeguridadSocial) || ' ' || to_char(empleadoDNI.Cuenta));
EXCEPTION
	WHEN OTHERS THEN
		DBMS_OUTPUT.PUT_LINE('ERROR');
END;
