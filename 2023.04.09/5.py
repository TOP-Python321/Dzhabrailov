integer = int(input())
fractional_number = int(input())

# ИСПРАВИТЬ: а если пользователю понадобится ввести дробную часть для числа 7.1234? думайте обо всех возможностях, а не об одной частной — как написать код, который правильно преобразует любую комбинацию целой и дробной части в одно вещественное число?
while fractional_number < 10:
    fractional_number2 = fractional_number / 10
    break
while fractional_number > 9:
    fractional_number2 = fractional_number / 100
    break
# УДАЛИТЬ: этот блок вообще непонятно зачем нужен (см. пример ниже)
while fractional_number > 99:
    fractional_number2 = fractional_number / 100
    print("ну и ну, ну ладно, посчитаем будто целые мили добавлены")
    break

result_mile = integer + fractional_number2

print(result_mile, "миль =", round(result_mile*1.61, 1), "км")


# КОММЕНТАРИЙ: пример выполнения для fractional_number > 99
# 12
# 1234
# ну и ну, ну ладно, посчитаем будто целые мили добавлены
# КОММЕНТАРИЙ: число миль должно было получиться 12.1234
# 24.34 миль = 39.2 км


# ДОБАВИТЬ: результат ВЫПОЛНЕНИЯ программы с собственными данными


# ИТОГ: переделать — 2/4
