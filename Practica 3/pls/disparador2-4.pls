CREATE OR REPLACE TRIGGER habitacionYaOcupada
  BEFORE INSERT OR UPDATE
  ON ReservaOcupada
  FOR EACH ROW
DECLARE
  ocupaciones INTEGER;
BEGIN
  SELECT count(*)
  INTO ocupaciones
  FROM (
    SELECT Identificador
    FROM ReservaOcupada
    WHERE IdentificadorHabitacion = :new.IdentificadorHabitacion
    MINUS
    SELECT Identificador
    FROM ReservaFinalizada
  );

  IF (ocupaciones > 0) THEN
    raise_application_error(-20750, 'Habitación ya ocupada.');
  END IF;

END;
