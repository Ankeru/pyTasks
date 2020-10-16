ac_dict = {}
with open('data_task3.csv') as f:    
    firstline = True
    for line in f:
        # Пропуск первой строки
        if firstline: 
            firstline = False
            continue
        sp = line.split('\t')
        # Очищение данных - удачление символа возврата каретки
        sp[-1] = sp[-1].replace('\n','')
        # Сравниваем оценку а. и истинную
        compare_result = sp[-2] == sp[-1]
        if compare_result:
            value = [1, 1]
        else:
            value = [0, 1]
        if ac_dict.get(sp[0]) is None:            
            ac_dict[sp[0]] = value
        else:
            ac_dict[sp[0]][0] += value[0]
            ac_dict[sp[0]][1] += value[1]
final_list = []
for k in ac_dict:
    final_list+= [[k, ac_dict[k][0]/ac_dict[k][1]]]
# Функция для сортировки - выдает процент правильных оценок
def sort_col(i):
    return i[1]
final_list.sort(key=sort_col)
print('10 наименьших результатов:', final_list[:10])
