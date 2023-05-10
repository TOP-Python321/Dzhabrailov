coordinate_1 = input()
coordinate_2 = input()    

if ('a' <= coordinate_1[0] <= 'h' 
        and 'a' <= coordinate_2[0] <= 'h'
        and 1 <= int(coordinate_1[1]) <= 8
        and 1 <= int(coordinate_2[1]) <= 8):
    if (-1 <= ord(coordinate_1[0]) - ord(coordinate_2[0]) <= 1
            and -1 <= int(coordinate_1[1]) - int(coordinate_2[1]) <= 1):
        print('Да')
    else:
        print('Нет')
# d4
# c3
# Да

# d4
# c8
# Нет