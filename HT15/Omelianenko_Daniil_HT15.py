class Figure:
    def __init__(self, side_a):
        self.side_a = side_a
        self._sides = [side_a]


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__validation_triangle(side_a, side_b, side_c)
        super().__init__(side_a)
        self.side_b = side_b
        self.side_c = side_c
        self._sides.append(self.side_b)
        self._sides.append(self.side_c)

    def __validation_triangle(self, side_a, side_b, side_c):
        if (side_a >= (side_b + side_c)) or (side_b >= (side_a + side_c)) or (side_c >= (side_a + side_b)):
            print("There is no triangle with such sides! Check sides of your triangle!")

    def show_sides(self):
        return self._sides

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def square(self):
        p = self.perimeter / 2
        return round(((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5), 5)


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(side_a)
        self.side_b = self.side_d = side_b
        self.side_c = side_a
        self._sides.append(self.side_b)
        self._sides.append(self.side_c)
        self._sides.append(self.side_d)

    def show_sides(self):
        return self._sides

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    @property
    def square(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side_a):
        super().__init__(side_a)
        self.side_b = self.side_c = self.side_d = side_a
        self._sides.append(self.side_b)
        self._sides.append(self.side_c)
        self._sides.append(self.side_d)

    def show_sides(self):
        return self._sides

    @property
    def perimeter(self):
        return self.side_a * 4

    @property
    def square(self):
        return self.side_a ** 2


# print('Triangle')
# # b = Triangle(23, 20, 15)
# # print(b.show_sides())
# # print(b.perimeter)
# # print(b.square)
#
# print('Rectangle')
# # rectangle = Rectangle(10, 5)
# # print(rectangle.show_sides())
# # print(rectangle.perimeter)
# # print(rectangle.square)

print('Square')
my_square = Square(7)
print(my_square.show_sides())
print(my_square.perimeter)
print(my_square.square)