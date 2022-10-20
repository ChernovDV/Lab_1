list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# найти сумму, количество и среднее арифметическое уникальных чисел

summa = sum(set(list_))
amount = len(set(list_))
sr_arifm = round(summa/amount, 5)
print(summa)
print(amount)
print(sr_arifm)