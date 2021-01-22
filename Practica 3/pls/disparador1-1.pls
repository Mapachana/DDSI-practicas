CREATE OR REPLACE TRIGGER edadEmpleado
BEFORE INSERT OR UPDATE ON Empleado
FOR EACH ROW
    BEGIN
        IF (FLOOR(MONTHS_BETWEEN(SYSDATE, :new.FechaNacimiento)/12) < 16) THEN
            RAISE_APPLICATION_ERROR(-20111, 'Error: el empleado debe ser mayor de 16 anios');
        END IF;
    END;
