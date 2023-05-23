coordinate_1 = input()
coordinate_2 = input()

sum_1 = ord(coordinate_1[0]) + int(coordinate_1[1])
sum_2 = ord(coordinate_2[0]) + int(coordinate_2[1])
sum_coord = sum_1 + sum_2

# КОММЕНТАРИЙ: уж при копировании-то чужого кода можно хотя бы ошибок не допускать?
if 'a' <= coordinate_1[0] <= 'h'
        and 'a' <= coordinate_2[0] <= 'h'
        
        and 1 <= int(coordinate_1[1]) <= 8
        and 1 <= int(coordinate_2[1]) <= 8):
    if sum_coord % 2 == 0:
        print('Да')
    else:
        print('Нет')


# КОММЕНТАРИЙ: вы не запускали этот код, и не могли получить эти значения
# a1
# b2
# да


# ИТОГ: переделать — 0/5
