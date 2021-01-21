CREATE OR REPLACE PROCEDURE asignar_limpieza(
	identificadorE VARCHAR2,
	num_habE NUMBER,
	dniE VARCHAR2,
	fechaE DATE
) AS
BEGIN
	INSERT INTO Limpieza (
		IdentificadorLimpieza,
		IdentificadorHabitacion,
		DNI,
		FechaHora
	) VALUES (
		IdentificadorE,
		num_habE,
		dniE,
		fechaE
	);
	COMMIT;
END;
