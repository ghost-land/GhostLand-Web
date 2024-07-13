from flask import Blueprint, render_template, abort
import json
from run import settings

APIs_bp = Blueprint('APIs', __name__)


@APIs_bp.route('/api')
@APIs_bp.route('/API')
@APIs_bp.route('/api/')
@APIs_bp.route('/API/')
@APIs_bp.route('/apis')
@APIs_bp.route('/APIs')
@APIs_bp.route('/apis/')
@APIs_bp.route('/APIs/')
def index():
    return render_template('APIs.html')

@APIs_bp.route('/<api_file>')
@APIs_bp.route('/<api_file>/')
def api_file_route(api_file):
    if api_file.lower() in settings['api'].get('data-files', []):
        with open(f'data/{api_file.lower()}', 'r', encoding='utf-8') as f:
            return json.load(f)
    
    abort(404)