import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app(os.environ.get("APP_SETTINGS", 'local'))

if __name__ == "__main__":
    app.run(
        debug=app.config.get('DEBUG', False),
        port=os.environ.get('PORT', 5000)
    )
