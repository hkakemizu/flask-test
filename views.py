from flask import jsonify, request
from models import TimeRecord, add_timerecord
from app import app, db
import time


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/timerecord/<id>", methods=["GET"])
def get_timerecord(id=None):
    if id is None:
        return jsonify({})
    records = db.session.query(TimeRecord).filter_by(id=id).all()
    return jsonify(records=[e.serialize() for e in records])


@app.route("/timerecord/<id>", methods=["POST"])
def post_timerecord(id=None):
    if id is None:
        return jsonify({})  # FIXME: return "not found"
    type = request.form["type"]
    add_timerecord(id, type)
    return jsonify({})  # FIXME: return "success"
