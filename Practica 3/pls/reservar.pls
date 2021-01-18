CREATE OR REPLACE PROCEDURE reservar(
    identificadorE VARCHAR2,
    dniE VARCHAR2,
    tipoHabE CHAR,
    fechaEntradaE DATE,
    fechaSalidaE DATE
) AS
BEGIN
   	INSERT INTO Reserva (
     	Identificador,
    	DNI,
     	TipoHab,
     	FechaEntrada,
     	FechaSalida
    ) VALUES (
        identificadorE,
      	dniE,
       	tipoHabE,
       	fechaEntradaE,
       	fechaSalidaE
    );
    COMMIT;
END;
