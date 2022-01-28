CREATE OR REPLACE TRIGGER salaDisponible
BEFORE INSERT OR UPDATE ON EventoTieneLugarEn
FOR EACH ROW
DECLARE
	numevent INTEGER;
BEGIN
	SELECT count(*) INTO numevent FROM EventoTieneLugarEn e WHERE (e.IdentificadorSala = :new.IdentificadorSala AND e.FechaHora = :new.FechaHora);
	IF (numevent > 2) THEN
		raise_application_error(-20601, :new.IdentificadorSala || ' no puede albergar mas eventos en esa fecha y hora');
	END IF;
END;
