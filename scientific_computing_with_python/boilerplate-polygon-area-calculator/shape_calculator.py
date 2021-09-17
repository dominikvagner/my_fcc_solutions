class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (self.width * 2 + self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical

class Square(Rectangle):
    def __init__(self, side):
        self.width = side 
        self.height = side

    def set_side(self, side):
        self.width = side 
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'
