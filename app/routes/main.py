from flask import Blueprint, flash, redirect, render_template, url_for, abort, jsonify, request
from flask_login import login_user, logout_user, current_user
from functools import wraps
from sqlalchemy import func

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import Usuario, Inscripcion, Settings, Cupos

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

@main.route('/', methods=['GET', 'POST'])
def general():
    if request.method == 'POST':
        try:
            # Procesar los cambios de cupos
            for i, value in enumerate(request.form.getlist('cupos_restantes[]')):
                deporte = request.form.getlist('deporte[]')[i]
                categoria = request.form.getlist('categoria[]')[i]

                # Actualizar la base de datos
                cupo = Cupos.query.filter_by(deporte=deporte, categoria=categoria).first()
                if cupo:
                    cupo.cupos_restantes = int(value)
            
            # Confirmar cambios en la base de datos
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(f"Error al procesar los datos: {str(e)}")

    # Consultar los datos para mostrarlos
    usuarios = Usuario.query.all()
    deportes = db.session.query(Cupos.deporte, Cupos.categoria, Cupos.cupos, Cupos.cupos_restantes).all()

    # Agrupar los datos por deporte
    deportes_dict = {}
    for deporte, categoria, cupos, cupos_restantes in deportes:
        if deporte not in deportes_dict:
            deportes_dict[deporte] = []
        deportes_dict[deporte].append({
            'categoria': categoria,
            'cupos': cupos,
            'cupos_restantes': cupos_restantes
        })

    return render_template('general.html', deportes_dict=deportes_dict, usuarios=usuarios)


@main.route('/guardar_cupos', methods=['POST'])
def guardar_cupos():
    try:
        # Obtener los datos enviados desde el cliente
        cupos_actualizados = request.get_json()
        print("Datos recibidos:", cupos_actualizados)

        # Procesar cada entrada y actualizar en la base de datos
        for deporte, categorias in cupos_actualizados.items():
            for categoria in categorias:
                # Buscar la entrada correspondiente en la base de datos
                cupo = Cupos.query.filter_by(
                    deporte=deporte, categoria=categoria['categoria']
                ).first()

                if cupo:
                    # Actualizar los campos necesarios
                    cupo.cupos = categoria['cupos']
                    cupo.cupos_restantes = categoria.get('cupos_restantes', cupo.cupos_restantes)
                    print(f"Actualizado: {cupo}")
                else:
                    print(f"No se encontró el registro para: Deporte={deporte}, Categoría={categoria['categoria']}")

        # Confirmar los cambios
        db.session.commit()

        # Obtener todos los registros para devolverlos como respuesta
        cupos_guardados = Cupos.query.all()
        resultado = [
            {
                "deporte": cupo.deporte,
                "categoria": cupo.categoria,
                "cupos": cupo.cupos,
                "cupos_restantes": cupo.cupos_restantes,
            }
            for cupo in cupos_guardados
        ]
        print(resultado)

        return jsonify({"mensaje": "Cambios guardados correctamente", "cupos": resultado}), 200

    except Exception as e:
        db.session.rollback()  # Revertir cambios en caso de error
        print("Error al guardar cupos:", e)
        return jsonify({"error": "Ocurrió un error al guardar los cupos"}), 500




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