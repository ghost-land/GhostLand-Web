from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_dance.contrib.github import make_github_blueprint, github
from datetime import datetime
from run import settings
from app.utils.languages import text, language_exists, get_languages_info

posts_bp = Blueprint('posts', __name__)

# Set up GitHub OAuth
github_blueprint = make_github_blueprint(
    client_id=settings["github-oauth"]["public"],
    client_secret=settings["github-oauth"]["secret"],
    scope="read:org",
    redirect_to="posts.github_authorized"  # Specify the callback URL explicitly
)

# Register the GitHub blueprint on the actual Blueprint
posts_bp.register_blueprint(github_blueprint, url_prefix="/github_login")


@posts_bp.route('/announcements')
@posts_bp.route('/announcements/')
def posts():
    language = request.args.get('lang', 'en')
    if not language_exists(language):
        language = 'en'
        
    return render_template(
        'news.jinja', lang=language,
        settings=settings['site']['index'],
        year=datetime.now().year,
        open=open,
        text=text, get_languages_info=get_languages_info,
    )


@posts_bp.route('/news')
@posts_bp.route('/news/')
@posts_bp.route('/posts')
@posts_bp.route('/posts/')
@posts_bp.route('/updates')
@posts_bp.route('/updates/')
def redirect_announcements():
    language = request.args.get('lang', 'en')
    if not language_exists(language):
        language = 'en'

    if language == 'en':
        return redirect('/announcements')
    else:
        return redirect(f'/announcements?lang={language}')
        


# Admin side

@posts_bp.route('/posts/write')
@posts_bp.route('/posts/write/')
def write_post():
    github_data = None
    if not github.authorized:
        if settings.get('debug', False):
            return redirect('/login')
        return redirect('/announcements')

    github_data = github.get('/user').json()
    org = github.get('/orgs/ghost-land/members').json()
    print(github_data)

    user_authorized = any(github_data['id'] == user['id'] for user in org)
    if not user_authorized:
        return redirect('/announcements')
    
    return render_template(
        'write_post.jinja', lang='en',
        github=github_data, orgs=org,
        year=datetime.now().year,
        text=text, get_languages_info=get_languages_info,
    )
    

@posts_bp.route('/login')
@posts_bp.route('/login/')
def github_login():
    return redirect(url_for('posts.github.login'))

@posts_bp.route('/github/authorized')
def github_authorized():
    if not github.authorized:
        print('not authorized')
        return redirect(url_for('github.login'))  # Redirect to the login URL if not authorized
    else:
        print('authorized')
        return redirect('/posts/write')  # Redirect to the page maker page

@posts_bp.route('/logout')
@posts_bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('posts.redirect_announcements'))