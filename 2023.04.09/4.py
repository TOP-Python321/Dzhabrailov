nom = int(input())
while nom < 100:
    print("Введите трёхзначное число")
    break
    
while nom > 999:
    print("Введите трёхзначное число")
    break
    
while 100 < nom < 1000:
    nom1 = int(nom) % 10
    nom2 = int(nom) % 100 // 10
    nom3 = int(nom) // 100
    print("Сумма цифр =", nom1+nom2+nom3,"\nПроизведение цифр =", nom1*nom2*nom3) 
    break