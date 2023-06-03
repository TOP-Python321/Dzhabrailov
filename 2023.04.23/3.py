num = int(input())
# ПЕРЕИМЕНОВАТЬ: не использовать имена встроенных функций
sum = 0

# ИСПОЛЬЗОВАТЬ: имена переменных i, j, k используются только для индексов, а здесь вы перебираете делители — всегда предпочтительнее называть вещи своими именами: делитель — divisor, div
# ИСПРАВИТЬ: цикл ниже выполняет лишние итерации — подумайте, при каких значениях div остаток от деления никогда не сможет быть равным нулю и соответствующим образом ограничьте диапазон с помощью range()
for div in range(num + 1):
    # ИСПРАВИТЬ: первое условие очень неоптимально помещать сюда
    # КОММЕНТАРИЙ: выше вы генерируете последовательность, в которой ноль встречается только один раз — но вы продолжаете с завидным упорством проверять каждое последующее число: не ноль ли? и это каждый раз бесполезно, потому что последовательность возрастающая, там нет и не может быть ноля на всех итерациях, кроме первой — вот так и возникают тормоза в приложениях — так может вместо этого условия сгенерировать последовательность в range() так, чтобы в ней не было ноля?
    if div != 0 and num % div == 0:
        sum += div
print(sum)

# Получаем число из stdin, создаём функцию sum, потом цикл for, там в функции range добавляю +1,
# т.к при условном значении 5 повторяться будет 4 (т.к начинается с 0), пропускаем 0
# и проверяем - 0 не считаем, если число делится на div полностью, то добавляем к sum, когда заканчивается - выводится


# ДОБАВИТЬ: результат выполнения кода с СОБСТВЕННЫМИ данными


# ИТОГ: работает, но нужно лучше — 2/5
