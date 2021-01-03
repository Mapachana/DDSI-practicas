CREATE OR REPLACE TRIGGER NoCancelarReservaOcupada
  BEFORE INSERT
  ON ReservaCancelada
  FOR EACH ROW
DECLARE
  reservas INTEGER;
BEGIN
  SELECT COUNT(*)
  INTO reservas
  FROM ReservaOcupada
  WHERE ReservaOcupada.identificador = :new.identificador;

  IF (reservas > 0) THEN
    raise_application_error(-20700, 'No se puede cancelar una reserva ocupada.');
  END IF;
  
END;
