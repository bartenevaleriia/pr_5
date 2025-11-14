def convert_usd_to_rub(amount_usd):
    """
    Конвертирует долларовую сумму в рубли по текущему курсу.
    Запрашивает сумму в долларах и выводит в рублях.
    :param amount_usd: 
    amount_usd(float): Сумма в долларах.
    :return: 
    float: Сумма в рублях.
    """
    exchange_usd_course = 95.50
    return amount_usd * exchange_usd_course
print("Курс доллара = 95.50 рублей")
dollars = float(input("Введите сумму в долларах "))
if dollars >= 0:
    rubles = convert_usd_to_rub(dollars)
    print(f"Данная сумма в долларах равна {rubles:.2f} в рублях")
else:
    print("Сумма не может быть отрицательной")