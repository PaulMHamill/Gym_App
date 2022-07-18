from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("session", __name__)

@sessions_blueprint.route("/session")
def sessions():
    sessions = session_repository.select_all()
    return render_template("session/index.html", sessions = sessions)

@sessions_blueprint.route("/session/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.member(session)
    return render_template("session/show.html", session=session, members=members)

@sessions_blueprint.route("/session/new")
def new_session():
    sessions = session_repository.select_all()
    return render_template("session/new.html", sessions = sessions)

@sessions_blueprint.route("/session",  methods=['POST'])
def create_session():
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    session = Session(name, date, time)
    session_repository.save(session)
    return redirect('/session')

@sessions_blueprint.route('/session/<id>/update')
def edit(id):
    session = session_repository.select(id)
    return render_template('/session/edit.html', session = session)


# Route which the edit existing session page can POST its form data back to in order to save the changes
@sessions_blueprint.route('/session/<id>/update', methods=['POST'])
def update(id):
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    
    session = session_repository.select(id)
    session.name = name
    session.date = date
    session.time = time

    session_repository.update(session)

    return redirect('/session')


@sessions_blueprint.route("/session/<id>/delete", methods=['POST'])
def delete_member(id):
    session_repository.delete(id)
    return redirect('/session')

