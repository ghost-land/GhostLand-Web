from flask import Blueprint, render_template
from datetime import datetime
from run import settings
from app.utils.languages import text

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    return render_template(
        'index.jinja', lang='en',
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text
    )