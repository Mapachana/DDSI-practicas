CREATE OR REPLACE PROCEDURE participante_grupo_excursion(
  id_grupo VARCHAR2,
  dni_participante VARCHAR2
) AS
BEGIN
  INSERT INTO Integrar (IdentificadorGrupo, DNI) VALUES (id_grupo, dni_participante);
END;
