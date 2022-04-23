import os

from app.main import create_app
from app.main.routes import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
