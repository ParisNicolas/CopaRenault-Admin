from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models import Inscripcion
from app.models import Partido
from app.models import Equipo
from collections import defaultdict

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

sport_bp = Blueprint('sport_bp', __name__, template_folder='templates')

@sport_bp.route('/partidos', defaults={'deporte': 'futbol', 'categoria': 'mayor'})
@sport_bp.route('/partidos/<deporte>/<categoria>')
def partidos(deporte, categoria):

    equipos = Equipo.query.filter_by(deporte=deporte, categoria=categoria).order_by(Equipo.grupo).all()

    #agrupar por grupo
    equipos_por_grupo = defaultdict(list)
    for equipo in equipos: 
        equipos_por_grupo[equipo.grupo].append(equipo)

    #acceder a los equipos por grupo
    for grupo, equipos in equipos_por_grupo.items():
        print(f'Grupo {grupo}:')
        for equipo in equipos:
            print(f'{equipo.nombre} - {equipo.colegio}')

    return render_template('deportes/partidos.html', grupos= equipos_por_grupo)
    """datos = []
    for equipo in equipos:
        datos.append({"nombre":equipo.deporte, "grupo":registro.grupo_equipo, "pts":registro.puntos_equipo})
    return render_template('deportes/grupos.html', datos=datos)"""

