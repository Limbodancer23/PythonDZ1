# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
num = (input('Enter number: '))
if int(num) < 100 or int(num) > 999:
    print('Wrong number!!!')
else:
    print(f'Result = {int(num[0])+int(num[1])+int(num[2])}')