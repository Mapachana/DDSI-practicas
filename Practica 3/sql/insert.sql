INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('11111111A', 'Pepe', 'Espagnol', '611111111', 'Gerente', TO_DATE('1970-10-10', 'YYYY-MM-DD'), '11111111', 'ES662100041840123456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('22222222B', 'Carmen', 'San Diego', '622222222', 'Recepcionista', TO_DATE('1985-12-11', 'YYYY-MM-DD'), '22222222', 'ES6621000418401233456789');

INSERT INTO Empleado (DNI, Nombre, Apellidos, Telefono, Puesto, FechaNacimiento, NSeguridadSocial, Cuenta) VALUES ('33333333C', 'Manuel', 'Carrero', '633333333', 'Limpieza', TO_DATE('1965-01-10', 'YYYY-MM-DD'), '33333333', 'ES6621507418401233456365');

INSERT INTO EmpleadoDeBaja (DNI) VALUES ('22222222B');

INSERT INTO Sala (IdentificadorSala) VALUES ('S00000001');

INSERT INTO Sala (IdentificadorSala) VALUES ('S00000002');

INSERT INTO EventoTieneLugarEn (IdentificadorEvento, IdentificadorSala, Descripcion, Precio, FechaHora) VALUES ('E00000001', 'S00000001', 'Boda', '200', TO_DATE('2020-10-02 10:00', 'YYYY-MM-DD HH:MI'));

INSERT INTO Actividad (IdentificadorActividad, Descripcion) VALUES ('A00000001', 'Playa');

INSERT INTO Guia (IdentificadorGuia) VALUES ('12345678B');

INSERT INTO GrupoDirigidoPor (IdentificadorGrupo, IdentificadorGuia, FechaHora) VALUES ('G00000001', '12345678B', TO_DATE('2020-12-23', 'YYYY-MM-DD'));

INSERT INTO Realiza (IdentificadorGrupo, IdentificadorActividad) VALUES ('G00000001', 'A00000001');

INSERT INTO Cliente (DNI, CorreoElectronico) VALUES ('12345678S', 'pepitojd97@go.ugr.es');

INSERT INTO Cliente (DNI, CorreoElectronico) VALUES ('72435678S', 'rosalinda@go.ugr.es');

INSERT INTO Integrar (IdentificadorGrupo, DNI) VALUES ('G00000001', '12345678S');

INSERT INTO TipoDeHabitacion (Tipo) VALUES ('I');

INSERT INTO TipoDeHabitacion (Tipo) VALUES ('D');

INSERT INTO TipoDeHabitacion (Tipo) VALUES ('S');

INSERT INTO Individual (Tipo) VALUES ('I');

INSERT INTO Doble (Tipo) VALUES ('D');

INSERT INTO Suite (Tipo) VALUES ('S');

INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('100','I');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('101','I');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('102','I');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('103','I');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('104','I');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('105','D');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('106','D');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('107','D');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('108','D');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('200','S');
INSERT INTO Habitacion (IdentificadorHabitacion, Tipo) VALUES ('201','S');

INSERT INTO Reserva (Identificador, DNI, TipoHab, FechaEntrada, FechaSalida) VALUES ('R00000001', '12345678S', 'I', TO_DATE('2021-12-11', 'YYYY-MM-DD'), TO_DATE('2021-12-14', 'YYYY-MM-DD'));

INSERT INTO Reserva (Identificador, DNI, TipoHab, FechaEntrada, FechaSalida) VALUES ('R00000002', '72435678S', 'D', TO_DATE('2021-12-13', 'YYYY-MM-DD'), TO_DATE('2021-12-17', 'YYYY-MM-DD'));

INSERT INTO Reserva (Identificador, DNI, TipoHab, FechaEntrada, FechaSalida) VALUES ('R00000003', '72435678S', 'S', TO_DATE('2021-12-18', 'YYYY-MM-DD'), TO_DATE('2021-12-19', 'YYYY-MM-DD'));


INSERT INTO ReservaOcupada (Identificador, IdentificadorHabitacion, FechaHoraCheckIn) VALUES ('R00000001', 101, TO_DATE('2021-12-7 12:30', 'YYYY-MM-DD HH:MI'));

INSERT INTO ReservaOcupada (Identificador, IdentificadorHabitacion, FechaHoraCheckIn) VALUES ('R00000002', 102, TO_DATE('2021-12-7 12:30', 'YYYY-MM-DD HH:MI'));


INSERT INTO ReservaFinalizada (Identificador, FechaHoraCheckOut) VALUES ('R00000001', TO_DATE('2021-12-12 12:30', 'YYYY-MM-DD HH:MI' ));

INSERT INTO ReservaCancelada (Identificador) VALUES ('R00000003');



