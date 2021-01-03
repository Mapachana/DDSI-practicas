CREATE OR REPLACE TRIGGER maximoHabitacionesDia BEFORE INSERT ON Limpieza
BEGIN
	SELECT COUNT(*) INTO numlimp FROM Limpieza l WHERE( l.DNI = '12345689' AND l.FechaHora = 'NULL');
	if (numlimp >= 10) THEN
		DBMS_OUTPUT.PUT_LINE("Error, un empleado no puede limpiar tantas habitaciones en un dia\n");
	END IF
END
