class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    date = db.Column(db.Date)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
