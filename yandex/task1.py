def get_date_time(time_date):
    """Возвращает 2 кортежа: разделенные элементы даты и времени"""
    spl = time_date.split(' ')
    date = spl[0].split("-")
    time = spl[1].split(":")
    return date, time
def calc_secs(time_start, time_end):
    """Считает кол-во секунд, затраченное а. на задачу"""
    tds = get_date_time(time_start)
    tde = get_date_time(time_end) 
    tde_date = list(map(lambda x:int(x),tde[0] ))
    tde_time = list(map(lambda x:int(x),tde[1] ))
    tds_date = list(map(lambda x:int(x),tds[0] ))
    tds_time = list(map(lambda x:int(x),tds[1] ))
    return  ((((((tde_date[0] -tds_date[0])*365 + tde_date[1] -tds_date[1])*30 
     + tde_date[2] -tds_date[2])*24 + tde_time[0] -tds_time[0])*60 + tde_time[1]
      -tds_time[1])*60 + tde_time[2] -tds_time[2])
    

ac_list = []
with open('data_task4_old.txt') as f:    
    firstline = True
    for line in f:
        # Пропуск первой строки
        if firstline: 
            firstline = False
            continue
        sp = line.split('\t')
        to_list = sp[:3]     
        to_list.append(calc_secs(sp[3], sp[4]))
        ac_list.append(to_list)
#Находим сумму секунд по всем задачам и количество микрозадач 
sym = 0
zad = 0
for line in ac_list:
    sym+= line[-1]
    zad+= float(line[-2])
print(f'Ответ = srednee*n/30= {sym}/({zad}*30)=', sym/zad/30,  'n')
 
