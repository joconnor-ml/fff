# fff/server/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from bokeh.embed import components
from bokeh.plotting import figure

################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")


@main_blueprint.route("/graph/")
def graph():
    plot = figure()
    plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5],
                size=15, line_color="navy",
                fill_color="orange", fill_alpha=0.5)
    script, div = components(plot)
    return render_template('graph.html', script=script, div=div)
    
