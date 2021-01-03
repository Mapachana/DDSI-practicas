CREATE OR REPLACE TRIGGER fechaEntradaPosteriorR
BEFORE INSERT ON Reserva
FOR EACH ROW
    BEGIN
        IF (FLOOR(MONTHS_BETWEEN(:new.FechaEntrada, SYSDATE)/12) < 0) THEN 
            RAISE_APPLICATION_ERROR(-20111, 'Error: la fecha de entrada debe ser posterior a la fecha actual');
        END IF;
    END;