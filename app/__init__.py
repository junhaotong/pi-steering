from flask import Flask
from app.views import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)
