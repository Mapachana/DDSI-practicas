CREATE OR REPLACE PROCEDURE incrementar_producto(
	identificadorE VARCHAR2,
	cantidadE NUMBER
) IS
BEGIN
	UPDATE Producto p
	SET p.cantidad = p.cantidad + cantidadE
	WHERE p.IdentificadorProducto = identificadorE
END;
