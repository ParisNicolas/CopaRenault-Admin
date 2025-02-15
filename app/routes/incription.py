import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from app import db
import os


from app.models import Inscripcion, Equipo, Cupos
from app.forms import FilterForm
from sqlalchemy import or_

teams_bp = Blueprint('teams_bp', __name__, template_folder='templates')
APPSCRIPT_URL1 = os.getenv('APPSCRIPT_URL1')


@teams_bp.route('/inscripciones', methods=['GET','POST'])
def inscripciones():
    form = FilterForm()

    query = Inscripcion.query
    if form.validate_on_submit():
        
        if form.deporte.data != 'all':
            query = query.filter(Inscripcion.Deporte==form.deporte.data)
        
        if form.categoria.data != 'all':
            query = query.filter(Inscripcion.Categoria==form.categoria.data)
            
        if form.grupo.data != 'all':
            query = query.filter(Inscripcion.Grupo==form.grupo.data)

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

#agrega un equipo a la base de datos de manera manual (uso exclusivo para pruebas no se recomienda su uso)
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




# confirmar la inscripcion de un equipo al evento
@teams_bp.route('/cargar/<int:id>/<string:deporte>/<string:categoria>')
def cargar_team(id, deporte, categoria):
    # Buscar el equipo en la tabla Inscripcion
    equipo = Inscripcion.query.get_or_404(id)
    equipo.Estado = True  # Actualizar estado del equipo

    # Buscar el cupo correspondiente y actualizarlo
    cupo = Cupos.query.filter_by(deporte=deporte, categoria=categoria).first()
    if cupo:
        if cupo.cupos_tomados < cupo.cupos_totales:  # Verificar que aún haya cupos disponibles
            cupo.cupos_tomados += 1
        else:
            flash("No hay cupos disponibles para esta categoría y deporte.", "error")
            return redirect(url_for('teams_bp.inscripciones'))

    db.session.commit()  # Guardar cambios en ambas tablas
    
    # Imprimir el ID y la URL del Apps Script
    print(f"ID recibido en Flask: {id}")
    print(f"Enviando solicitud a: {APPSCRIPT_URL1}")
    
    # Enviar la solicitud al Apps Script sin esperar respuesta
    try:
        # Crear la URL completa
        full_url = f"{APPSCRIPT_URL1}?id={id}"
        response = requests.get(full_url)  # Usar GET para pruebas simples
        if response.status_code == 200:
            flash("Orden enviada exitosamente al Apps Script.", "success")
        else:
            flash(f"Error en Apps Script: {response.status_code}", "error")
    except requests.exceptions.RequestException as e:
        flash(f"Error al llamar al Apps Script: {str(e)}", "error")

    return redirect(url_for('teams_bp.inscripciones'))




#abre fromulario de edicion
@teams_bp.route('/edit_form/<int:id>')
def edit_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('inscripciones/edit_form.html', team=equipo)

#actualiza los datos del equipo en la base de datos tras completar el formulario
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

#borra un equipo de la base de datos
@teams_bp.route('/delete/<int:id>')
def delete_team(id):
    inscripcion	 = Inscripcion.query.get_or_404(id)
    db.session.delete(inscripcion)
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))

#asigna un grupo a un equipo
@teams_bp.route('/asignar_grupo/<int:id>', methods=['POST'])
def asignar_grupo(id):
    inscripto = Inscripcion.query.get_or_404(id)
    grupo = request.form.get('grupo')

    if not grupo:
        return jsonify({"success": False, "message": "Debe seleccionar un grupo"}), 400

    if inscripto.equipo_id:
        inscripto.Grupo = grupo
        inscripto.equipo.grupo = grupo
    else:
        equipo = Equipo(
            nombre=inscripto.Equipo,
            colegio=inscripto.Colegio,
            deporte=inscripto.Deporte,
            categoria=inscripto.Categoria,
            grupo=grupo
        )
        db.session.add(equipo)
        db.session.commit()
        inscripto.equipo_id = equipo.id
        inscripto.Grupo = grupo

    db.session.commit()
    
    return jsonify({"success": True, "message": "Grupo asignado correctamente"})


@teams_bp.route('/ver_equipo/<id>', methods=['GET'])
def mostrar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    return render_template('inscripciones/ver_equipo.html', equipo=equipo)