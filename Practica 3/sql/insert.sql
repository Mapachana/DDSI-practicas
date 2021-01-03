INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('11111111A', 'Pepe', 'Espagnol', '611111111', 'Gerente', TO_DATE('1970-10-10', 'YYYY-MM-DD'), '11111111', 'ES662100041840123456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('22222222B', 'Carmen', 'San Diego', '622222222', 'Recepcionista', TO_DATE('1985-12-11', 'YYYY-MM-DD'), '22222222', 'ES6621000418401233456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('33333333C', 'Manuel', 'Carrero', '633333333', 'Limpieza', TO_DATE('1965-01-10', 'YYYY-MM-DD'), '33333333', 'ES6621507418401233456365');

INSERT INTO EmpleadoDeBaja (DNI) VALUES ('22222222B');

INSERT INTO Sala (IdentificadorSala) VALUES ('S00000001');

INSERT INTO Sala (IdentificadorSala) VALUES ('S00000002');

INSERT INTO EventoTieneLugarEn (IdentificadorEvento, IdentificadorSala, Descripcion, Precio, FechaHora) VALUES ('E00000001', 'S00000001', 'Boda', '200', TO_DATE('2020-10-02 10:00', 'YYYY-MM-DD HH:MI'));

INSERT INTO Actividad (IdentificadorActividad, Descripcion) VALUES ('A00000001', 'Playa');

INSERT INTO Guia (IdentificadorGuia) VALUES ('12345679B');

INSERT INTO GrupoDirigidoPor (IdentificadorGrupo, IdentificadorGuia, FechaHora) VALUES ('G00000001', '12345678B', TO_DATE('2020-12-23', 'YYYY-MM-DD'));

INSERT INTO Realiza (IdentificadorGrupo, IdentificadorActividad) VALUES ('G00000001', 'A00000001');

INSERT INTO Integrar (IdentificadorGrupo, DNI) VALUES ('G00000001', '12345678S');



