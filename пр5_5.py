B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

money = int(input("Введите сумму, которая вносится в банкомат "))
c_B5000 = money // B5000
print ("Купюр по 5000: ", c_B5000)
money = money % B5000
c_B2000 = money // B2000
print ("Купюр по 2000: ", c_B2000)
money = money % B2000
c_B1000 = money // B1000
print ("Купюр по 1000: ", c_B1000)
money = money % B1000
c_B500 = money // B500
print ("Купюр по 500: ", c_B500)
money = money % B500
c_B200 = money // B200
print ("Купюр по 200: ", c_B200)
money = money % B200
c_B100 = money // B100
print ("Купюр по 100: ", c_B100)
money = money % B100
print ("Банкомат не может выдать: ", money)

"""
Рассчитывает количество купюр каждого номинала, которое будет выдано.
Использует жадный метод.
param(money):
money(int): Вносимая в банкомат сумма.
return:
(int): Количество купюр.
"""

