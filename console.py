import pdb
from models.session import Session
from models.member import Member
from models.booking import Booking

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member1 = Member('Paul Hamill')
member_repository.save(member1)

member2 = Member('Cheryl Stewart')
member_repository.save(member2)

member3 = Member('Tiger Woods')
member_repository.save(member3)

session1 = Session('Box fit', '01/08/2022', '9:00')
session_repository.save(session1)

session2 = Session('Kick Boxing', '01/08/2022', '11:00')
session_repository.save(session2)

booking1 = Booking(member1, session1)
booking_repository.save(booking1)

booking2 = Booking(member3, session1)
booking_repository.save(booking2)

booking3 = Booking(member1, session2)
booking_repository.save(booking3)

booking4 = Booking(member2, session2)
booking_repository.save(booking4)

pdb.set_trace()