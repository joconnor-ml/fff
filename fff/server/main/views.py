from fff.server.models import Player, Performance, db

from flask import render_template, Blueprint
from bokeh.embed import components
from bokeh.plotting import figure

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")


@main_blueprint.route("/graph/")
def graph():
    # oj = db.session.query(Player).filter_by(name='oj').one()
    perfs = db.session.query(Performance).all()
    print(perfs)
    plot = figure()
    x = []
    y = []
    for perf in perfs:
        x.append(perf.goals_scored)
        y.append(perf.points)
    plot.circle(x, y,
                size=15, line_color="navy",
                fill_color="orange", fill_alpha=0.5)
    script, div = components(plot)
    return render_template('main/graph.html', script=script, div=div)
