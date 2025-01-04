class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides: int):
        self.__color = list(color)
        self.__sides = list(sides) if self.__is_valid_sides_for_init(*sides) else [1] * self.sides_count
        self.filled = False

    def __is_valid_sides_for_init(self, *sides):
        check = None
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                check = True
            else:
                check = False
        return check

    def __str__(self):
        return (f'У фигуры {self.__color} - цвет, {self.__sides} - сторон, {self.filled} - закрашенная,'
                f'{self.__len__()} - периметр')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.filled = False
        self.r = r
        self.g = g
        self.b = b
        if isinstance(self.r, int) and 0 <= self.r <= 255:
            if isinstance(self.g, int) and 0 <= self.g <= 255:
                if isinstance(self.b, int) and 0 <= self.b <= 255:
                    self.filled = True
        return self.filled

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = self.r
            self.__color[1] = self.g
            self.__color[2] = self.b
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        check = None
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == len(self.__sides):
                check =True
            else:
                check = False
        return check

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, __radius=0):
        super().__init__(color, *sides)
        self.__radius = __radius

    def get_square(self):
        self.__radius = self.get_radius()
        result_square = round(3.14159 * (self.__radius ** 2), 2)
        return result_square

    def get_radius(self):
        s = self.get_sides()
        self.__radius = s[0]/(2 * 3.14159)
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return s * (s - a) * (s - b) * (s - c) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides: int):
        if self.__is_valid_sides(*sides):
            side_len = sides[0]
        else:
            side_len = 1
        super().__init__(color, *((side_len,) * self.sides_count))

    def __is_valid_sides(self, *sides: int):
        if len(sides) != 1:
            return False
        else:
            return isinstance(sides[0], int) and sides[0] > 0

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(*new_sides):
            super().set_sides(*((new_sides[0],) * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
