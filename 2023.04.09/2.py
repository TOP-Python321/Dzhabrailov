num = input("Введите число ")

# КОММЕНТАРИЙ: объявление данных переменных можно считать избыточным, если принять во внимание простоту используемых выражений выражений и то, что в дальнейшем каждая из переменных используется только единожды
next_num = int(num) + 1
# ИСПРАВИТЬ: попытка использовать не объявленную ранее переменную — number — приводит к исключению
previous_num = int(number) - 1

# ИСПОЛЬЗОВАТЬ: альтернативный вариант записи строковых литералов в несколько строчек (только внутри скобок)
print(f"Следующее за числом {num} число: {next_num} \n"
      f"Для числа {num} предыдущее число: {previous_num}")


# ДОБАВИТЬ: результат ВЫПОЛНЕНИЯ программы с собственными данными
# Пример ввода:
    # 20

# Пример вывода:
    # Следующее за числом 20 число: 21
    # Для числа 20 предыдущее число: 19
# КОММЕНТАРИЙ: поясняю ещё раз: мне нужно увидеть не примеры ввода/вывода, которые я сам написал, а результат выполнения ВАМИ собственного кода
# ОТВЕТИТЬ: очевидно, что как минимум этот код вы сами не запускали, потому что интерпретатор прерывает работу с выбросом исключения из-за несуществующей переменной — так при чём здесь спрашивается примеры ввода/вывода?


# ИТОГ: переделать — 0/3
