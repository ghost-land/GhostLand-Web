from flask import Blueprint, render_template, redirect
from datetime import datetime
from run import settings

about_bp = Blueprint('about', __name__)


@about_bp.route('/about')
def about():
    return render_template(
        'about.jinja',
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open
    )

@about_bp.route('/about/')
def redirect_about():
    return redirect('/about')
