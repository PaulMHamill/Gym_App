from db.run_sql import run_sql
class Member:

    def __init__(self, name, age, address, id=None ):
        self.name = name
        self.age = age
        self.address = address
        self.id = id
        
    def save(member):
        sql = "INSERT INTO member ( name, age, address ) VALUES ( %s, %s, %s ) RETURNING id"
        values = [member.name, member.age, member.address]
        results = run_sql( sql, values )
        member.id = results[0]['id']
        return member