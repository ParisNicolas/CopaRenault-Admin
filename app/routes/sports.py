from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models import Equipo, Inscripcion, Partido
from collections import defaultdict

sport_bp = Blueprint('sport_bp', __name__, template_folder='templates')

@sport_bp.route('/partidos', defaults={'deporte': 'Futbol', 'categoria': 'Masculino Mayor'})
@sport_bp.route('/partidos/<deporte>/<categoria>')
def partidos(deporte, categoria):
    # Filtrar equipos según el deporte y la categoría
    query = Equipo.query
    if deporte:
        query = query.filter_by(deporte=deporte)
    if categoria:
        query = query.filter_by(categoria=categoria)
    equipos = query.order_by(Equipo.grupo).all()

    # Agrupar equipos por grupo
    equipos_por_grupo = defaultdict(list)
    for equipo in equipos:
        equipos_por_grupo[equipo.grupo].append(equipo)


    partidos = Partido.query.filter_by(deporte=deporte, categoria=categoria).order_by(Partido.grupo, Partido.horario, Partido.cancha).all()

    partidos_por_grupo = defaultdict(list)
    for partido in partidos:
        grupo = partido.grupo
        partidos_por_grupo[grupo].append(partido)


    return render_template('deportes/partidos.html', grupos=equipos_por_grupo, partidos_grupo=partidos_por_grupo, deporte=deporte, categoria=categoria)

@sport_bp.route('/updates/<int:id>', methods=['POST'])
def update_match(id):
    partido  = Partido.query.get_or_404(id) 
    partido.puntaje1 = request.form['puntaje1']
    partido.puntaje2 = request.form['puntaje2']

    db.session.commit()
    return redirect(url_for('sport_bp.partidos'))



@sport_bp.route('/crear_partidos/<deporte>/<categoria>/<grupo>')
def crear_partidos(deporte, categoria, grupo):
    try:
        equipos = Equipo.query.filter_by(deporte=deporte, categoria=categoria, grupo=grupo).all()

        if len(equipos) < 2:
                return jsonify({'error': 'No hay suficientes equipos en este grupo para generar partidos.'}), 400
        

        db.session.query(Partido).filter(
            and_(
                Partido.deporte == deporte,
                Partido.categoria == categoria,
                Partido.grupo == grupo
                )).delete()
        db.session.commit()

        equipos_ids = [equipo.id for equipo in equipos]
        partidos_creados = []

        for i in range(len(equipos_ids)):
            for j in range(i + 1, len(equipos_ids)):
                partido = Partido(
                    deporte=deporte,
                    categoria=categoria,
                    grupo=grupo,
                    equipo1_id = equipos_ids[i],
                    equipo2_id=equipos_ids[j]
                )
                partidos_creados.append(partido)
        
        # Insertar los nuevos partidos en la base de datos
        db.session.add_all(partidos_creados)
        db.session.commit()

        return jsonify({'message': f'Se generaron {len(partidos_creados)} partidos para el grupo {grupo}.'}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': f'Error de base de datos: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500


    return jsonify("Todo OK")



def asignar_equipos_manually():
    inscripciones = Inscripcion.query.all()
    grupos = ['A', 'B', 'C', 'D']
    for i, incripto in enumerate(inscripciones):
        equipo = Equipo(
            nombre=incripto.Equipo, 
            colegio=incripto.Colegio,
            deporte=incripto.Deporte,
            categoria=incripto.Categoria,
            grupo=grupos[i//4]
            )
        incripto.equipo_id = equipo.id
        db.session.add(equipo)
    db.session.commit()