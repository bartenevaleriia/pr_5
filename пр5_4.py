import math
def calculate_rectangle_area(width, height):
    """
    Рассчитывает площадь прямоугольника по заданным сторонам.
    Запрашивает высоту и ширину.
    Выводит площадь.
    :param height:
    height(float): Высота прямоугольника.
    :param width:
    width(float): Ширина прямоугольника.
    :return:
    float: Площадь прямоугольника.
    """
    return width * height
def calculate_circle_area(radius):
    """
    Рассчитывает площадь круга по радиусу.
    Запрашивает радиус и выводит площадь.
    :param radius:
    radius(float): Радиус круга.
    :return:
    float: Площадь круга.
    """
    return radius ** 2 * math.pi
height, width = map(float, input("Введите стороны высоту и ширину прямоугольника через пробел: ").split())
square_rectangle = calculate_rectangle_area(width, height)
print(f"Площадь этого прямоугольника равна {square_rectangle:.2f}")
radius = float(input("Введите радиус круга: "))
circle_rectangle = calculate_circle_area(radius)
print(f"Площадь этого круга равна {circle_rectangle:.2f}")
