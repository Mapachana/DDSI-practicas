CREATE OR REPLACE PROCEDURE cancelar_reserva(
    identificadorE VARCHAR2
) AS
BEGIN
   	INSERT INTO ReservaCancelada (
     	  Identificador
    ) VALUES (
      	identificadorE
    );
    COMMIT;
END;
