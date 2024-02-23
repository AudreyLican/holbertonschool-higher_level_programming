#!/usr/bin/python3
from models.rectangle import Rectangle


"""Define a class Square from Rectangle class"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']
        if args:
            attrs_plus_value = zip(attributes, args)
            for attr_i, arg_j in attrs_plus_value:
                setattr(self, attr_i, arg_j)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y' : self.y
        }
