CREATE OR REPLACE PROCEDURE hacer_checkout(
    identificadorE VARCHAR2,
    fechaSalidaE DATE
)AS

BEGIN
   	INSERT INTO ReservaFinalizada (
     	Identificador,
     	FechaHoraCheckOut
    ) VALUES (
        identificadorE,
       	fechaSalidaE
    );
    COMMIT;
END;
