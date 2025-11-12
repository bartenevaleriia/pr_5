full_income = float(input('Введите годовой доход '))
nalog = 0.13
your_nalog = full_income*nalog
final_income = full_income-your_nalog
rub = 'руб.'
print(f'Общая сумма дохода: {full_income:.2f} {rub}')
print(f'Сумма рассчитанного налога: {your_nalog:.2f} {rub}')
print(f'Сумма на руки после вычета налога: {final_income:.2f} {rub}')
