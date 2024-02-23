#!/usr/bin/python3
from models.base import Base


"""Define a child class from Base"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self, value):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not (int):
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not (int):
            raise TypeError("x must be a integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not (int):
            raise TypeError("y must be a integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the characters '#', by taking care of x and y"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height))

    def update(self, *args, **kwargs):
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            attrs_plus_value = zip(attributes, args)
            for attr_i, arg_j in attrs_plus_value:
                setattr(self, attr_i, arg_j)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionnary, representation of the rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
