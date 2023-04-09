#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
s = int(input('Enter number: '))
KatyaNum = int((s/3)*2)
PetyaNum = int(KatyaNum/2/2)
SergeyNum = int(KatyaNum/2/2)
print(f'Katya made {KatyaNum} origami')
print(f'Petya made {PetyaNum} origami')
print(f'Sergey made {SergeyNum} origami')