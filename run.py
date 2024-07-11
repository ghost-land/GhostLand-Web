from json import load
from app.utils.languages import reload_all_lang_files

with open("settings.json", encoding="utf-8") as f:
    settings = load(f)

if __name__ == "__main__":
    from app import create_app
    
    app = create_app()
    
    if settings.get('debug', False):
        @app.before_request
        def reload_langs():
            reload_all_lang_files()
        
    app.run(
        host='0.0.0.0',
        debug=settings.get('debug', False),
        port=settings.get('port', 80)
    )