number = int(input())

fib = []

fib.append(0)
fib.append(1)


for i in range(2, number+1):
    fib.append(fib[i-1] + fib[i-2])

for i in range(number):
        print(fib[i+1])
        
# получаю число, создаю список для хранения, вычисляю первые два числа и добавляю их в список
# далее считаю от 2 числа до n + 1, добавляю в список с подсчётом, вывожу результат


    # 1


    # 1


    # 17

    # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597