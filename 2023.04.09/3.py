# ИСПРАВИТЬ: вам не требуется в дальнейшем использовать текущее строковое значение переменной nom, поэтому более эффективно сразу преобразовать возвращаемое значение input() в объект int (исправлено)
minute = int(input())

hour = 60
# КОММЕНТАРИЙ: объявление нижеследующих переменных можно считать избыточным, если принять во внимание простоту используемых выражений выражений и то, что в дальнейшем каждая из переменных используется только единожды
# rez1 = int(nom) // hour  - убрано за ненадобностью
# КОММЕНТАРИЙ: поскольку вы не преобразовали возвращаемое значение input() в число сразу, здесь вам приходится второй раз преобразовывать строку в число — это лишняя работа
# rez2 = int (nom) % hour - убрано за ненадобностью

print(f"{minute} мин - это {minute // hour} час {minute % hour} мин")

# print(f"{nom} мин - это {rez1} час {rez2} мин") - убрано за ненадобностью

# КОММЕНТАРИЙ: имена rez1 и rez2 не помогают понять, что за значения ассоциированы с этими переменными — а ведь я говорил об этом
# КОММЕНТАРИЙ: мне не нравится, когда мои настоятельные рекомендации, проговорённые в лекции, игнорируются — первый раз обращаю внимание, в дальнейшем буду снижать баллы

# ДОБАВИТЬ: результат выполнения программы — в закомментированном виде

# Пример ввода:
    # 150

# Пример вывода:
    # 150 мин - это 2 час 30 мин


# ИТОГ: средне — 2/4
