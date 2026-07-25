from shape import Shape


class Circle(Shape):
    def __init__(self, radius:float, color:str="yello", filled:bool="False"):

        super().__init__(color,filled)
        self.__radius = radius


    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


    @property
    def area(self):
        return self.__radius * self.__radius

    @area.setter
    def area(self, area):
        self.__radius = area

    @property
    def perimeter(self):
        return self.__radius * 2

    # @perimeter.setter
    # def perimeter(self, perimeter):
    #     self.__radius = perimeter



circle = Circle(10)

print(circle.filled)
print(circle.area)
print(circle.perimeter)
print(circle.color)


