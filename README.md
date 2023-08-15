# Films catalog
Back-end for films catalog like kinopoisk
***
## Features
- Authorization/Authentication users by jwt
- Add movies to bookmarks
- Films, directors, genres

***
## Technology stack
- Python 3.10.6
- Flask 2.0.2
- flask-restx 0.5.1
- Flask-SQLAlchemy 2.5.1
- Jinja2 3.0.2
- marshmallow 3.14.0
- PyJWT 2.6.0

***
## Start app
1. Clone project
   ```
   https://github.com/RusinVladislav/Films_catalog_API
2. Create virtual environment
   ```
    python3 -m venv venv
3. Activate virtual environment
   ```
    source venv/bin/activate
4. Install requirements
   ```
    pip install -r requirements.txt
5. Run flask application
   ```
    export FLASK_APP=run.py
    flask run
***
***
## Project structure
- `dao/`: models and work with database
- `service/`: bissness logics
- `tests/`: tests
- `views/`: views
