CREATE OR REPLACE PROCEDURE hacer_checkin(
    identificadorE VARCHAR2,
    identificadorHabitacionE INT,
    fechaEntradaE DATE
) AS
BEGIN
   	INSERT INTO ReservaOcupada (
     	Identificador,
    	IdentificadorHabitacion,
     	FechaHoraCheckIn
    ) VALUES (
        identificadorE,
      	identificadorHabitacionE,
       	fechaEntradaE
    );
    COMMIT;
END;
