import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    def test_id_int(self):
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_incrementation(self):
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Betty"})
        self.assertEqual(b.id, {"id": 7, "name": "Betty"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)


if __name__ == '__main__':
    unittest.main()

