# ИСПРАВИТЬ здесь и далее везде: PEP 8 не рекомендует отделять пробелом скобки вызова от имени функции
name = input ("Введите ваше имя: ")
# ИСПРАВИТЬ здесь и далее везде: PEP 8 не рекомендует использовать транслитерацию в именах переменных
fam = input ("Введите вашу фамилию: ")
god = input ("Введите год рождения: ")
# ИСПРАВИТЬ: число 2023 создаётся сразу как объект int — его не нужно преобразовывать
god = int(2023) - int(god)

# ИСПРАВИТЬ: вывод не соответствует требуемому формату (лишний пробел)
print(name, fam, ",", god)


# ДОБАВИТЬ: результат выполнения программы — в закомментированном виде
# КОММЕНТАРИЙ: это требование, прописанное в задании — невыполнение требований задания влечёт снижение баллов


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода:
#   https://peps.python.org/pep-0008/

# КОММЕНТАРИЙ: наверняка это поможет вам подобрать правильные имена переменным:
#   https://translate.yandex.ru/?source_lang=ru&target_lang=en


# ИТОГ: плохо — 1/3
