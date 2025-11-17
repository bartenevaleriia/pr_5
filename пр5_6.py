import math

def calculate_distance(x1, y1, x2, y2):
    """
    Рассчитывает расстояние между двумя точками.
    :param x1:
    x1(float): X первой точки.
    :param y1:
    y1(float): Y первой точки.
    :param x2:
    x2(float): X второй точки.
    :param y2:
    y2(float): Y второй точки.
    :return:
    (float): Расстояние между двумя точками.
    """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

x1, y1 = map(float, input("Введите координаты первой точки через пробел: ").split())
x2, y2 = map(float, input("Введите координаты второй точки через пробел: ").split())
a = calculate_distance(x1, y1, x2, y2)
print (f"Первая сторона (a) равна {a:.2f}")
x1, y1 = map(float, input("Введите координаты первой точки через пробел: ").split())
x2, y2 = map(float, input("Введите координаты второй точки через пробел: ").split())
b = calculate_distance(x1, y1, x2, y2)
print (f"Вторая сторона (b) равна {b:.2f}")
x1, y1 = map(float, input("Введите координаты первой точки через пробел: ").split())
x2, y2 = map(float, input("Введите координаты второй точки через пробел: ").split())
c = calculate_distance(x1, y1, x2, y2)
print (f"Вторая сторона (c) равна {c:.2f}")


def calculate_triangle_area(a,b,c):
    """
    Рассчитывает площадь треугольника.
    :param a: 
    a(float): Первая сторона.
    :param b: 
    b(float): Вторая сторона.
    :param c: 
    c(float): Третья сторона.
    :return:
    (float): Площадь треугольника. 
    """
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

square = calculate_triangle_area(a,b,c)
print(f"Площадь треугольника равна {square:.2f}")

