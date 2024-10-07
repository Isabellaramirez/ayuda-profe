from flask import Blueprint, render_template

conoceme_bp = Blueprint('conoceme_bp', __name__)

@conoceme_bp.route('/')
def conoceme():
    return render_template('conoceme.html')
