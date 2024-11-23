import unittest
from models import PersonCRUD
from models import Person

class TestPersonCRUD(unittest.TestCase):
    def setUp(self):
        self.crud=PersonCRUD()
        self.person1=Person("Luis", "Chaparro", "24", "1234")
        self.person2=Person("Sebastian", "Agredo", "23", "12345")

    def test_create(self):
        self.crud.create(self.person1)

        self.assertEqual(len(self.crud.persons), 1)
        self.assertEqual(self.crud.persons[0].name,"Luis")

    def test_person_duplicate_dni(self):
        self.crud.create(self.person1)
        with self.assertRaises(ValueError):
            self.crud.create(self.person1)

    def test_read(self):
        self.crud.create(self.person1)
        person =self.crud.read("1234")

if __name__ == "__main__":
    unittest.main()