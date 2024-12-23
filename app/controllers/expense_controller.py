from flask import Blueprint, render_template, request
from app.models.expense_model import Gasto
from datetime import datetime

expense_bp = Blueprint('Views', __name__)

@expense_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fecha_ini = datetime.strptime(request.form['fecha_ini'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        
        gastos = Gasto.get_gastos_by_date_range(fecha_ini, fecha_fin)
        totales = Gasto.get_totales_by_date_range(fecha_ini, fecha_fin)
        
        return render_template('Views/results.html', 
                             gastos=gastos,
                             totales=totales,
                             fecha_ini=fecha_ini,
                             fecha_fin=fecha_fin)
    
    return render_template('Views/index.html')
