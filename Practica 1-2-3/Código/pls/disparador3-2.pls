CREATE OR REPLACE TRIGGER fechaEntradaPosteriorL
BEFORE INSERT ON Limpieza
FOR EACH ROW
    BEGIN
        IF (FLOOR(MONTHS_BETWEEN(:new.FechaHora, SYSDATE)/12) < 0) THEN 
            RAISE_APPLICATION_ERROR(-20111, 'Error: la fecha de entrada debe ser posterior a la fecha actual');
        END IF;
    END;