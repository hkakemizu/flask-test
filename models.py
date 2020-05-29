from app import db
import time


class TimeRecord(db.Model):

    __tablename__ = "timerecord"

    count = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Text, nullable=False)
    time = db.Column(db.Float, nullable=False)

    def __init__(self, id, type, time):
        self.id = id
        self.type = type
        self.time = time

    def __repr__(self):
        return "<TimeRecord(id={}, type={}, time={})>".format(self.id, self.type, self.time)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "time": self.time,
        }


def add_timerecord(id, type, t=None):
    if t is None:
        t = time.time()
    timerecord = TimeRecord(id, type, t)
    db.session.add(timerecord)
    db.session.commit()
    return timerecord


if __name__ == "__main__":
    db.create_all()
