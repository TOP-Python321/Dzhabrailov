ticket = int(input())

# ПЕРЕИМЕНОВАТЬ: у вас в эти переменные вся математика сохраняется? сомневаюсь. part1 и part2 ничем не хуже — или trio1 и trio2, как у вас же ниже — фейспалм, конечно, галимый, но на худой конец сойдёт и так
math = ticket // 1000
math2 = ticket % 1000

# ПЕРЕИМЕНОВАТЬ: number — число; digit — цифра числа
number1 = math % 10
number2 = math % 100 // 10
number3 = math // 100

number4 = math2 % 10
number5 = math2 % 100 // 10
number6 = math2 // 100

trio1 = number1+number2+number3
trio2 = number4+number5+number6

# ИСПРАВИТЬ: для разовых проверок используйте конструкцию if...elif...else
while trio1 == trio2:
    print("да")
    break
while trio1 != trio2:
    print("нет")
    break

# ОТВЕТИТЬ: способ ваш хороший, но наводит на мысли — может, вы индексацию и взятие срезов не поняли?

# Создал поле ввода , посчитал деление без остатка и остаток от деления, вычислил с каждого по числу,
# посчитал первую тройку и вторую, дальше работа циклов
# КОММЕНТАРИЙ: нет здесь у вас никаких циклов, в том-то и дело


# ДОБАВИТЬ: результат выполнения кода с СОБСТВЕННЫМИ данными


# ИТОГ: хорошо — 2/3
