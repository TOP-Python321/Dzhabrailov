number = int(input())
while number < 100:
    print("Введите трёхзначное число")
    number = int(input())
    break

while number > 999:
    print("Введите трёхзначное число")
    number = int(input())
    break

while 100 < number < 1000:
    number1 = number % 10
    number2 = number % 100 // 10
    number3 = number // 100
    print("Сумма цифр =", number1+number2+number3, "\nПроизведение цифр =", number1*number2*number3)
    break


# ДОБАВИТЬ: результат ВЫПОЛНЕНИЯ программы с собственными данными


# ИТОГ: хорошо — 2/3
