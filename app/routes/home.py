from flask import Blueprint, request, abort, render_template
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    language = request.args.get('lang', 'en')
    if not language_exists(language):
        language = 'en'
    
    return render_template(
        'index.jinja', lang=language,
        settings=settings['site']['index'],
        emails=settings['site']['settings']['emails'],
        year=datetime.now().year,
        open=open,
        text=text
    )