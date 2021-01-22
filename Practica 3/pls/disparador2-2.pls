CREATE OR REPLACE TRIGGER fechaSalidaPosterior
BEFORE INSERT OR UPDATE ON Reserva
FOR EACH ROW
    BEGIN
        IF (FLOOR(MONTHS_BETWEEN(:new.FechaSalida, :new.FechaEntrada)/12) < 0) THEN
            RAISE_APPLICATION_ERROR(-20111, 'Error: la fecha de salida debe ser posterior a la fecha de entrada');
        END IF;
    END;
