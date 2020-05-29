from random import randint 
 
def generateFile(filename='f'): 
    components = randint(2, 100) 
    while components%5 != 0: 
        components += 1 
    with open(filename, 'w') as f: 
        listToWrite = [] 
        for i in range(components//2): 
            listToWrite.append(randint(-100, -1)) 
            listToWrite.append(randint(1, 100)) 
        listToWrite = sorted(listToWrite) 
        f.write(' '.join(map(str, listToWrite))) 
 
def writeToG(filename='g', filenameRead='f'): 
    with open(filenameRead, 'r') as f: 
        listn = list(map(int, f.read().split(' '))) 
    newList = [] 
    with open('g', 'w') as g: 
        for i in range(len(listn)//3): 
            flag = True if i%2 != 0 else False 
            listn = sorted(listn, reverse=flag) 
            newList.extend(listn[0:3]) 
            listn = listn[3::] 
        g.write(' '.join(map(str, newList))) 
if name == '__main__': 
# Те що, написано нижче спрацює лише тоді коли скрипт буде запущений вручну
    generateFile() 
    writeToG()
