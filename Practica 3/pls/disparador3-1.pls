CREATE OR REPLACE TRIGGER maximoHabitacionesDia BEFORE INSERT OR UPDATE ON Limpieza FOR EACH ROW
DECLARE
    numlimp INTEGER;
BEGIN
	SELECT COUNT(*) INTO numlimp FROM Limpieza l WHERE( l.DNI = :new.DNI AND TO_CHAR(l.FechaHora, 'YYYY-MM-DD') = TO_CHAR(:new.FechaHora, 'YYYY-MM-DD'));
	IF (numlimp >= 10) THEN
		raise_application_error(-20600, :new.DNI || ' no puede limpìar mas de 10 habitaciones en un dia');
	END IF;
END;
