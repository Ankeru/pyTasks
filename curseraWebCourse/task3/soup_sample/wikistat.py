from bs4 import BeautifulSoup
import re
import os    
    
# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path, reg):
    proceded.append(start)
    newLinks = re.findall(reg, open("{}{}".format(path,start), 'r').read())
    links = []
    for link in newLinks:
        if (link in files) and (link not in links) and (link not in proceded):
            links.append(link)
            if files.get(link) == None:
                files[link] = start
                if link == end:
                    return files
    for link in links:
        build_tree(link, end, path, reg)
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    global  files
    global proceded
    proceded = []
    files = dict.fromkeys(os.listdir(path))
    smth = build_tree(start, end, path, re.compile(r"(?<=/wiki/)[\w()]+"))
    bridge = [end]
    while True:
        parent = files[bridge[-1]]
        bridge.append(parent)
        if parent == start:
            break
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    # bridge = [end, start]
    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")
        body = soup.find(id="bodyContent")
       
        
        imgs = 0
        #success
        for img in body.find_all('img'):
            if int(img.get('width') or 0) >= 200:
                imgs += 1
        #fail
        headers = 0
        for title in body.find_all(["h{}".format(i) for i in range(1,7)]):
            if title.span != None:
                strr = title.span.string
            else:
                strr = title.string
            if strr != None:
                if strr[0] == 'E' or strr[0] == 'T' or strr[0] == 'C':
                    headers+=1
        
        
        # TODO посчитать реальные значения
        # imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        # headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]
    print(out)
    return out
