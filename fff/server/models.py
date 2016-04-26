from fff.server import app, db, bcrypt


class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    home_score = db.Column(db.Integer, nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_score = db.Column(db.Integer, nullable=False)


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    # players = db.relationship('Player', backref='team', lazy='dynamic')


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    def __repr__(self):
        return '<Player {0}>'.format(self.name)

class Performance(db.Model):
    __tablename__ = "performances"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    minutes_played = db.Column(db.Integer, nullable=False)
    goals_scored = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    goals_conceded = db.Column(db.Integer, nullable=False)
    clean_sheet = db.Column(db.Boolean, nullable=False)
    bps = db.Column(db.Integer, nullable=True)
    bonus = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
