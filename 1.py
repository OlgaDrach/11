import struct 
with open('f.txt', 'wb') as f:  # Відкриваємо файл f 
    pack = [] 
    p = int(input('Введіть к-сть елементів у файлі: ')) 
    for h in range(p):      #Записуємо додатні і від'ємні числа у список
        if h % 2 == 0: 
            pack.append(int(input('Введіть додатне число: '))) 
        else: 
            pack.append(int(input('Введіть від*ємне число: '))) 
    a = (struct.pack(f'{p}h', *pack))     #Записуємо закодовані числа
    f.write(a) 
with open('f.txt', 'rb') as f:      #Розкодовуємо файл f, і переводимо його данні у відсортований список, типу int 
    unpack = sorted([h[0] for h in struct.iter_unpack('h', f.read())])
with open('g.txt', 'a') as g: 
    with open('h.txt', 'w') as h: 
        res = [] 
        for h in range(len(unpack) // 3):     #Записуємо по 3 додатніх і від'ємних значення 
            flag = False if h % 2 != 0 else True 
            unpack = sorted(unpack, reverse=flag) 
            print(unpack) 
            res.extend(unpack[0:3])     #Беремо значення з кінця
            unpack = unpack[3::]      #Беремо значення з початку
        res.extend(unpack) 
        for h in range(len(res)):      #Із списку по елементно записуємо данні у файл g 
            g.write(str(res[h])) 
with open('g.txt', 'r') as g: 
    print(g.read())     #Вивиодимо файл g
