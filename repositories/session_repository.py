from db.run_sql import run_sql

from models.member import Member
from models.session import Session

def save(session):
    sql = "INSERT INTO session(name, date, time, capacity) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [session.name, session.date, session.time, session.capacity]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session


def select_all():
    sessions = []

    sql = "SELECT * FROM session ORDER BY date"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['date'], row['time'], row['capacity'], row['id'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM session WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['date'], result['time'], result['capacity'], result['id'] )
    return session


def member(session):
    members = []

    sql = "SELECT member.* FROM member INNER JOIN booking ON booking.member_id = member.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['age'], row['address'], row['id'])
        members.append(member)

    return members

def update(session):
    sql = "UPDATE session SET (name, date, time, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.date, session.time, session.capacity, session.id]
    run_sql(sql, values)

def get_capacity(session):
    sql = "SELECT capacity FROM session WHERE id = %s"
    values = [session]
    results = run_sql(sql, values)
    return results 


def delete(id):
    sql = "DELETE FROM session WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM session"
    run_sql(sql)
