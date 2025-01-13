import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models import Inscripcion, Equipo

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

teams_bp = Blueprint('teams_bp', __name__, template_folder='templates')

@teams_bp.route('/inscripciones')
def inscripciones():
    inscripciones = Inscripcion.query.filter_by(Estado=0).all()
    equipos = Inscripcion.query.filter_by(Estado=1).all()

    return render_template('inscripciones/inscripciones.html', Table1_inf=inscripciones, Table2_inf = equipos)

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
        )
        db.session.add(nueva_inscripcion)
        db.session.commit()
        return redirect(url_for('teams_bp.inscripciones'))
    return render_template('inscripciones/add_team.html')


# cargar al equipo en la copa
@teams_bp.route('/cargar/<int:id>')
def cargar_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    equipo.Estado = True
    db.session.commit()
    
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




@teams_bp.route('/edit_form/<int:id>')
def edit_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('inscripciones/edit_form.html', team=equipo)

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

@teams_bp.route('/delete/<int:id>')
def delete_team(id):
    inscripcion	 = Inscripcion.query.get_or_404(id)
    db.session.delete(inscripcion)
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))









@teams_bp.route('/asignar_grupo/<int:id>', methods=['POST'])
def asignar_grupo(id):
    inscripto = Inscripcion.query.get_or_404(id)
    
    if inscripto.equipo_id:
        inscripto.equipo.grupo = request.form['grupo']
    else:
        equipo = Equipo(
            nombre=inscripto.Equipo,
            colegio=inscripto.Colegio,
            deporte=inscripto.Deporte,
            categoria=inscripto.Categoria,
            grupo=request.form['grupo']
        )
        db.session.add(equipo)
        db.session.commit()
        inscripto.equipo_id = equipo.id
    db.session.commit()

    return redirect(url_for('teams_bp.inscripciones'))
