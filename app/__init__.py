import os
import secrets
from flask import Flask

from .routes import home_bp, about_bp, posts_bp, misc_bp, APIs_bp

from run import settings


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.secret_key = settings.get('app-secret-key', secrets.token_hex(16))
    if app.secret_key == '93edb4c7329455e5aeff7e43f837e6be':  # default key
        app.secret_key = secrets.token_hex(16)
        
    if not settings.get('production', True):
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # oauth ssl if needed
    
    app.config['OAUTH2_PROVIDERS'] = {
        # GitHub OAuth 2.0 documentation:
        # https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
        'github': {
            'client_id': settings["github-oauth"]["public"],
            'client_secret': settings["github-oauth"]["secret"],
            'authorize_url': 'https://github.com/login/oauth/authorize',
            'token_url': 'https://github.com/login/oauth/access_token',
            'userinfo': {
                'url': 'https://api.github.com/user/emails',
                'email': lambda json: json[0]['email'],
            },
            'scopes': ['user:email'],
        },
    }
    
    app.jinja_env.add_extension('jinja2.ext.do')
    
    app.register_blueprint(APIs_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(misc_bp)
    
    return app