import unittest
from models.square import Square
from models.base import Base


class TestSquaree(unittest.TestCase):

    def test_idf(self):
        r = Square(2)
        self.assertEqual(r.id, Base.get_nb_objects())
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.area(), 4)

    def test_not_negative(self):
        with self.assertRaises(Exception) as context:
            Square(-1)
            
    def test_zero(self):
        with self.assertRaises(Exception) as context:
            Square(0)

    def test_x_negative(self):
        with self.assertRaises(Exception) as context:
            Square(3, x=-1)

    def test_y_negative(self):
        with self.assertRaises(Exception) as context:
            Square(4, y=-1)

    def test_width_string(self):
        with self.assertRaises(Exception) as context:
            Square("1")

    def test_height_string(self):
        with self.assertRaises(Exception) as context:
            Square(4, "2")

    def test_x_string(self):
        with self.assertRaises(Exception) as context:
            Square(4, 4, x="3")

    def test_no_string(self):
        with self.assertRaises(Exception) as context:
            Square(4, 4, x=3, y=2)



if __name__ == "__main__":
    unittest.main()
