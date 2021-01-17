CREATE OR REPLACE PROCEDURE incrementar_producto(
	identificadorE VARCHAR2,
	cantidadE NUMBER
) AS
BEGIN
	UPDATE Producto p
	SET p.Cantidad = p.Cantidad + cantidadE
	WHERE p.IdentificadorProducto = identificadorE;
END;
