CREATE OR REPLACE TRIGGER unicoGerente
  BEFORE INSERT
  ON Empleado
  FOR EACH ROW
DECLARE
  num_gerentes INTEGER;
BEGIN
    IF(:new.Puesto='Gerente') THEN
      SELECT count(*) INTO num_gerentes FROM Empleado WHERE Puesto='Gerente';
      IF(num_gerentes > 0) THEN
        RAISE_APPLICATION_ERROR(-20134, 'Error: solo puede haber un gerente en el sistema');
      END IF;
    END IF;
END;
