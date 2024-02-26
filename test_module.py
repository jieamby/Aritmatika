import pytest
from shape_calculator import Rectangle, Square


def test_rectangle():
  rect = Rectangle(10, 5)
  assert rect.get_area() == 50
  assert rect.get_perimeter() == 30
  assert rect.get_diagonal() == 11.180339887498949
  assert rect.get_picture() == ("**********\n"
                                "**********\n"
                                "**********\n"
                                "**********\n"
                                "**********\n")
  rect.set_height(3)
  assert rect.get_perimeter() == 26
  assert str(rect) == "Rectangle(width=10, height=3)"


def test_square():
  sq = Square(9)
  assert sq.get_area() == 81
  assert sq.get_perimeter() == 36
  assert sq.get_diagonal() == 12.727922061357855
  assert sq.get_picture() == ("*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n"
                              "*********\n")
  sq.set_side(4)
  assert sq.get_perimeter() == 16
  assert str(sq) == "Square(side=4)"


if __name__ == "__main__":
  pytest.main()
