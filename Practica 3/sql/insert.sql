INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('11111111A', 'Pepe', 'Espagnol', '611111111', 'Gerente', TO_DATE('1970-10-10', 'YYYY-MM-DD'), '11111111', 'ES662100041840123456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('22222222B', 'Carmen', 'San Diego', '622222222', 'Recepcionista', TO_DATE('1985-12-11', 'YYYY-MM-DD'), '22222222', 'ES6621000418401233456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('33333333C', 'Manuel', 'Carrero', '633333333', 'Limpieza', TO_DATE('1965-01-10', 'YYYY-MM-DD'), '33333333', 'ES6621507418401233456365');

INSERT INTO EmpleadoDeBaja (DNI) VALUES ('22222222B');

INSERT INTO EventoTieneLugarEn (IdentificadorEvento, IdentificadorSala, Descripcion, Precio, FechaHora) VALUES ('E00000001', 'S000000001', 'Boda', '200', TO_DATE('2020-10-02 14:00', 'YYYY-MM-DD HH:MI'));

INSERT INTO Sala (IdentificadorSala) VALUES ('S000000001');

INSERT INTO Sala (IdentificadorSala) VALUES ('S000000002');

INSERT INTO Actividad (IdentificadorActividad, Descripcion) VALUES ('A000000001', 'Playa');


