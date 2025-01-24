from flask import Blueprint, flash, redirect, render_template, url_for, abort, jsonify
from flask_login import login_user, logout_user, current_user
from functools import wraps
from sqlalchemy import func

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import Usuario, Inscripcion

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

main = Blueprint('main', __name__, template_folder='templates')

#DECORADOR
def role_required(allowed_rol):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated and (current_user.rol == 'admin' or current_user.rol == allowed_rol):
                return f(*args, **kwargs)
            else:
                abort(403)  # Prohibido: el usuario no tiene permiso
        return decorated_function
    return decorator


@main.route('/')
def general():


    return render_template(
        'general.html'
    )

@main.route('/data/ingresos')
def obtener_ingresos():
    # Datos de ejemplo (pueden provenir de una base de datos o cálculo)
    ingresos = {
        "meses": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "valores": [12000, 15000, 17000, 13000, 18000]
    }
    return jsonify(ingresos)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nombre=form.nombre.data).first()
        if usuario and usuario.check_password(form.contraseña.data):  # Comprueba la contraseña
            login_user(usuario)
            flash('Inicio de sesión exitoso', 'success')
            # Si el usuario es "owner", activa la animación
            if usuario.nombre == "owner":  # Cambia esto según tu lógica de identificación de "owner"
                return render_template('login.html', form=form, animate=True)
            return redirect(url_for('main.general'))  # Redirige normalmente si no es "owner"
        else:
            flash('Inicio de sesión fallido. Verifica tu nombre de usuario y contraseña.', 'danger')
    return render_template('login.html', form=form, animate=False)


#Registro
@main.route('/register', methods=['GET', 'POST'])
@role_required('admin')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(
            nombre=form.nombre.data,
            gmail=form.gmail.data,
            rol=form.rol.data,
            descripcion=form.descripcion.data
        )
        nuevo_usuario.set_password(form.contraseña.data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Tu cuenta ha sido creada con éxito. ¡Ahora puedes iniciar sesión!', 'success')
        return redirect(url_for('main.register'))  # Redirige al login después del registro
    return render_template('register.html', form=form)

#Registro
@main.route('/logout')
def logout():
    logout_user()
    flash("Has cerrado session.", "success")
    return redirect(url_for("main.general"))