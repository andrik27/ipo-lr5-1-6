stri = open('D:/profiles/krachkA_82/Desktop/ghg/text.txt','r',encoding='utf-8') #открытие файла для чтения
out = open('D:/profiles/krachkA_82/Desktop/ghg/output.txt','w',encoding='utf-8') #открытие файла для записи
i = 1 #задаем значение переменной 
for line in stri: #Проходим по каждой строке
    out.write(str(i) + " ") #записываем номер строки и пробел 
    out.write(line) #записываем содержимое строки
    i += 1 #счетчик
stri.close() #закрытие файла
out.close() #закрытие файла
