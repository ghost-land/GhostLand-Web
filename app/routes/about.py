from flask import Blueprint, request, render_template, redirect
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists, get_languages_info

about_bp = Blueprint('about', __name__)

svgs = {
    'graduation-cap': open('static/images/graduation-cap.svg').read(),
    'security-shield': open('static/images/security-shield.svg').read(),
    'check': open('static/images/check.svg').read(),
    'user-group': open('static/images/user-group.svg').read(),
    'note': open('static/images/note.svg').read(),
}

@about_bp.route('/about')
@about_bp.route('/about/')
def about():
    language = request.args.get('lang', 'en')
    if not language_exists(language):
        language = 'en'
        
    return render_template(
        'about.jinja', lang=language,
        emails=settings['site']['settings']['emails'],
        year=datetime.now().year, svg=svgs,
        text=text, get_languages_info=get_languages_info,
    )

@about_bp.route('/contact')
@about_bp.route('/contact/')
def redirect_about():
    language = request.args.get('lang', 'en')
    if not language_exists(language):
        language = 'en'

    if language == 'en':
        return redirect('/about')
    else:
        return redirect(f'/about?lang={language}')