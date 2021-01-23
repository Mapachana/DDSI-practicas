CREATE OR REPLACE PROCEDURE aniadir_producto(
	identificadorE VARCHAR2,
	cantidadE NUMBER
) IS
BEGIN
    INSERT INTO Producto (
        IdentificadorProducto,
        cantidad
    ) VALUES (
        identificadorE,
        cantidadE
    );
	COMMIT;
END;