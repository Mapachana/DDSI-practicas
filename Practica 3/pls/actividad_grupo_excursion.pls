CREATE OR REPLACE PROCEDURE actividad_grupo_excursion(
  id_grupo VARCHAR2,
  id_actividad VARCHAR2,
  descripcion VARCHAR2
) AS
BEGIN
  INSERT INTO Actividad (IdentificadorActividad, Descripcion) VALUES (id_actividad, descripcion);
  INSERT INTO Realiza (IdentificadorGrupo, IdentificadorActividad) VALUES (id_grupo, id_actividad);
END;
