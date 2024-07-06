import os
import secrets
from flask import Flask

from .routes import home_bp, misc_bp, APIs_bp

from run import settings


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.secret_key = settings.get('app-secret-key', secrets.token_hex(16))    
    app.jinja_env.add_extension('jinja2.ext.do')
    
    if not settings.get('production', True):
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # oauth ssl if needed
    
    app.register_blueprint(home_bp)
    app.register_blueprint(misc_bp)
    app.register_blueprint(APIs_bp)
    
    return app