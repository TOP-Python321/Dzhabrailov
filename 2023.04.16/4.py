coordinate_1 = input()
coordinate_2 = input()

sum_1 = ord(coordinate_1[0]) + int(coordinate_1[1])
sum_2 = ord(coordinate_2[0]) + int(coordinate_2[1])
sum_coord = sum_1 + sum_2

if 'a' <= coordinate_1[0] <= 'h'
        and 'a' <= coordinate_2[0] <= 'h'
        
        and 1 <= int(coordinate_1[1]) <= 8
        and 1 <= int(coordinate_2[1]) <= 8):
    if sum_coord % 2 == 0:
        print('Да')
    else:
        print('Нет')

# a1
# b2
    
# да
