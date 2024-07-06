from json import load

with open("settings.json", encoding="utf-8") as f:
    settings = load(f)

if __name__ == "__main__":
    from app import create_app
    
    app = create_app()
    app.run(
        host='0.0.0.0',
        debug=settings.get('debug', False),
        port=settings.get('port', 80)
    )