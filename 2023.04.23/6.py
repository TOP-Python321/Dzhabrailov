ticket = int(input())

math = ticket // 1000
math2 = ticket % 1000

number1 = math % 10
number2 = math % 100 // 10
number3 = math // 100

number4 = math2 % 10
number5 = math2 % 100 // 10
number6 = math2 // 100

trio1 = number1+number2+number3
trio2 = number4+number5+number6

while trio1 == trio2:
    print("да")
    break
while trio1 != trio2:
    print("нет")
    break
    
#Создал поле ввода , посчитал деление без остатка и остаток от деления, вычислил с каждого по числу, 
# посчитал первую тройку и вторую, дальше работа циклов

    # 183534

    # да

    # 401367

    # нет
    
    # 123456
    
    # нет