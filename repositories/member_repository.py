from db.run_sql import run_sql

from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO member ( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM member"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM member WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['id'] )
    return member


def session(member):
    sessions = []

    sql = "SELECT session.* FROM session INNER JOIN visits ON member.session_id = session.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['name'], row['date'], row['time'], row['id'])
        sessions.append(session)

    return sessions

def delete_all():
    sql = "DELETE FROM member"
    run_sql(sql)