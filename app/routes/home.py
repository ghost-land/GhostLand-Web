from flask import Blueprint, request, abort, render_template
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists, get_languages_info

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
        text=text, get_languages_info=get_languages_info,
        open=open,
    )