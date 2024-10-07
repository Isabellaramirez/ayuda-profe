from flask import Blueprint, render_template


rifa_bp = Blueprint('rifa_bp', __name__)



@rifa_bp.route('/')
def rifa():
    return render_template('rifa.html')
