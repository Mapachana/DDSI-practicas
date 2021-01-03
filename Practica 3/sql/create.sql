CREATE TABLE Empleado(
	DNI VARCHAR2(9) PRIMARY KEY,
	Nombre VARCHAR2(50) NOT NULL,
	Apellidos VARCHAR2(50) NOT NULL,
	Telefono CHAR(9),
	Puesto VARCHAR2(50) CHECK(
		Puesto='Gerente' OR
		Puesto='Recepcionista' OR
		Puesto='Mantenimiento' OR
		Puesto='Limpieza' OR
		Puesto='Eventos'
	) NOT NULL,
	FechaNacimiento DATE,
	NSeguridadSocial VARCHAR2(8) NOT NULL UNIQUE,
	Cuenta CHAR(24)
);
CREATE TABLE EmpleadoDeBaja(
    DNI VARCHAR2(9) PRIMARY KEY REFERENCES Empleado(DNI) ON DELETE CASCADE
);

CREATE TABLE Cliente(
    DNI VARCHAR2(9) PRIMARY KEY,
    CorreoElectronico VARCHAR2(30)
);

CREATE TABLE TipoDeHabitacion(
    Tipo CHAR PRIMARY KEY CHECK (Tipo='I' OR Tipo='D' OR Tipo='S')
);
CREATE TABLE Individual(
    Tipo CHAR REFERENCES TipoDeHabitacion(Tipo) PRIMARY KEY
);

CREATE TABLE Doble(
    Tipo CHAR REFERENCES TipoDeHabitacion(Tipo) PRIMARY KEY
);

CREATE TABLE Suite(
    Tipo CHAR REFERENCES TipoDeHabitacion(Tipo) PRIMARY KEY
);
CREATE TABLE Habitacion(
    IdentificadorHabitacion INT PRIMARY KEY,
    Tipo CHAR(1) REFERENCES TipoDeHabitacion(Tipo) NOT NULL
);

CREATE TABLE Reserva(
    Identificador VARCHAR2(9) PRIMARY KEY,
    DNI VARCHAR2(9) REFERENCES Cliente(DNI) NOT NULL,
    TipoHab CHAR(1) REFERENCES TipoDeHabitacion(Tipo) NOT NULL,
    FechaEntrada DATE NOT NULL,
    FechaSalida DATE NOT NULL
);
CREATE TABLE ReservaCancelada(
    Identificador VARCHAR2(9) REFERENCES Reserva(Identificador) PRIMARY KEY
);
CREATE TABLE ReservaOcupada(
    Identificador VARCHAR2(9) REFERENCES Reserva(Identificador) PRIMARY KEY,
    IdentificadorHabitacion INT REFERENCES Habitacion(IdentificadorHabitacion) NOT NULL,
    FechaHoraCheckIn DATE NOT NULL,
    UNIQUE (IdentificadorHabitacion, FechaHoraCheckIn)
);
CREATE TABLE ReservaFinalizada(
    Identificador VARCHAR2(9) REFERENCES ReservaOcupada(Identificador) PRIMARY KEY,
    FechaHoraCheckOut DATE NOT NULL
);

CREATE TABLE Guia(
	IdentificadorGuia VARCHAR2(9) PRIMARY KEY
);

CREATE TABLE Actividad(
	IdentificadorActividad VARCHAR2(9) PRIMARY KEY,
	Descripcion VARCHAR2(100)
);

CREATE TABLE GrupoDirigidoPor(
    IdentificadorGrupo VARCHAR2(9) PRIMARY KEY,
    IdentificadorGuia VARCHAR2(9) REFERENCES Guia(IdentificadorGuia) NOT NULL,
    FechaHora DATE NOT NULL,
    UNIQUE(IdentificadorGuia, FechaHora)
);

CREATE TABLE Realiza(
    IdentificadorGrupo VARCHAR2(9) REFERENCES GrupoDirigidoPor(IdentificadorGrupo),
    IdentificadorActividad VARCHAR2(9) REFERENCES Actividad(IdentificadorActividad),
    PRIMARY KEY (IdentificadorGrupo, IdentificadorActividad)
);

CREATE TABLE Integrar(
    IdentificadorGrupo VARCHAR2(9) REFERENCES GrupoDirigidoPor(IdentificadorGrupo),
    DNI VARCHAR2(9) REFERENCES Cliente(DNI),
    PRIMARY KEY (IdentificadorGrupo, DNI)
);


CREATE TABLE Sala(
	IdentificadorSala VARCHAR2(9) PRIMARY KEY
);

CREATE TABLE EventoTieneLugarEn(
	IdentificadorEvento VARCHAR2(9) PRIMARY KEY,
	IdentificadorSala VARCHAR2(9) REFERENCES Sala(IdentificadorSala) NOT NULL,
	Descripcion VARCHAR2(100),
	Precio FLOAT NOT NULL CHECK(Precio > 0),
	FechaHora DATE NOT NULL
);

CREATE TABLE TrabajaEn(
    DNI VARCHAR2(9) REFERENCES Empleado(DNI) ON DELETE CASCADE,
    IdentificadorEvento VARCHAR2(9) REFERENCES EventoTieneLugarEn(IdentificadorEvento) ON DELETE CASCADE,
    PRIMARY KEY(DNI, IdentificadorEvento)
);

CREATE TABLE Producto(
    IdentificadorProducto VARCHAR2(9) PRIMARY KEY,
    Cantidad INT CHECK(Cantidad >= 0) NOT NULL
);

CREATE TABLE Limpieza(
    IdentificadorLimpieza VARCHAR2(9) PRIMARY KEY,
    IdentificadorHabitacion INT REFERENCES Habitacion(IdentificadorHabitacion) NOT NULL,
	DNI VARCHAR2(9) REFERENCES Empleado(DNI) NOT NULL,
	FechaHora DATE NOT NULL,
	UNIQUE (IdentificadorHabitacion, DNI, FechaHora)

);

CREATE TABLE RegistraAvisoReparacion(
    IdentificadorReparacion VARCHAR2(9) PRIMARY KEY,
    IdentificadorHabitacion INT REFERENCES Habitacion(IdentificadorHabitacion) NOT NULL,
		Descripcion VARCHAR2(100),
		Fecha DATE
);

CREATE TABLE ReparacionResuelta(
    IdentificadorReparacion VARCHAR2(9) REFERENCES RegistraAvisoReparacion(IdentificadorReparacion) PRIMARY KEY
);
