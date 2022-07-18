from db.run_sql import run_sql

from models.member import Member
from models.session import Session

def save(session):
    sql = "INSERT INTO session(name, date, time) VALUES ( %s, %s, %s ) RETURNING id"
    values = [session.name, session.date, session.time]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session


def select_all():
    sessions = []

    sql = "SELECT * FROM session"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['date'], row['time'], row['id'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM session WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['date'], result['time'], result['id'] )
    return session


def member(session):
    members = []

    sql = "SELECT member.* FROM member INNER JOIN booking ON booking.member_id = member.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)

    return members

def delete_all():
    sql = "DELETE FROM session"
    run_sql(sql)
