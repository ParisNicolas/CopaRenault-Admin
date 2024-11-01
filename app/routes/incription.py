import requests
#pip install requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models import Inscripcion

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

teams_bp = Blueprint('teams_bp', __name__, template_folder='templates')

@teams_bp.route('/inscripciones')
def inscripciones():
    inscripciones = Inscripcion.query.filter_by(Estado=False).all()
    equipos = Inscripcion.query.filter_by(Estado=True).all()

    return render_template('inscripciones/inscripciones.html', Table1_inf=inscripciones, Table2_inf = equipos)

#Cargar equipo manualmente a tabla1
@teams_bp.route('/add_team', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        # Crear una nueva inscripción
        nueva_inscripcion = Inscripcion(
            Equipo=request.form['Equipo'],
            Colegio=request.form['Colegio'],
            Deporte=request.form['Deporte'],
            Categoria=request.form['Categoria'],
            Telefono=request.form['Telefono'],
            DNI=request.form['DNI'],
            Correo=request.form['Correo'],
            Miembros=request.form['Miembros'],
            Acompañantes=request.form['Acompañantes'],
            Vegetariano=request.form['Vegetariano'],
            Celiaco=request.form['Celiaco'],
            Diabetico=request.form['Diabetico'],
            Estado=False  # Ajusta según tus necesidades
        )
        db.session.add(nueva_inscripcion)
        db.session.commit()
        return redirect(url_for('teams_bp.inscripciones'))
    return render_template('inscripciones/add-team.html')


#Editar equipo de tabla1
@teams_bp.route('/edit/<int:id>')
def get_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('inscripciones/edit-team.html', team=equipo)

@teams_bp.route('/update_team/<int:id>', methods=['POST'])
def update_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    equipo.Equipo = request.form['Equipo']
    equipo.Colegio = request.form['Colegio']
    equipo.Deporte = request.form['Deporte']
    equipo.Categoria = request.form['Categoria']
    equipo.Telefono = request.form['Telefono']
    equipo.DNI = request.form['DNI']
    equipo.Correo = request.form['Correo']
    equipo.Miembros = request.form['Miembros']
    equipo.Acompañantes = request.form['Acompañantes']
    equipo.Vegetariano = request.form['Vegetariano']
    equipo.Celiaco = request.form['Celiaco']
    equipo.Diabetico = request.form['Diabetico']
    
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))




@teams_bp.route('/cargar/<int:id>', methods=['GET'])
def confirm_team(id):
    
    equipo = Inscripcion.query.get_or_404(id)
    equipo.Estado = True  # Descomentar si deseas cambiar el estado
    db.session.commit()  # Confirmar cambios en la base de datos
    
    
    # URL del Apps Script (asegúrate de que esta sea la correcta)
    script_url = 'https://script.google.com/macros/s/AKfycbyQIB2RlS3YG9OrV43UOCcFf_0Hi8juvrsWbjyaLhf6z6OcJ3JfopZPBFI9JlHrde3FpQ/exec'

    # Imprimir el ID y la URL del Apps Script
    print(f"ID recibido en Flask: {id}")
    print(f"Enviando solicitud a: {script_url}")

    # Enviar la solicitud al Apps Script sin esperar respuesta
    try:
        # Crear la URL completa
        full_url = f"{script_url}?id={id}"
        response = requests.get(full_url)  # Usar GET para pruebas simples

        # Verificar la respuesta del Apps Script
        if response.status_code == 200:
            flash("Orden enviada exitosamente al Apps Script.", "success")
        else:
            flash(f"Error en Apps Script: {response.status_code}", "error")
    except requests.exceptions.RequestException as e:
        flash(f"Error al llamar al Apps Script: {str(e)}", "error")

    return redirect(url_for('teams_bp.inscripciones'))








#Editar equipo de tabla2
@teams_bp.route('/edit2/<int:id>')
def get_team2(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('inscripciones/final-config.html', team=equipo)

@teams_bp.route('/update_team2/<int:id>', methods=['POST'])
def update_team2(id):
    if request.method == 'POST':
        equipo = Inscripcion.query.get_or_404(id)
        equipo.Equipo = request.form['Equipo']
        equipo.Colegio = request.form['Colegio']
        equipo.Deporte = request.form['Deporte']
        equipo.Categoria = request.form['Categoria']
        equipo.Telefono = request.form['Telefono']
        equipo.DNI = request.form['DNI']
        equipo.Correo = request.form['Correo']
        equipo.Miembros = request.form['Miembros']
        equipo.Acompañantes = request.form['Acompañantes']
        equipo.Grupo = request.form['Grupo']
        equipo.Vegetariano = request.form['Vegetariano']
        equipo.Celiaco = request.form['Celiaco']
        equipo.Diabetico = request.form['Diabetico']
        
        db.session.commit()
        return redirect(url_for('teams_bp.inscripciones'))
    return render_template('inscripciones/final-config.html')


@teams_bp.route('/delete/<int:id>')
def delete_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))