import unittest
from models.member import Member
from models.session import Session

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("John", 10, "Edinburgh")
        
        
    def test_member_has_name(self):
        self.assertEqual("John", self.member.name)
        
    def test_member_has_age(self):
        self.assertEqual(10, self.member.age)

    def test_member_has_address(self):
        self.assertEqual("Edinburgh", self.member.address)