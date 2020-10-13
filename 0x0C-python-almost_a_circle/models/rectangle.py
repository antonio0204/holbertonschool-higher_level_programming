#!/usr/bin/python3
"""Class rectangle crate class eitn inherefemcia"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
