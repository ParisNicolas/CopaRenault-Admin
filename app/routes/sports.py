from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models import Inscripcion
from app.models import Partido

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm

sport_bp = Blueprint('sport_bp', __name__, template_folder='templates')


@sport_bp.route('/partidos')
def partidos():

    return render_template('deportes/grupos.html')

