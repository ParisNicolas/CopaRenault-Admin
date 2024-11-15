from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models import Inscripcion, Equipo

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

teams_bp = Blueprint('teams_bp', __name__, template_folder='templates')

@teams_bp.route('/inscripciones')
def inscripciones():
    inscripciones = Inscripcion.query.filter_by(Estado=False).all()
    equipos = Inscripcion.query.filter_by(Estado=True).all()

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
            Libre=0,  # Ajusta según tus necesidades
            Estado=True  # Ajusta según tus necesidades
        )
        db.session.add(nueva_inscripcion)
        db.session.commit()
        return redirect(url_for('teams_bp.inscripciones'))
    return render_template('add-team.html')

@teams_bp.route('/edit/<int:id>')
def get_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('edit-team.html', team=equipo)

@teams_bp.route('/update/<int:id>', methods=['POST'])
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
    equipo = inscripcion.equipo

    db.session.delete(inscripcion)
    if equipo:
        db.session.delete(equipo)
    
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))

@teams_bp.route('/cargar/<int:id>')
def cargar_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    equipo.estado = True
    db.session.commit()
    return redirect(url_for('teams_bp.inscripciones'))

@teams_bp.route('/get_info/<int:id>')
def get_team2(id):
    equipo = Inscripcion.query.get_or_404(id)
    return render_template('inscripciones/final-config.html', team=equipo)

@teams_bp.route('/config/<int:id>', methods=['POST'])
def config_team(id):
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
        equipo.Vegetariano = request.form['Vegetariano']
        equipo.Celiaco = request.form['Celiaco']
        equipo.Diabetico = request.form['Diabetico']
        
        db.session.commit()
        return redirect(url_for('teams_bp.inscripciones'))
    return render_template('final-config.html')

@teams_bp.route('/delete_copa/<int:id>', methods=['POST'])
def eliminar_team(id):
    equipo = Inscripcion.query.get_or_404(id)
    db.session.delete(equipo)
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
        inscripto.equipo_id = equipo.id
        db.session.add(equipo)
    db.session.commit()

    return redirect(url_for('teams_bp.inscripciones'))
