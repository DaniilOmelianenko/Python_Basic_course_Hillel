class Figure:
    def __init__(self, side_1):
        self.side_1 = side_1

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        self._validate_figure(side_1, side_2, side_3)
        super().__init__(side_1)
        self.side_2 = side_2
        self.side_3 = side_3

    def _validate_figure(self, side_1, side_2, side_3):
        # какая-то логика по валидации
        if side_1 <= 0:
            raise ValueError
        elif side_2 <= 0:
            raise ValueError
        elif side_3 <= 0:
            raise ValueError

    def perimeter(self):
        perim = side_1 + side_2 + side_3
        return perim

    def square(self):
        pass


figura_1 = Triangle(1, 2, 3)
print(figura_1.perimeter)
