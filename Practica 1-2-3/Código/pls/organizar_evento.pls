CREATE OR REPLACE PROCEDURE organizar_evento(
  id_evento VARCHAR2,
  id_sala VARCHAR2,
  descripcion VARCHAR2,
  precio FLOAT,
  fecha DATE
) AS
BEGIN
  INSERT INTO EventoTieneLugarEn (IdentificadorEvento, IdentificadorSala, Descripcion, Precio, FechaHora) VALUES (id_evento, id_sala, descripcion, precio, fecha);
  COMMIT;
END;
