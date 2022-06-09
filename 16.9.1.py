# 16.9.1
class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return (f'Rectangle: {self.x}, {self.y}, {self.width}, {self.heigth}')

    def get_area(self):     # 16.9.2
        return (self.width * self.heigth)


rectangle_1 = Rectangle(5, 10, 50, 100)
print(rectangle_1)
print(rectangle_1.get_area())





