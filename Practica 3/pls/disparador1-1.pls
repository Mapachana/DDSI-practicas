CREATE OR REPLACE TRIGGER edadEmpleado
BEFORE INSERT ON Empleado
FOR EACH ROW
    BEGIN 
        IF ((SELECT DATEDIFF(YEAR,FechaNacimiento,GETDATE()) FROM Empleado) < 16) THEN 
            RAISE_APPLICATION_ERROR("11111", "Error: el empleado debe ser mayor de 16 anios");
        END IF;
    END;