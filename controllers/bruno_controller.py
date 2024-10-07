from flask import Blueprint, render_template

bruno_bp = Blueprint('bruno_bp', __name__)

@bruno_bp.route('/bruno')
def bruno():
    return render_template('principal_bruno.html')