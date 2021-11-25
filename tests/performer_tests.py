import unittest
from src.performer import Performer

class TestPerformer(unittest.TestCase):

    def setUp(self):
        self.performer = Performer("Jimmy Crankey")

    def test_has_name(self):
        self.assertEqual("Jimmy Crankey", self.performer.name)