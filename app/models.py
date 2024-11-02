from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db

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
    Comprobante = db.Column(db.String(255), nullable=False, default='no se cargo', 
    info={'charset': 'utf8', 'collate': 'utf8_general_ci'})
    Autorizacion = db.Column(db.String(255), nullable=False, default='no se cargo', 
    info={'charset': 'utf8', 'collate': 'utf8_general_ci'})
    QR = db.Column(db.String(255), nullable=False, default='no se cargo', 
    info={'charset': 'utf8', 'collate': 'utf8_general_ci'})
    Grupo = db.Column(db.String(12), nullable=True, default='sin definir', 
    info={'charset': 'utf8', 'collate': 'utf8_general_ci'})
    Estado = db.Column(db.Boolean, nullable=False, default=False)  # MySQL tinyint(1) as Boolean

    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=True, unique=True)
    equipo = db.relationship('Equipo', back_populates='inscripcion')

    def __repr__(self):
        return f'<Inscripcion {self.Equipo} - {self.Deporte}>'




# Para fase de grupos
class Equipo(db.Model):
    __tablename__ = 'equipos'

    #Datos identificativos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    colegio = db.Column(db.String(100), nullable=False)
    #Datos de la division
    deporte = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    grupo = db.Column(db.String(1), nullable=False)
    #Puntaje
    victorias = db.Column(db.Integer, nullable=False, default=0)
    empates = db.Column(db.Integer, nullable=False, default=0)
    derrotas = db.Column(db.Integer, nullable=False, default=0)
    puntos = db.Column(db.Integer, nullable=False, default=0)

    #Relaciones (1-1 a inscripcion) y (1-N a partidos)
    inscripcion = db.relationship("Inscripcion", back_populates='equipo', uselist=False)
    #partidos = db.relationship('Partido')
    partidos = db.relationship('Partido', 
                                primaryjoin='or_(Equipo.id==Partido.equipo1_id, Equipo.id==Partido.equipo2_id)',
                                backref='equipo')

    #Optimizacion de consultas con filtrado
    __table_args__ = (
    db.Index('idx_deporte_categoria', 'deporte', 'categoria'),  # Filtrado por deporte y categoría
    )

    #Representacion en la consola
    def __repr__(self):
        return f'<Equipo {self.grupo} | {self.nombre}-{self.colegio} {self.deporte}-{self.categoria}>'


# Modelo de Partidos
class Partido(db.Model):
    __tablename__ = 'partidos'

    #Constantes para definir estados
    ESTADO_PENDIENTE = "Pendiente"
    ESTADO_FINALIZADO = "Finalizado"
    ESTADO_CANCELADO = "Cancelado"

    #Datos informativos
    id = db.Column(db.Integer, primary_key=True)
    deporte = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    horario = db.Column(db.DateTime, nullable=True)
    cancha = db.Column(db.Integer, nullable=False)

    #Datos del partido
    equipo1_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    equipo2_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    puntaje1 = db.Column(db.Integer, nullable=False, default=0)
    puntaje2 = db.Column(db.Integer, nullable=False, default=0)
    estado = db.Column(db.String(20), nullable=False, default=ESTADO_PENDIENTE)

    #Relaciones
    equipo1 = db.relationship('Equipo', foreign_keys=[equipo1_id])
    equipo2 = db.relationship('Equipo', foreign_keys=[equipo2_id])

    def __repr__(self):
        return f'<Partido {self.equipo1} vs {self.equipo2} - {self.puntaje1}:{self.puntaje2}>'
    

    
# Modelo de Usuarios
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    gmail = db.Column(db.String(30), nullable=False)

    rol = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def set_password(self, contraseña):
        self.contraseña = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'
    
    
class Settings(db.Model):
    __tablename__ = 'Settings'

    deporte = db.Column(db.String(20), primary_key=True)  # Clave primaria
    categoria = db.Column(db.String(20), nullable=False)
    cupos = db.Column(db.Integer, nullable=False)
    cierre = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Settings {self.deporte} - {self.categoria}>'
