weight, height = map(float,input('Введите вес (в кг) и рост (в м) через пробел: ').split())
imt = weight/(height**2)
print(f'ИМТ = {imt:.1f}')
