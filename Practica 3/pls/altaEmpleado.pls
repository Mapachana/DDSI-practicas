FUNCTION altaEmpleado(
    dniE VARCHAR2(9),
    nombreE VARCHAR2(50),
    apellidosE VARCHAR2(50),
    telefonoE CHAR(9),
    puestoE VARCHAR2(50),
    fechaNacimientoE DATE,
	nSeguridadSocialE VARCHAR2(8),
	cuentaE CHAR(24)
) RETURN VARCHAR2(9) IS
    dniE VARCHAR2(9);

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
    RETURN (dniE);
END;