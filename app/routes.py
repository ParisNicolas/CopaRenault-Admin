from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from flask_login import login_required, current_user
from app import db

#from app.models import Carrito, Producto, CarritoProducto, Transaccion
#from app.forms import TarjetaForm


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def general():
    return render_template('general.html')