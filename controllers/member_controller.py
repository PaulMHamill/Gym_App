from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("member", __name__)

@members_blueprint.route("/member")
def members():
    members = member_repository.select_all()
    return render_template("member/index.html", members = members)

@members_blueprint.route("/member/<id>")
def show(id):
    member = member_repository.select(id)
    session = member_repository.session(member)
    return render_template("member/show.html", member=member, session=session)
