from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("booking", __name__)

@bookings_blueprint.route("/booking")
def bookings():
    booking = booking_repository.select_all()
    return render_template("booking/index.html", booking = booking)

@bookings_blueprint.route("/booking/new", methods=['GET'])
def new_task():
    member = member_repository.select_all()
    session = session_repository.select_all()
    return render_template("booking/new.html", member = member, session = session)

@bookings_blueprint.route("/booking",  methods=['POST'])
def create_task():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    booking = Booking(member, session)
    booking_repository.save(booking)
    return redirect('/booking')

@bookings_blueprint.route("/booking/<id>/delete", methods=['POST'])
def delete_task(id):
    booking_repository.delete(id)
    return redirect('/booking')