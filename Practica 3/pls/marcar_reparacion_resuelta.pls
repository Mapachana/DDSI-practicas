CREATE OR REPLACE PROCEDURE marcar_reparacion_resuelta(
	identificadorE VARCHAR2
) AS
BEGIN
	INSERT INTO ReparacionResuelta (
		IdentificadorReparacion
	) VALUES (
		identificadorE
	);
END;
