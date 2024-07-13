from flask import Blueprint, abort, render_template
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    return render_template(
        'index.jinja', lang='en',
        settings=settings['site']['index'],
        emails=settings['site']['settings']['emails'],
        year=datetime.now().year,
        open=open,
        text=text
    )
    
@home_bp.route('/<language>')
@home_bp.route('/<language>/')
def index_lang(language):
    if not language_exists(language):
        abort(404)
        
    return render_template(
        'index.jinja', lang=language,
        settings=settings['site']['index'],
        emails=settings['site']['settings']['emails'],
        year=datetime.now().year,
        open=open,
        text=text
    )