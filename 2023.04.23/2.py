n_number = int(input())

# ПЕРЕИМЕНОВАТЬ: sum — это имя встроенной функции, создавая свою переменную с таким же именем вы лишаете себя прямого доступа к встроенной функции — таких ситуаций лучше избегать: например, здесь можно исполььзовать имя positive_sum (сумма положительных) или sum_
sum = 0
# ИСПОЛЬЗОВАТЬ: когда переменная цикла не нужна, то вместо неё пишут _
for _ in range(n_number):
    num = int(input())
    if num > 0:
        sum += num

print(sum)

# Получаю натуральное число из stdin, создаю функцию sum, использую цикл for нужное количество раз (полученное из stdin)
# в цикле - ввожу число, происходит проверка - если оно больше 0, то добавляется в sum, после - выводится сумма чисел


# ДОБАВИТЬ: результат выполнения кода с СОБСТВЕННЫМИ данными


# ИТОГ: хорошо — 2/3
