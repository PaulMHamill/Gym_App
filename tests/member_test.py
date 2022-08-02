import unittest
from models.member import Member
from repositories.member_repository import *
from db.run_sql import run_sql

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("John", 30, "Edinburgh")
        
        
    def test_member_has_name(self):
        self.assertEqual("John", self.member.name)
        
    def test_member_has_age(self):
        self.assertEqual(30, self.member.age)

    def test_member_has_address(self):
        self.assertEqual("Edinburgh", self.member.address)

