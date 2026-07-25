from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color:str="green", filled = True):
        self.__color = color
        self.__filled = filled


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self, filled):
        self.__filled = filled


    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass