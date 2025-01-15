import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
import os


from app.models import Inscripcion, Equipo
from app.forms import FilterForm
from sqlalchemy import or_

teams_bp = Blueprint('teams_bp', __name__, template_folder='templates')
APPSCRIPT_URL = os.getenv('APPSCRIPT_URL')

@teams_bp.route('/inscripciones', methods=['GET','POST'])
def inscripciones():
    form = FilterForm()

    query = Inscripcion.query
    if form.validate_on_submit():
        
        if form.deporte.data != 'all':
            query = query.filter(Inscripcion.Deporte==form.deporte.data)
        
        if form.categoria.data != 'all':
            query = query.filter(Inscripcion.Categoria==form.categoria.data)

        query = query.filter(
            or_(
                Inscripcion.Equipo.ilike(f"%{form.filtro.data}%"),
                Inscripcion.Colegio.ilike(f"%{form.filtro.data}%")
            ))
        
        inscripciones = query.filter_by(Estado=0).limit(form.cantidad.data).all()
        equipos = query.filter_by(Estado=1).limit(form.cantidad.data).all()
    else:
        inscripciones = query.filter_by(Estado=0).all()
        equipos = query.filter_by(Estado=1).all()

    return render_template('inscripciones/inscripciones.html',
        form=form,
        Table1_inf=inscripciones,
        Table2_inf=equipos
    )

#    return render_template('inscripciones/inscripciones.html', Table1_inf=inscripciones, Table2_inf = equipos)

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
    
    # Imprimir el ID y la URL del Apps Script
    print(f"ID recibido en Flask: {id}")
    print(f"Enviando solicitud a: {APPSCRIPT_URL}")
    # Enviar la solicitud al Apps Script sin esperar respuesta
    try:
        # Crear la URL completa
        full_url = f"{APPSCRIPT_URL}?id={id}"
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
    
    grupo = request.form.get('grupo')  # Obtener el valor del grupo
    
    if not grupo:  # Verificar si se seleccionó un grupo
        flash("Debe seleccionar un grupo", "danger")
        return redirect(url_for('teams_bp.inscripciones'))

    if inscripto.equipo_id:
        inscripto.Grupo = grupo  # Asignar el grupo al inscripto
        inscripto.equipo.grupo = grupo  # Asignar el grupo al equipo existente
    else:
        equipo = Equipo(
            nombre=inscripto.Equipo,
            colegio=inscripto.Colegio,
            deporte=inscripto.Deporte,
            categoria=inscripto.Categoria,
            grupo=grupo  # Asignar el grupo al nuevo equipo
        )
        db.session.add(equipo)
        db.session.commit()
        inscripto.equipo_id = equipo.id  # Asignar el ID del nuevo equipo al inscripto
        inscripto.Grupo = grupo  # Asignar el grupo al inscripto

    db.session.commit()
    flash("Grupo asignado exitosamente", "success")

    return redirect(url_for('teams_bp.inscripciones'))