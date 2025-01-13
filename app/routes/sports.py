from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models import Equipo, Inscripcion, Partido
from collections import defaultdict

sport_bp = Blueprint('sport_bp', __name__, template_folder='templates')


##########################
#### FASE DE GRUPOS ######
##########################

#MOSTRAR EL RANKING DE LA FASE DE GRUPOS
@sport_bp.route('/partidos', defaults={'deporte': 'Futbol', 'categoria': 'Masculino Mayor'})
@sport_bp.route('/partidos/<deporte>/<categoria>')
def partidos(deporte, categoria):

    #GRUPOS
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


    #PARTIDOS
    #Filtrar partidos segun su deporte y categoria. Ordenarlos por grupo,horario,Ncancha
    partidos = Partido.query.filter_by(deporte=deporte, categoria=categoria).order_by(Partido.grupo, Partido.horario, Partido.cancha).all()

    #Agrupar partidos segun su grupo
    partidos_por_grupo = defaultdict(list)
    for partido in partidos:
        partidos_por_grupo[partido.grupo].append(partido)


    return render_template('deportes/partidos.html', grupos=equipos_por_grupo, partidos_grupo=partidos_por_grupo, deporte=deporte, categoria=categoria)

#ESTABLECER EL RESULTADO DE UN PARTIDO
@sport_bp.route('/updates/<int:id>', methods=['POST'])
def update_match(id):
    partido  = Partido.query.get_or_404(id) 
    partido.puntaje1 = request.form['puntaje1']
    partido.puntaje2 = request.form['puntaje2']

    db.session.commit()
    return redirect(url_for('sport_bp.partidos'))


#CREAR FIXTURE DE UN GRUPO EN UN DEPORTE/CATEGORIA
@sport_bp.route('/crear_partidos/<deporte>/<categoria>/<grupo>')
def crear_partidos(deporte, categoria, grupo):
    try:
        equipos = Equipo.query.filter_by(deporte=deporte, categoria=categoria, grupo=grupo).all()

        #Al menos 2 equipos
        if len(equipos) < 2:
                return jsonify({'error': 'No hay suficientes equipos en este grupo para generar partidos.'}), 400
        
        #Eliminar partidos ya creados
        db.session.query(Partido).filter(
            and_(
                Partido.deporte == deporte,
                Partido.categoria == categoria,
                Partido.grupo == grupo
                )).delete()
        db.session.commit()

        #CREAR LA ENTRUCIJADA DE PARTIDOS
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
        
        db.session.add_all(partidos_creados)
        db.session.commit()

        return jsonify({'message': f'Se generaron {len(partidos_creados)} partidos para el grupo {grupo}.'}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': f'Error de base de datos: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500



#FUNCION EXTERNA PARA ASIGNAR GRUPOS A TODOS LAS INCRIPCIONES Y GENERAR EQUIPOS
#NO ANDA, FALLO EN EQUIPOS DE 3
def asignar_equipos_manually():
    deporte = "Futbol"
    categoria = "Masculino Mayor"
    inscripciones = Inscripcion.query.filter_by(Estado=1, deporte=deporte, categoria=categoria).all()

    # Cantidad total de inscripciones
    total_inscripciones = len(inscripciones)

    # Cantidad de grupos totales y grupos de 3 para equilibrar
    cantGrupos = total_inscripciones // 4
    cantGrupos3 = 0

    # Determinar si se necesitan grupos de 3
    if total_inscripciones % 4 != 0:
        cantGrupos += 1
        cantGrupos3 = 4 - (total_inscripciones % 4)

    # Formar lista de grupos según orden ASCII
    grupos = [chr(65 + i) for i in range(cantGrupos)]  # Ejemplo: ['A', 'B', 'C', 'D']

    # Crear equipos y eliminar antiguos
    Equipo.query.filter_by(deporte=deporte, categoria=categoria).delete(synchronize_session=False)
    db.session.commit()

    # Asignar equipos a los grupos
    for i, inscrito in enumerate(inscripciones):
        # Determinar el grupo al que pertenece el inscrito
        grupo_index = i // 4
        if grupo_index >= cantGrupos - cantGrupos3:  # Si es un grupo de 3
            grupo = grupos[grupo_index]
        else:  # Grupos normales de 4
            grupo = grupos[grupo_index]

        # Crear el equipo
        equipo = Equipo(
            nombre=inscrito.Equipo,
            colegio=inscrito.Colegio,
            deporte=inscrito.Deporte,
            categoria=inscrito.Categoria,
            grupo=grupo
        )
        inscrito.equipo_id = equipo.id
        db.session.add(equipo)

    # Confirmar los cambios
    db.session.commit()
