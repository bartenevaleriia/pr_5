def calculate_imt():
    """
    Вычисляет ИМТ по заданному росту и весу.
    Args:
        weight(float): Вес человека.
        height(float): Рост человека.
    Returns:
         float: ИМТ по заданным параметрам.
    """
weight, height = map(float,input('Введите вес (в кг) и рост (в м) через пробел: ').split())
imt = weight/(height**2)
print(f'ИМТ = {imt:.1f}')

