CREATE OR REPLACE PROCEDURE baja_empleado(
    dniE VARCHAR2
) AS
BEGIN
   	INSERT INTO EmpleadoDeBaja (
     	DNI
    ) VALUES (
      	dniE
    );
    COMMIT;
END;
