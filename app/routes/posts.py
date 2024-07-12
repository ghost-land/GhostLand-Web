from flask import Blueprint, render_template, redirect
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists

posts_bp = Blueprint('posts', __name__)



@posts_bp.route('/announcements')
@posts_bp.route('/announcements/')
def posts():
    return render_template(
        'news.jinja', lang='en',
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text
    )

@posts_bp.route('/<language>/announcements')
@posts_bp.route('/<language>/announcements/')
def index_lang(language):
    if not language_exists(language):
        return redirect('/posts')
        
    return render_template(
        'news.jinja', lang=language,
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text
    )


@posts_bp.route('/news')
@posts_bp.route('/news/')
@posts_bp.route('/posts')
@posts_bp.route('/posts/')
@posts_bp.route('/updates')
@posts_bp.route('/updates/')
def redirect_announcements():
    return redirect('/announcements')

@posts_bp.route('/<language>/news')
@posts_bp.route('/<language>/news/')
@posts_bp.route('/<language>/posts')
@posts_bp.route('/<language>/posts/')
@posts_bp.route('/<language>/updates')
@posts_bp.route('/<language>/updates/')
def redirect_announcements_lang(language):
    return redirect(f'/{language}/announcements')
