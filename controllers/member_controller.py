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
    sessions = member_repository.session(member)
    return render_template("member/show.html", member=member, sessions=sessions)

@members_blueprint.route("/member/new")
def new_member():
    members = member_repository.select_all()
    return render_template("member/new.html", members = members)

@members_blueprint.route("/member",  methods=['POST'])
def create_member():
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    member = Member(name, age, address)
    member_repository.save(member)
    return redirect('/member')

@members_blueprint.route('/member/<id>/update')
def edit(id):
    member = member_repository.select(id)
    return render_template('/member/edit.html', member=member)

@members_blueprint.route('/member/<id>/update', methods=['POST'])
def update(id):
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    member = member_repository.select(id)
    member.name = name
    member.age = age
    member.address = address
    member_repository.update(member)

    return redirect('/member')

@members_blueprint.route('/member/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/member')
