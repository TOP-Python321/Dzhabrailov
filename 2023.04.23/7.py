text = str(input())
need_delite = ".,:;!?–—\'\"()*/"
end_rez = text.split()
end_rez = ''.join([char for char in text if char not in need_delite])

print(end_rez)

# Получаем текст, указываем какие символы нужно будет удалить, создаём разделение, через join удаляем символы и принтуем

# Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.

# Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита