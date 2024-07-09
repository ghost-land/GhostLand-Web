from flask import Blueprint, render_template, redirect
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists

about_bp = Blueprint('about', __name__)


@about_bp.route('/about')
@about_bp.route('/about/')
def about():
    return render_template(
        'about.jinja', lang='en',
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text
    )

@about_bp.route('/<language>/about')
@about_bp.route('/<language>/about/')
def index_lang(language):
    if not language_exists(language):
        return redirect('/about')
        
    return render_template(
        'about.jinja', lang=language,
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text
    )
    
@about_bp.route('/about/')
def redirect_about():
    return redirect('/about')
