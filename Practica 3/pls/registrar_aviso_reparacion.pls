CREATE OR REPLACE PROCEDURE registraravisoreparacion(
    identificadorE VARCHAR2,
    identificador_habE NUMBER,
    descripcionE VARCHAR2,
    fechaE DATE,
) AS
BEGIN
   	INSERT INTO RegistraAvisoReparacion (
     	IdentificadorReparacion,
      	IdentificadorHabitacion,
       	Descripcion,
       	Fecha
    ) VALUES (
      	identificadorE,
       	identificador_habE,
       	descripcionE,
       	fechaE
    );
END;
