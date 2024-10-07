from flask import Blueprint, render_template

donar_bp = Blueprint('donar_bp', __name__)

@donar_bp.route('/')
def donar():
    return render_template('donar.html')
