import os

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)


if 'APP_SETTINGS' in os.environ:
    app_settings = os.environ['APP_SETTINGS']
else:
    app_settings = 'fff.server.config.DevelopmentConfig'

app.config.from_object(app_settings)


####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


from fff.server.main.views import main_blueprint
app.register_blueprint(main_blueprint)

########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
