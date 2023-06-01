coordinate_1 = input()
coordinate_2 = input()

if ('a' <= coordinate_1[0] <= 'h'
        and 'a' <= coordinate_2[0] <= 'h'
        and 1 <= int(coordinate_1[1]) <= 8
        and 1 <= int(coordinate_2[1]) <= 8):
    if coordinate_1[0] == coordinate_2[0] or int(coordinate_1[1]) == int(coordinate_2[1]):
        print('да')
    else:
        print('нет')


# ДОБАВИТЬ: результат выполнения программы с собственными данными
# d4
# e4
# да

# a2
# c4
# нет


# ИТОГ: пишите и выполняйте свой код, только потом смотрите чужой — 2/3
