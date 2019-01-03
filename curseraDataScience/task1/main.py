#Условие задачи под кодом
import re
import numpy as np
import scipy.spatial as scsp

#Открываем файл
sentenceFile = open(".git/pyTasks/curseraDataScience/task1/sentences.txt")

#Получаем список пердложений, разделенных на слова (пустые слова убраны). Слова приведены к нижнему регистру.
sentencelist = [[word for word in re.split('[^a-z]', line.lower()) if word != "" ] for line in sentenceFile.readlines()] 

#Создаем список всех встречающихся слов - словарь с парами "слово"-"номер (нумерация с нуля)"
wordsDict = {}
for lines in sentencelist:
    for word in lines:
        if wordsDict.get(word) == None:
            wordsDict.update([(word, len(wordsDict))])

#Создаем матрицу, заполняем: строки - номер строки в файле; столбцы - количество повторов слова из словаря wordsDict в строке 
matrix = np.zeros((len(sentencelist), len(wordsDict)))
for i, line in enumerate(sentencelist):
    for word in line:
        matrix[i, wordsDict.get(word)] += 1

#Находим косинусное расстояние между нулевой строкой и всеми остальными - чем ближе к нулю, тем вероятнее предложения совпадают по смыслу. 
for i, line in enumerate(matrix):
    print('Косинусное расстояние для пары 0_' + str(i) + ' = ' + str(scsp.distance.cosine(matrix[0], line)))  


# Задача: Сравнение предложений
# Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" в одном из трех смыслов:

# кошки (животные)
# UNIX-утилита cat для вывода содержимого файлов
# версии операционной системы OS X, названные в честь семейства кошачьих
# Задача — найти два предложения, которые ближе всего по смыслу к расположенному в самой первой строке. В качестве меры близости по смыслу мы будем использовать косинусное расстояние.
# Взято отсюда: https://www.coursera.org/learn/mathematics-and-python/programming/QySgp/linieinaia-alghiebra-skhodstvo-tiekstov-i-approksimatsiia-funktsii