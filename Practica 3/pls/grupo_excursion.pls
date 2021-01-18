CREATE OR REPLACE PROCEDURE grupo_excursion(
  id_grupo VARCHAR2,
  dni_guia VARCHAR2,
  fecha DATE
) AS
BEGIN
  INSERT INTO GrupoDirigidoPor (IdentificadorGrupo, IdentificadorGuia, FechaHora) VALUES (id_grupo, dni_guia, fecha);
END;
