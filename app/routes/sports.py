from flask import Blueprint, render_template, request
from app import db
from app.models import Equipo
from collections import defaultdict

sport_bp = Blueprint('sport_bp', __name__, template_folder='templates')

@sport_bp.route('/partidos', defaults={'deporte': None, 'categoria': None})
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

    return render_template('deportes/partidos.html', grupos=equipos_por_grupo)

    
    """datos = []
    for equipo in equipos:
        datos.append({"nombre":equipo.deporte, "grupo":registro.grupo_equipo, "pts":registro.puntos_equipo})
    return render_template('deportes/grupos.html', datos=datos)"""

