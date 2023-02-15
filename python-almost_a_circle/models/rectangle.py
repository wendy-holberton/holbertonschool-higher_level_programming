#!/usr/bin/python3
"""Import class Basee"""
from models.base import Base


class Rectangle(Base):
    """Initialize the data"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def validate_positive(self, value, name):
        """
        Function validate_positive pass the parameters value and name
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    """
    Function validate_positive_or_zero pass the parameters value and name
    """
    def validate_positive_or_zero(self, value, name):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @width.setter
    def width(self, value):
        self.validate_positive(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate_positive(value, "height")
        self.__height = value

    @x.setter
    def x(self, value):
        self.validate_positive_or_zero(value, "x")
        self.__x = value

    @y.setter
    def y(self, value):
        self.validate_positive_or_zero(value, "y")
        self.__y = value
