from . import db

# Modelo de Inscripciones
class Inscripcion(db.Model):
    __tablename__ = 'Inscripciones'

    ID = db.Column(db.Integer, primary_key=True)
    Equipo = db.Column(db.String(100), nullable=False)
    Colegio = db.Column(db.String(100), nullable=False)
    Deporte = db.Column(db.String(20), nullable=False)
    Categoria = db.Column(db.String(20), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)
    DNI = db.Column(db.Integer, nullable=False)
    Correo = db.Column(db.String(50), nullable=False)
    Miembros = db.Column(db.Integer, nullable=False)
    Acompañantes = db.Column(db.Integer, nullable=False)
    Vegetariano = db.Column(db.String(5), nullable=False)
    Celiaco = db.Column(db.String(5), nullable=False)
    Diabetico = db.Column(db.String(5), nullable=False)
    Libre = db.Column(db.Integer, nullable=False)
    Estado = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Inscripcion {self.Equipo} - {self.Deporte}>'

# Modelo de Partidos
class Partido(db.Model):
    __tablename__ = 'Partidos'

    ID = db.Column(db.Integer, primary_key=True)
    Equipo = db.Column(db.String(100), nullable=False)
    Deporte = db.Column(db.String(20), nullable=False)
    Grupo = db.Column(db.Integer, nullable=False)
    Empates = db.Column(db.Integer, nullable=False)
    Victorias = db.Column(db.Integer, nullable=False)
    Derrotas = db.Column(db.Integer, nullable=False)
    GF = db.Column(db.Integer, nullable=False)  # Goles a favor
    GC = db.Column(db.Integer, nullable=False)  # Goles en contra
    Puntos = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Partido {self.Equipo} - {self.Deporte}>'

# Modelo de Usuarios
class Usuario(db.Model):
    __tablename__ = 'Usuarios'

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=False)
    Gmail = db.Column(db.String(30), nullable=False)
    Contraseña = db.Column(db.String(255), nullable=False)
    ROL = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.Nombre}>'
