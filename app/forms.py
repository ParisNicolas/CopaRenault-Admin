from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo, Optional

from app.models import Usuario
from sqlalchemy import or_

class LoginForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    contraseña = PasswordField("Constraseña", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    nombre = StringField('Nombre de Usuario:', validators=[DataRequired(), Length(min=2, max=20)])
    gmail = StringField('Correo electronico:', validators=[DataRequired(), Length(min=5, max=40)])
    contraseña = PasswordField('Contraseña:', validators=[DataRequired(), Length(min=6)])
    confirmar_contraseña = PasswordField('Confirmar Contraseña:', validators=[DataRequired(), EqualTo('contraseña')])
    
    rol = SelectField('Rol', choices=[
        ('admin', 'Administrador'), 
        ('planillero', 'Planillero')
        ], validators=[DataRequired()])
    descripcion = TextAreaField('Descripción (opcional):', validators=[Optional(), Length(max=500)])

    submit = SubmitField('Registrar')

    # Validación personalizada para asegurar que el nombre de usuario es único
    def validate_username(self, nombre):
        user = Usuario.query.filter_by(nombre=nombre.data).first()
        if user:
            raise ValidationError('El nombre de usuario ya existe. Por favor elige uno diferente.')

    def validate_email(self, gmail):
        user = Usuario.query.filter_by(gmail=gmail.data).first()
        if user:
            raise ValidationError('El gmail ya esta registrado. Por favor elige uno diferente.')