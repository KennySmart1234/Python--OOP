from shape import Shape


class Rectangle(Shape):

    def __init__(self, width:float, height:float, color:str="red", filled:bool="False"):
        super().__init__(color,filled)
        self.__width = width
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width:float):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height:float):
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def perimeter(self):
        return 2 * self.__width * self.__height


rectangle = Rectangle(5, 10)

print(rectangle.area)
print(rectangle.perimeter)
print(rectangle.color)
print(rectangle.filled)