# manage.py


import os
import unittest
import coverage
from datetime import datetime

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from fff.server.models import *

COV = coverage.coverage(
    branch=True,
    include='fff/*',
    omit=[
        'fff/tests/*',
        'fff/server/config.py',
        'fff/server/*/__init__.py'
    ]
)
COV.start()

from fff.server import app, db


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('fff/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('fff/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_data():
    """Creates sample data."""
    wdfc = Team(name="wdfc")
    superstarz = Team(name="superstarz")
    db.session.add(wdfc)
    db.session.add(superstarz)
    db.session.commit()

    joe = Player(name="joe", team_id=wdfc.id)
    oj = Player(name="oj", team_id=wdfc.id)
    db.session.add(joe)
    db.session.add(oj)
    db.session.commit()

    match1 = Match(date=datetime(2005,2,14),
                   home_team_id=superstarz.id, home_score=24,
                   away_team_id=wdfc.id, away_score=4)
    db.session.add(match1)
    db.session.commit()

    joe1 = Performance(date=datetime(2005, 2, 14),
                       player_id=joe.id, match_id=match1.id,
                       minutes_played=40, goals_scored=1,
                       assists=1, goals_conceded=24,
                       clean_sheet=False,
                       bps=12, bonus=0,
                       points=-2, price=6.0)

    oj1 = Performance(date=datetime(2005, 2, 14),
                      player_id=joe.id, match_id=match1.id,
                      minutes_played=40, goals_scored=0,
                      assists=0, goals_conceded=24,
                      clean_sheet=False,
                      bps=12, bonus=0,
                      points=-10, price=6.0)

    db.session.add(joe1)
    db.session.add(oj1)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
