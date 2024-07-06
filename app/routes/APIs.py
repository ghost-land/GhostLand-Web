from flask import Blueprint, render_template
from run import settings

APIs_bp = Blueprint('APIs', __name__)


@APIs_bp.route('/apis')
@APIs_bp.route('/APIs')
def index():
    return render_template('APIs.html')