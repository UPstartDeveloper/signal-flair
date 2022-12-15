from flask import Flask

app = Flask(__name__, instance_relative_config=True, template_folder="views")
app.config["SECRET_KEY"] = "secret"

con = None

# ensure all the route handlers are in scope
with app.app_context():
    from .routes import *
