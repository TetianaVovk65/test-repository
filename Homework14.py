class Shape:

    def __init__(self, *args, width: int, height: int, **kwargs):
        self.width = width
        self.height = height


class Triangle(Shape):
    def __init__(self, *args, width: int, **kwargs):
        super(Shape, self).__init__(*args, **kwargs)
        self.width = width

    def try_triangle(self):
        for triangle_rows in range(1, self.width + 1):
            for triangle_elements in range(1, self.width + 2 - triangle_rows):
                print("*", end=" ")
            print(" ")


class Rectangle(Shape):
    def __init__(self, *args, width: int, height: int, **kwargs):
        super(Shape, self).__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def try_rectangle(self):
        for i in range(1, self.height + 1):
            if i == 1 or i == self.height:
                print('*' * self.width)
            else:
                print('*' + " " * (self.width - 2) + '*')


width5 = Triangle(width=5)
width5.try_triangle()
rectangle = Rectangle(width=10, height=5)
rectangle.try_rectangle()
