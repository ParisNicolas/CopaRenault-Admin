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

@teams_bp.route('/cargar/<int:id>')
def confirm_team(id):
    # Confirmar el equipo en la base de datos
    equipo = Inscripcion.query.get_or_404(id)
    print(f"Estado antes: {equipo.Estado}")
    equipo.Estado = True
    db.session.commit()
    print(f"Estado después: {equipo.Estado}")

    # # Llamar al Apps Script para crear el documento
    # try:
    #     script_url = 'https://docs.google.com/spreadsheets/d/1iC2vXoUpnRGCYjwohHsRJh7CBxR7YuNGtotHupB4ZMc/edit?usp=sharing'
    #     response = requests.get(script_url, params={'id': id})
        
    #     if response.status_code == 200:
    #         doc_url = response.json().get('doc_url')
    #         # Guardar la URL del documento en el campo QR
    #         equipo.QR = doc_url
    #         db.session.commit()
    #         flash("Equipo confirmado y documento creado exitosamente.", "success")
    #     else:
    #         flash("Error al crear el documento en Google Docs.", "error")
    # except Exception as e:
    #     flash(f"Error al llamar al Apps Script: {str(e)}", "error")

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