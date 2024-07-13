from json import load
from flask import render_template
from datetime import datetime
from app.utils.languages import text, reload_all_lang_files

with open("settings.json", encoding="utf-8") as f:
    settings = load(f)

if __name__ == "__main__":
    from app import create_app
    
    app = create_app()
    
    if settings.get('debug', False):
        @app.before_request
        def reload_langs():
            reload_all_lang_files()
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        error_code, error_info = str(error).split(':')
        return render_template(
            'errorhandler.jinja', lang='en',
            year=datetime.now().year, error_code=error_code, error_info=error_info,
            text=text
        )
        
    app.run(
        host='0.0.0.0',
        debug=settings.get('debug', False),
        port=settings.get('port', 80)
    )